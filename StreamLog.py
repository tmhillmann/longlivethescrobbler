import requests
import json
import csv
import sys

# Stream List
resp = requests.get('http://listen.di.fm/[streamlist]')
resplist = resp.json()
respsort = sorted(resplist, key=lambda k: k['name'])
respfinal = []
for i in respsort:
    print(i['id'],"\t",i['name'])
    respfinal.append({'id': i['id'], 'name': i['name'], 'key': i['key']})

# Save Stream List to CSV
with open('streamlist.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'key']
    writer = csv.DictWriter(csvfile, lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()
    for i in respfinal:
        writer.writerow(i)

# Get Track List from Stream ID
streamid = input("Enter Stream ID: ")
tlurl = 'http://api.audioaddict.com/v1/di/track_history/channel/' + streamid
resp = requests.get(tlurl)
resplist = resp.json()
respsort = sorted(resplist, key=lambda k: k['started'])
respfinal = []
for i in respsort:
    if i['artist'] != None:
        if i['title'] != None:
            print(i['artist'],"-",i['title'])
            respfinal.append({'artist': i['artist'], 'title': i['title'], 'duration': i['duration'], 'started': i['started']})

# Save Track List to CSV
with open('tracklist.csv', 'a') as csvfile:
    fieldnames = ['artist', 'title', 'duration', 'started']
    writer = csv.DictWriter(csvfile, lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader() # Removed while appending entries.
    for i in respfinal:
        writer.writerow(i)