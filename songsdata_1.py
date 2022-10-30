import os
import json
import csv
import time
import spotipy
import lyricsgenius as lg

import numpy as np
import pandas as pd

import credential
from spotipy.oauth2 import SpotifyClientCredentials

df = pd.read_csv('charts.csv')
artists = list(set(df.artist))

# get songs' lyrics from artist
def get_lyrics(artist):
    
    return None

# search songs name and artist for spotify uri
def get_spotify_uri(artist, song_title):

    return None


# get song features from spotify
def get_features(uri):

    return None

# get data from artist list
def get_data(artists_list):

    return None

# for artist in artists
# search songs by artist from genius
# for song in songs:
# get the lyrics
# spotipy search for song + artist to get the features
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
genius = lg.Genius(os.environ['GENIUS_ACCESS_TOKEN'])

name = 'ed sheeran'
track = 'bad habits'
result = spotify.search(q= f'artist: + {name}, track: + {track}', type='artist,track')
print(json.dumps(result, indent=4, sort_keys=False))
# for artist in artists:

if __name__ == '__main__':
    artists_list = artists[:5]
    get_data(artists_list)
    print(df)
