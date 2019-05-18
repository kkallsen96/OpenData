import tweepy
import pandas as pd
import os

# consumer keys and access tokens, used for OAuth
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# creation of the actual interface, using authentication
api = tweepy.API(auth)

# user = api.me()
#
# print('Name: ' + user.name)
# print('Location: ' + user.location)
# print('Friends: ' + str(user.friends_count))

# user = api.get_user('')
#
# print('Name: ' + user.name)
# print('Location: ' + user.location)
# print('Friends: ' + str(user.friends_count))
#
# user_friends = user.friends()
# for friend in user_friends[5:2]:
#     print (friend.screen_name)
#
# search = tweepy.Cursor(api.search, q="Nepal", lang="ne").items(5)

search = tweepy.Cursor(api.search, q="Zacarias Irun", result_type="recent", lang="es").items(100)
diccionario = {}
resultado = []
titulos = []

titulos.append("Tweet")
titulos.append("Autor")
titulos.append("Tiempo de Tweet")
titulos.append("Retweets")
titulos.append("Favs")

for item in search:
    contenido = []
    contenido.append(item.text)
    contenido.append(item.user.name)
    contenido.append(item.created_at)
    contenido.append(item.retweet_count)
    contenido.append(item.favorite_count)

    for i,e in enumerate(titulos):
        diccionario[titulos[i]] = contenido[i]

    resultado.append(diccionario)
    diccionario = {}

df = pd.DataFrame(
        resultado)
df.to_csv('result.csv', index=False)


