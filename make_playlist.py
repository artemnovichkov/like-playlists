#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
from yandex_music.client import Client
import datetime
import re

client = Client.from_credentials(os.environ['LOGIN'], os.environ['PASSWORD'])

# get previous day
yesterday = datetime.date.today() - datetime.timedelta(days=1)

# get liked tracks for selected month and year
tracks = []
for track in client.users_likes_tracks():
  date = datetime.datetime.fromisoformat(track.timestamp)
  if date.year == yesterday.year and date.month == yesterday.month:
  	tracks.append(track)
  else:
  	break

# create a new playlist if needed
if len(tracks) == 0:
  print('No tracks')
else:
  months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
  playlist = client.usersPlaylistsCreate("Лайки за {} {}".format(months[yesterday.month - 1], yesterday.year))
  for track in tracks:
    playlist = client.usersPlaylistsInsertTrack(playlist.kind, track.track.id, track.track.albums[0].id, 0, playlist.revision)
  # update url in README
  url = "https://music.yandex.com/users/{}/playlists/{}".format(playlist.owner.login, playlist.kind)
  with open ('README.md', 'r+' ) as f:
    content = f.read()
    content_new = re.sub('https://music.yandex.com/users/.*\d', url, content, flags = re.M)
    f.seek(0)
    f.write(content_new)
    f.truncate()