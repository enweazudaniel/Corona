# Telegram Corona UserBot 🤖
   
   The bot relays  messages from Corona bots to a channel

``` python
      from pyrogram import Client,Filters,Message
      import time
      import os

      id="##"
      hash="####"

      app =  Client("me_corona", api_hash=hash, api_id=id)
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
      app.send_message(target,trigger_message)
```
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

----
## Special thanks to


* [Mbonea Mjema](https://github.com/Mbonea-Mjema)


* [Daniel Ebuka](https://t.me/dandollar1)
