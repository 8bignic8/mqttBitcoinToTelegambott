#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python

#You need telegram_send and paho.mqtt installed and also setup you Telegramm bot with the BotFather
#https://core.telegram.org/bots
#!pip3 install telegram_send
#pip3 install paho-mqtt

import paho.mqtt.client as mqtt
import time
import json
import telegram_send
import requests
#https://janakiev.com/blog/python-background/

#automatic reading of the config JSON
json_config_path = "config.json"


# In[11]:


### https://stackoverflow.com/questions/16573332/jsondecodeerror-expecting-value-line-1-column-1-char-0
with open(json_config_path, 'r') as j:
     config = json.loads(j.read())


# In[12]:


def sendTGMessage(Message, config):
    #https://stackoverflow.com/questions/41174831/telegram-bot-chat-not-found
    method = 'sendMessage'
    Message = str(Message) + ' €'
    response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(config['token'], method),
        data={'chat_id': config['myuserid'], 'text': str(Message)}
    ).json()
    #print(response)


# In[14]:


#Telegram Part: 

#https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(config['mqTTSub']) # mit # wird alles ab da subscribed

    
    
old = 0
def change(new,changeAM):
    global old
    if (not(old == new)and(abs(new - old)>changeAM)):
        old = new
        return True

    

def on_message(client, userdata, msg):
    
    mqttData = (str(json.loads(msg.payload)).split('.')[0])
    
    if change(int(mqttData),int(config['changeValue'])):
        sendTGMessage(mqttData, config) 

        
###Main loop
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(config['mqTTBroker'], 1883, 60)

client.loop_forever()


# In[ ]:




