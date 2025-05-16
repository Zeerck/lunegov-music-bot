# fmt: off

import os
from typing import Optional

from musicbot.utils import get_env_var, alchemize_url


BOT_TOKEN: str = get_env_var("BOT_TOKEN", "")
SPOTIFY_ID: str = get_env_var("SPOTIFY_ID", "")
SPOTIFY_SECRET: str = get_env_var("SPOTIFY_SECRET", "")

BOT_PREFIX: Optional[str] = get_env_var("BOT_PREFIX", "-")  # set to None to disable
MENTION_AS_PREFIX = True
ENABLE_SLASH_COMMANDS = get_env_var("ENABLE_SLASH_COMMANDS", False)

ENABLE_BUTTON_PLUGIN = True

EMBED_COLOR = 0x4dd4d0  # replace after'0x' with desired hex code ex. '#ff0188' >> '0xff0188'

SUPPORTED_EXTENSIONS = (".webm", ".mp4", ".mp3", ".avi", ".wav", ".m4v", ".ogg", ".mov")

MAX_SONG_PRELOAD = get_env_var("MAX_SONG_PRELOAD", 5)   # maximum of 25


COOKIE_PATH = "/config/cookies/cookies.txt"

GLOBAL_DISABLE_AUTOJOIN_VC = False

VC_TIMEOUT = get_env_var("VC_TIMEOUT", 600)  # seconds
VC_TIMOUT_DEFAULT = get_env_var("VC_TIMOUT_DEFAULT", True)  # default template setting for VC timeout true= yes, timeout false= no timeout
ALLOW_VC_TIMEOUT_EDIT = True  # allow or disallow editing the vc_timeout guild setting


actual_prefix = (  # for internal use
    BOT_PREFIX
    if BOT_PREFIX is not None
    else ("/" if ENABLE_SLASH_COMMANDS else "@bot ")
)

# if database is not one of sqlite, postgres or MySQL
# you need to provide the url in SQL Alchemy-supported format.
# Must be async-compatible
# CHANGE ONLY IF YOU KNOW WHAT YOU'RE DOING
DATABASE = alchemize_url(
    get_env_var("DATABASE_URL", os.getenv("HEROKU_DB") or "sqlite:///settings.db")
)


STARTUP_MESSAGE = "Запуск бота..."
STARTUP_COMPLETE_MESSAGE = "Запуск завершён"

NO_GUILD_MESSAGE = "Ошибка: Пожалуйста, присоединитесь к голосовому каналу или введите команду в чате сервера."
USER_NOT_IN_VC_MESSAGE = "Ошибка: Пожалуйста, присоединитесь к голосовому каналу, чтобы использовать команды"
WRONG_CHANNEL_MESSAGE = "Ошибка: Пожалуйста, используйте настроенный командный канал"
NOT_CONNECTED_MESSAGE = "Ошибка: Бот не подключен ни к одному голосовому каналу"
ALREADY_CONNECTED_MESSAGE = "Ошибка: Уже подключен к голосовому каналу"
CHANNEL_NOT_FOUND_MESSAGE = "Ошибка: Не удалось найти канал"
DEFAULT_CHANNEL_JOIN_FAILED = "Ошибка: Не удалось присоединиться к голосовому каналу по умолчанию"
INVALID_INVITE_MESSAGE = "Ошибка: Недействительная ссылка для приглашения"

ADD_MESSAGE = "Чтобы добавить этого бота на свой сервер, нажмите [здесь]"  # brackets will be the link text

INFO_HISTORY_TITLE = "Проигранные песни:"
MAX_HISTORY_LENGTH = get_env_var("MAX_HISTORY_LENGTH", 10)
MAX_TRACKNAME_HISTORY_LENGTH = get_env_var("MAX_TRACKNAME_HISTORY_LENGTH", 15)

