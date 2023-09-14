#!/usr/bin/env python3
from plexapi.server import PlexServer
from plexapi.utils import download
from variables import baseurl, token
from colorthief import ColorThief
import time
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

plex = PlexServer(baseurl, token)

for media in plex.sessions():
    url = None
    if media.type == "track" and media.usernames[0] == "Tunnelmaker":
        print(media.title)
        filename = 'session_transcode_%s%s' % (media._prettyfilename(), ".jpg")
        url = media.parentThumb
        url = plex.transcodeImage(url, height=300, width=300)
        download(url, token, filename=filename)
        color_thief = ColorThief(filename)
        #dominant_color = color_thief.get_color(quality=1)
        Canvas = np.array(color_thief.get_palette(quality=1, color_count=6), dtype=np.uint8)
        print(Canvas)
        image = Image.fromarray(Canvas.astype(np.uint8))
        plt.imshow(Canvas)
        plt.show()

