# Lunegov
A Discord music bot written in Python with support for Youtube, SoundCloud, Spotify, Bandcamp, Twitter, and custom files.

## Prerequisites:

#### API Keys
* Discord - https://discord.com/developers
* Spotify (optional) - https://developer.spotify.com/dashboard/
  - Client ID
  - Client Secret
  - Note: Limited to 50 playlist items without API

Obtained keys must be entered into ```config/config.py``` (or set as environment variables)

#### Requirements

* Installation of Python 3.8+

Install dependencies:
```
pip install -r requirements.txt
```

##### Windows
Download `ffmpeg` and put it into a folder in PATH.

If ffmpeg is not found, the script will try to download it automatically.
##### Other platforms
Install `ffmpeg` and `libopus` packages.

### Installing - Self hosting

1. Download release if available, alternatively download repository zip
2. Complete Prerequisites
3. Start ```run.py``` in project root
4. See configuration options in /config/config.py (more info at https://github.com/Krutyi-4el/DandelionMusic/wiki/Configuration)

Button play plugin:
* Set emoji with the setting command to enable this feature
* Emote must be available for bot
* Needs Manage Message permissions

Custom Cookies:
* Extract cookies.txt from you browser using your preferred method
* Overwrite the existing cookies.txt in /config/cookies/
* (Optional) Set a custom cookies.txt location by modifying COOKIE_PATH in config.py

## Commands:

### Music

After the bot has joined your server, use ```-help``` to display help and command information.


```
-p [link/video title/key words/playlist-link/soundcloud link/spotify link/bandcamp link/twitter link]
```

* Plays the audio of supported website
    - A link to the video (https://ww...)
    - The title of a video ex. (Gennifer Flowers - Fever Dolls)
    - A link to a YouTube playlist
* If a song is playing, it will be added to queue

#### Playlist Commands

```
-skip / -s
```

* Skips the current song and plays next in queue.

```
-q
```

* Show the list of songs in queue

```
-shuffle / -sh
```

* Shuffle the queue

```
-l / -loop [all/single/off]
```

* Loops the entire queue by default. `-loop single` loops current track.

```
-mv / -move
```

* Move song position in queue

#### Audio Commands

```
-pause
```

* Pauses the current song.

```
-resume
```

* Resumes the paused song.

```
-prev
```

* Goes back one song and plays the last song again.

```
-np
```

* Shows more details about the current song.

```
-volume / -vol
```

* Adjust the volume 1-100%
* Pass no arguments for current volume

```
-remove / -rm
```

* Removes a song from the queue (defaults to last song)

```
-stop / -st
```
* Stops the current song and clears the playqueue.


### General

```
-settings / -setting / -set
```
* No Arguments: Lists server settings
* Arguments: (setting) (value)
* Use "unset" as an argument to reset a setting
* Example: -setting start_voice_channel ChannelName
* Administrators only

```
-c
```

* Connects the bot to the user's voice channel

```
-dc
```

* Disconnects the bot from the current voice channel

```
-history
```
* Shows you the titles of the X last played songs. Configurable in config.config.py


### Utility

```
-reset / -rs
```

* Disconnect and reconnect to the voice channel

```
-ping
```

* Test bot connectivity

```
-addbot
```

* Displays information on how to add the bot to another server of yours.

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the [GNU General Public License](LICENSE) as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
