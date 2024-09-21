import yt_dlp
import os
from sys import argv
   

def create_options():
   options = {}
   if argv[2] == '--video':
      options.update({'format' : 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b'})
   elif argv[2] == '--audio':
      options.update({'format' : 'm4a/bestaudio/best'})

   return  options

try:
   link = argv[1]
   options = create_options()
except:
   options = {'format' : 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b'}
   link = input("Enter the link: ")
   print("custom options not loaded")

with yt_dlp.YoutubeDL(options) as ydl:
   ydl.download([link])

print('video successfully downloaded')