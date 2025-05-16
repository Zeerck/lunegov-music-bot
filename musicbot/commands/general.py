import asyncio
import discord
from config import config
from discord.ext import commands, bridge
from discord.ext.commands import has_permissions
from musicbot.bot import Context, MusicBot
from musicbot.audiocontroller import AudioController


class General(commands.Cog):
    """Набор команд для перемещения бота по вашему серверу.

    Attributes:
        bot: Экземпляр бота, выполняющего команды.
    """

    def __init__(self, bot: MusicBot):
        self.bot = bot

    # logic is split to uconnect() for wide usage
    @bridge.bridge_command(
        name="connect",
        description=config.HELP_CONNECT_LONG,
        help=config.HELP_CONNECT_SHORT,
        aliases=["c"],
    )
    async def _connect(self, ctx: Context):  # dest_channel_name: str
        audiocontroller = ctx.bot.audio_controllers[ctx.guild]
        if await audiocontroller.uconnect(ctx):
            await ctx.send("Подключён.")

    @bridge.bridge_command(
        name="disconnect",
        description=config.HELP_DISCONNECT_LONG,
        help=config.HELP_DISCONNECT_SHORT,
        aliases=["dc"],
    )
    async def _disconnect(self, ctx: Context):
        audiocontroller = ctx.bot.audio_controllers[ctx.guild]
        if await audiocontroller.udisconnect():
            await ctx.send("Отключён.")
        else:
            await ctx.send(config.NOT_CONNECTED_MESSAGE)

    @bridge.bridge_command(
        name="reset",
        description=config.HELP_RESET_LONG,
        help=config.HELP_RESET_SHORT,
        aliases=["rs", "restart", "cc"],  # this command replaces removed changechannel
    )
    async def _reset(self, ctx: Context):
        await ctx.defer()
        if await ctx.bot.audio_controllers[ctx.guild].udisconnect():
            # bot was connected and need some rest
            await asyncio.sleep(1)

        audiocontroller = ctx.bot.audio_controllers[ctx.guild] = AudioController(
            self.bot, ctx.guild
        )
        if await audiocontroller.uconnect(ctx):
            await ctx.send(
                "{} Присоединён к {}".format(
                    ":white_check_mark:", ctx.author.voice.channel.name
                )
            )

    @bridge.bridge_command(
        name="яйца", description=config.HELP_PING_LONG, help=config.HELP_PING_SHORT
    )
    async def _ping(self, ctx):
        await ctx.send("Уберите руки товарищ!")

    @bridge.bridge_command(
        name="setting",
        description=config.HELP_SETTINGS_LONG,
        help=config.HELP_SETTINGS_SHORT,
        aliases=["settings", "set"],
    )
    @has_permissions(administrator=True)
    async def _settings(self, ctx: Context, setting=None, *, value=None):

        sett = ctx.bot.settings[ctx.guild]

        if setting is None and value is None:
            await ctx.send(embed=sett.format(ctx))
            return

        if setting is None or value is None:
            await ctx.send("Ошибка: параметр или значение отсутствует.")
            return

        response = await sett.process_setting(setting, value, ctx)

        if response is None:
            await ctx.send("`Ошибка: настройка не найдена`")
        elif response is True:
            async with ctx.bot.DbSession() as session:
                session.add(sett)
                await session.commit()
            await ctx.send("Настройка обновлена!")

    @bridge.bridge_command(
        name="addbot",
        description=config.HELP_ADDBOT_LONG,
        help=config.HELP_ADDBOT_SHORT,
    )
    async def _addbot(self, ctx):
        embed = discord.Embed(
            title="Invite",
            description=config.ADD_MESSAGE
            + "({})".format(discord.utils.oauth_url(self.bot.user.id)),
        )

        await ctx.send(embed=embed)


def setup(bot: MusicBot):
    bot.add_cog(General(bot))
