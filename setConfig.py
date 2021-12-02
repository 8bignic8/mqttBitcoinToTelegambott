#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Version 02122021
import json
import os
import requests


# In[ ]:


def findID(token):
    if ':' in token: #checks if a valid Telegram token has been inputed
        method = 'getUpdates' #sets the telegram request status
        response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(token, method) #reqets the updates with the token
        ).json()
        chatID = (((response['result'][1])['message'])['chat'])['id'] #searches in the dict for the chat message token
        print('Your Chat ID is' + str(chatID)) #shows it to the user
        return chatID
    else:
        print('Not the right Token :/')


# In[ ]:


##Input part
print('You need to setup your Telegram bot and add it to a group with you!!, than send a message in the group to initialize the connection')
token = input('Set your BOT TOKEN e.g.: 213477740:ssf.......wfVg --> ') or 'ERR'
changeValue = input('Set the value, Bitcoin needs to change to get a Telegam message : (number) default 1000 --> ') or '1000'
mqTTBroker = input('Set your mqTTBroker adress e.g.: 192.168.0.42 or localhost --> ') or 'localhost'
mqTTSub = input('Set your mqTTSub for the Bitcoin value e.g.: /home/bitcoin/euro --> ') or '/home/bitcoin/euro'

####Setup config as dict
config = {'myuserid': findID(token),
        'token': token,
         'changeValue': changeValue,
         'mqTTSub':mqTTSub,
         'mqTTBroker': mqTTBroker}


# In[ ]:


##Writing JSON with established dict
try: 
    with open('config.json', 'w', encoding='utf-8') as f: #writing config.json in utf-8
        json.dump(config, f)
except:
    print('config file write error')

