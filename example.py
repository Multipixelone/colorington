#!/usr/bin/env python3
from plexapi.server import PlexServer
from plexapi.utils import download
from variables import baseurl, token
#from colorthief import ColorThief
import time
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

plex = PlexServer(baseurl, token)

for media in plex.sessions():
    print(media.viewOffset)
    print(media.duration)

for media in plex.sessions():
    url = None
    if media.type == "track" and media.usernames[0] == "Tunnelmaker":
        print(media.title)
        filename = f"art_{media.parentTitle}.jpg"
        url = media.parentThumb
        url = plex.transcodeImage(url, height=350, width=350)
        download(url, token, filename=filename)
        print(media.viewOffset)
        print(media.duration)
