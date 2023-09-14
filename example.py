#!/usr/bin/env python3
from plexapi.server import PlexServer
from variables import baseurl, token

plex = PlexServer(baseurl, token)

for sessions in plex.sessions():
    print(sessions)