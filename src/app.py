from pyrogram import Client,Filters,Message
import time
import os

id="870972"
hash="ce2efaca02dfcd110941be6025e9ac0d"

app =  Client("me_Corona", api_hash=hash, api_id=id)
target = os.getenv('Bot_name')
channel_destination=os.getenv('Channel_name')
trigger_messages = [i for i in os.getenv('trigger_messages').split(",")] 
time_delay = int(os.getenv('time_delay'))

@app.on_message(filters=Filters.bot)
def catch_every(client:Client,message:Message):
  if message.chat.username == target:
    app.send_message(channel_destination,message.text)

app.start()

seconds = time_delay
while True:
  time.sleep(seconds)
  for trigger in trigger_messages:
    app.send_message(target,trigger)
    time.sleep(2)
