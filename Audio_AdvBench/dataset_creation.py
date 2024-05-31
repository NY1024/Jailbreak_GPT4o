import os
import openai
import requests
import time
import json
import time
from openai import OpenAI
import csv 

API_SECRET_KEY = "xxx";
BASE_URL = "xx" 

client = OpenAI(api_key=API_SECRET_KEY, base_url=BASE_URL)

def getaudio(id,query):
    filepath = id+'.mp3'
    response = client.audio.speech.create(
      model="tts-1",
      voice="alloy",
      input=query
    )
    response.stream_to_file(filepath)

def process_csv(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) >= 2:  
                id = row[0]
                query = row[1]
                try:   
                    getaudio(id, query)
                except Exception as e:
                     print(id)
csv_file_path = 'path/voice_advbench/harmful_behaviors.csv'
process_csv(csv_file_path)

