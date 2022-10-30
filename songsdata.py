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

# export all the credentials to the local variables named SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
# SPOTIPY_REDIRECT_URL, GENIUS_ACCESS_TOKEN, SPOTIFY_USER_ID

# scope = 'user-read-currently-playing'

uri_list = ['https://play.spotify.com/track/7CFa3xyrZiZNiNeKuxocvZ',
 'https://play.spotify.com/track/3xLT5J7qbKvDiTCNdaRgW3',
 'https://play.spotify.com/track/0RIFH0Gx0GrEjrSkjOkmzU',
 'https://play.spotify.com/track/5uPFOrMHlN0MuGrAExzsaI',
 'https://play.spotify.com/track/1PBx7cbYiqzDykOBCA3SOc',
 'https://play.spotify.com/track/2FvLqe3wIQKPLmB4IAbi23',
 'https://play.spotify.com/track/284y3yJIznK3JTCIBLaWOC',
 'https://play.spotify.com/track/5pyKz3eWCyPxgPqMcO8blh',
 'https://play.spotify.com/track/5RDeLr6aNWt1q35y8cmhmn',
 'https://play.spotify.com/track/6Ady6fcmUjjC2H99X0JW85']



def get_songs_features(uri_list):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    genius = lg.Genius(os.environ['GENIUS_ACCESS_TOKEN'])
    dict_list = []
    for uri in uri_list:
        songDict = {}
        try:
            song = spotify.track(uri)
            features = spotify.audio_features(uri)
            # print(features)
            songDict['artist'] = song['album']['artists'][0]['name']
            songDict['title'] = song['name']
            songDict['danceability'] = features[0]['danceability']
            songDict['energy'] = features[0]['energy']
            songDict['key'] = features[0]['key']
            songDict['loudness'] = features[0]['loudness']
            songDict['mode'] = features[0]['mode']
            songDict['speechiness'] = features[0]['speechiness']
            songDict['acousticness'] = features[0]['acousticness']
            songDict['instrumentalness'] = features[0]['instrumentalness']
            songDict['liveness'] = features[0]['liveness']
            songDict['valence'] = features[0]['valence']
            songDict['tempo'] = features[0]['tempo']
            songDict['duration'] = features[0]['duration_ms']
            songDict['time_signature'] = features[0]['time_signature']
            song = genius.search_song(artist=songDict['artist'], title=songDict['title'])
            lyrics = song.to_dict()
            songDict['lyrics'] = lyrics
        except:
            pass

        dict_list.append(songDict)
    df = pd.DataFrame.from_dict(dict_list)
    return df
    
if __name__ == '__main__':
    sample_uri = ['https://open.spotify.com/album/3h3Kj1ipfSRMWlU8TUPevb?highlight=spotify:track:1sKKqbK0zlQSYRzHggEtvO']
    features_df = get_songs_features(sample_uri)
    # features_df = get_songs_features(uri_list)
    features_df.to_csv(f'sample.csv', index= False, header=True)
    print(features_df)

# columns = ['artist','title','danceability','energy','key',
#             'loudness','mode','speechiness','acousticness',
#             'instrumentalness','liveness','valence','tempo','duration']

# with open()