SONGINFO_UPLOADER = "Автор: "
SONGINFO_DURATION = "Длительность: "
SONGINFO_SECONDS = "с"
SONGINFO_LIKES = "Лайки: "
SONGINFO_DISLIKES = "Дизлайки: "
SONGINFO_NOW_PLAYING = "Сейчас играет"
SONGINFO_QUEUE_ADDED = "Добавлено в очередь"
SONGINFO_SONGINFO = "Информация о песне"
SONGINFO_ERROR = "Ошибка: Неподдерживаемый сайт или контент с возрастными ограничениями."
SONGINFO_PLAYLIST_QUEUED = "Плейлист в очереди :page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "Неизвестно"
QUEUE_EMPTY = "Очередь пуста :x:"

HELP_ADDBOT_SHORT = "Добавить бота на другой сервер"
HELP_ADDBOT_LONG = "Дает вам ссылку для добавления этого бота на другой сервер."
HELP_CONNECT_SHORT = "Подключить бота к голосовому каналу"
HELP_CONNECT_LONG = "Подключает бота к голосовому каналу, в котором вы находитесь"
HELP_DISCONNECT_SHORT = "Отключить бота от голосового канала"
HELP_DISCONNECT_LONG = "Отключить бота от голосового канала и выключить воспроизведение."

HELP_SETTINGS_SHORT = "Просмотр и установка настроек бота"
HELP_SETTINGS_LONG = "Просмотр и установка настроек бота на сервере. Использование: {}settings setting_name value".format(actual_prefix)

HELP_HISTORY_SHORT = "Показать историю воспроизведения"
HELP_HISTORY_LONG = "Показать " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " последние проигранные треки."
HELP_PAUSE_SHORT = "Поставить на паузу"
HELP_PAUSE_LONG = "Приостанавливает воспроизведение музыки. Используйте его снова, чтобы возобновить воспроизведение."
HELP_VOL_SHORT = "Изменить громкость в %"
HELP_VOL_LONG = "Изменяет громкость трека. Указывается %, на который должена быть установлена громкость."
HELP_PREV_SHORT = "Предыдущий трек"
HELP_PREV_LONG = "Проигрывает предыдущий трек"
HELP_SKIP_SHORT = "Пропустить трек"
HELP_SKIP_LONG = "Пропускает текущий трек и переходит к следующему в очереди."
HELP_SONGINFO_SHORT = "Информация о текущей песне"
HELP_SONGINFO_LONG = "Показывает сведения о текущем треке и показывает ссылку на него."
HELP_STOP_SHORT = "Остановить воспроизведение"
HELP_STOP_LONG = "Останавливает воспроизведение и очищает очередь"
HELP_MOVE_LONG = f"{actual_prefix}move [номер трека в очереди] [новый номер трека в очереди]"
HELP_MOVE_SHORT = "Перемещает трек в очереди"
HELP_YT_SHORT = "Воспроизвести поддерживаемую ссылку или выполнить поиск на YouTube"
HELP_YT_LONG = f"{actual_prefix}p [link/video title/keywords/playlist/soundcloud link/spotify link/bandcamp link/twitter link]"
HELP_PING_SHORT = "Ты чё дебил"
HELP_PING_LONG = "Тестируем на долбаёба"
HELP_CLEAR_SHORT = "Очистить очередь."
HELP_CLEAR_LONG = "Очищает очередь и пропускает текущий трек."
HELP_LOOP_SHORT = "Зацикливает текущий трек или очередь."
HELP_LOOP_LONG = "Зацикливает текущий трек или очередь. Режимы all/single/off."
HELP_QUEUE_SHORT = "Показывает треки в очереди."
HELP_QUEUE_LONG = "Показывает количество треков в очереди, до 10."
HELP_SHUFFLE_SHORT = "Перемешать очередь"
HELP_SHUFFLE_LONG = "Произвольная сортировка треков в текущей очереди"
HELP_RESET_SHORT = "Отключить и снова подключить"
HELP_RESET_LONG = "Остановить проигрыватель, отключить и снова подключиться к каналу, на котором вы находитесь"
HELP_REMOVE_SHORT = "Удалить песню"
HELP_REMOVE_LONG = "Позволяет удалить песню из очереди, введя ее позицию (по умолчанию последняя песня)."

ABSOLUTE_PATH = ""  # do not modify
