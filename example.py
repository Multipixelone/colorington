#!/usr/bin/env python3
from plexapi.server import PlexServer
from plexapi.utils import download
from variables import baseurl, token
import time

plex = PlexServer(baseurl, token)

while True:
    for media in plex.sessions():
        if media.type == "track" and media.usernames[0] == "Tunnelmaker":
            filename = f"art_{media.parentTitle}.jpg"
            print(f"Currently playing: {media.title}")
            print(f"Album Art: {filename}")
            if not filename.exists():
                print(f"Downloading art...")
                url = media.parentThumb
                url = plex.transcodeImage(url, height=350, width=350)
                download(url, token, filename=filename)
    time.sleep(5)
