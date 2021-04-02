#IGDB API access
#Swadesh Malneedi

import requests
import json
import mysql.connector


mydb = mysql.connector.connect(
  user="sql5403007",
  password="3CaWiJcpI5",
  host="sql5.freemysqlhosting.net",
  database="sql5403007"
)
mycursor = mydb.cursor()

res = requests.post('https://id.twitch.tv/oauth2/token?client_id=khkc6i5cwvbln0ki3wo9u5mtw4qj64&client_secret=5b73meb9a1uugfop5ft4lge5tx7nyd&grant_type=client_credentials')
result = res.json()
headers = {
  'Client-ID': 'khkc6i5cwvbln0ki3wo9u5mtw4qj64',
  'Authorization': 'Bearer ' + result['access_token']
} 
# url = requests.get('https://api.igdb.com/v4/games?fields=*', headers=headers)

url = requests.get('https://api.igdb.com/v4/companies?fields=*', headers=headers)
json_data = url.json()

#print(json_data)

 #Sample INSERT statement to see if connection to DB is present.
# sql = "INSERT INTO games(name, aggregated_rating_count) VALUES (%s, %s)"
# val = ("hello","23")
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")
 

#Example professor showed me during meeting.
for i in range(0,3):
  #start_date = json_data[i]['start_date']
  name = json_data[i]['name']
  slug = json_data[i]['slug']
 # print(start_date)
  print(name)
  print(slug)
  sql = "INSERT INTO games (name, slug) VALUES (%s, %s)"
  val = (name, slug)
  mycursor.execute(sql,val)
  mydb.commit()
  print("record inserted.")


# url = requests.get('https://api.igdb.com/v4/companies?fields=*', headers=headers)
# data = url.json()
# for game in data():
#   sql = "INSERT INTO games (name, slug, start_date) VALUES (%s, %s, %s)"
#   val = (game['name'], game['slug'], game['start_date'])
#   mycursor.execute(sql,val)
#   mydb.commit()
#   print("Game Name: " + game['name'])
#   print("Game Slug: "+ game['slug'])
#   print("Start Date: ", game['start_date'])
#   print("--------------------------------------------")
#   print("record inserted.")

 