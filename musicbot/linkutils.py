import re
from enum import Enum
from typing import Optional, Union

import aiohttp
import spotipy
from bs4 import BeautifulSoup
from config import config
from spotipy.oauth2 import SpotifyClientCredentials

try:
    sp_api = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=config.SPOTIFY_ID, client_secret=config.SPOTIFY_SECRET
        )
    )
    api = True
except Exception:
    api = False

url_regex = re.compile(
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}


def clean_sclink(track: str) -> str:
    return re.sub(r"^https?://m\.", "https://", track)


async def convert_spotify(url: str) -> str:

    result = url_regex.search(url)
    if result and "?si=" in url:
        url = result.group(0) + "&nd=1"

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            page = await response.text()

    soup = BeautifulSoup(page, "html.parser")

    title = soup.find("title").string
    return re.sub(r"(.*) - song( and lyrics)? by (.*) \| Spotify", r"\1 \3", title)


async def get_spotify_playlist(url: str) -> list:
    """Вернуть класс Spotify_Playlist"""

    code = url.split("/")[4].split("?")[0]

    if api:
        results = None
        try:
            if "open.spotify.com/album" in url:
                results = sp_api.album_tracks(code)

            if "open.spotify.com/playlist" in url:
                results = sp_api.playlist_items(code)

            if results:
                tracks = results["items"]
                while results["next"]:
                    results = sp_api.next(results)
                    tracks.extend(results["items"])
                links = []
                for track in tracks:
                    try:
                        links.append(
                            track.get("track", track)["external_urls"]["spotify"]
                        )
                    except KeyError:
                        pass
                return links
        except Exception:
            if config.SPOTIFY_ID != "" or config.SPOTIFY_SECRET != "":
                print("ОШИБКА: Проверьте Spotify CLIENT_ID и SECRET")

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url + "&nd=1") as response:
            page = await response.text()

    soup = BeautifulSoup(page, "html.parser")

    results = soup.find_all(attrs={"name": "music:song", "content": True})

    links = []

    for item in results:
        links.append(item["content"])

    title = soup.find("title")
    title = title.string

    return links


def get_url(content: str) -> Optional[str]:
    result = url_regex.search(content)
    if result:
        return result.group(0)
    return None


class Sites(Enum):
    Spotify = "Spotify"
    Spotify_Playlist = "Spotify Playlist"
    YouTube = "YouTube"
    Twitter = "Twitter"
    SoundCloud = "SoundCloud"
    Bandcamp = "Bandcamp"
    Custom = "Custom"
    Unknown = "Unknown"


class Playlist_Types(Enum):
    Spotify_Playlist = "Spotify Playlist"
    YouTube_Playlist = "YouTube Playlist"
    BandCamp_Playlist = "BandCamp Playlist"
    Unknown = "Unknown"


class Origins(Enum):
    Default = "Default"
    Playlist = "Playlist"


def identify_url(url: Optional[str]) -> Sites:
    if url is None:
        return Sites.Unknown

    if "https://www.youtu" in url or "https://youtu.be" in url:
        return Sites.YouTube

    if "https://open.spotify.com/track" in url:
        return Sites.Spotify

    if (
        "https://open.spotify.com/playlist" in url
        or "https://open.spotify.com/album" in url
    ):
        return Sites.Spotify_Playlist

    if "bandcamp.com/track/" in url:
        return Sites.Bandcamp

    if "https://twitter.com/" in url:
        return Sites.Twitter

    if url.lower().endswith(config.SUPPORTED_EXTENSIONS):
        return Sites.Custom

    if "soundcloud.com/" in url:
        return Sites.SoundCloud

    # If no match
    return Sites.Unknown


def identify_playlist(url: Optional[str]) -> Union[Sites, Playlist_Types]:
    if url is None:
        return Sites.Unknown

    if "playlist?list=" in url:
        return Playlist_Types.YouTube_Playlist

    if (
        "https://open.spotify.com/playlist" in url
        or "https://open.spotify.com/album" in url
    ):
        return Playlist_Types.Spotify_Playlist

    if "bandcamp.com/album/" in url:
        return Playlist_Types.BandCamp_Playlist

    return Playlist_Types.Unknown
