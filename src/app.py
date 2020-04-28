from pyrogram import Client,Filters,Message
import time
import os

id="870972"
hash="ce2efaca02dfcd110941be6025e9ac0d"

app =  Client("my_netflix", api_hash=hash, api_id=id)
target = os.getenv('Bot_name')
channel_destination=os.getenv('Channel_name')
trigger_message =os.getenv('trigger_message')
time_delay = int(os.getenv('time_delay'))

@app.on_message()
def catch_every(client:Client,message:Message):
  app.send_message(channel_destination,message.text)

app.start()

seconds = time_delay
while True:
  time.sleep(seconds)
  app.send_message(target,'Tanzania')
