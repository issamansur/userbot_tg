# connect/import modules
import configparser
import asyncio
import os

from telethon.sync import TelegramClient, events

# set place of project as 'dirname' and
# url to config.ini as 'configfile'
dirname = os.path.dirname(__file__)
configfile = os.path.join(dirname, 'config.ini')

# read data in 'config.ini' (format: utf-8)
config = configparser.ConfigParser()
config.read(configfile, encoding='utf-8')

# Assign values to internal variables
username = config['Telegram']['username']
api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']

# Take name/title of chat
chat_name = config['Telegram']['chat_name']

# create object 'client' (our app) with variables WITHOUT PROXY
client = TelegramClient(username, api_id, api_hash)

# for proxy
'''
from telethon import connection

proxy = (proxy_server, proxy_port, proxy_key)

client = TelegramClient(username, api_id, api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=proxy)
'''

# Try to auth to account with our app
# The session file will be saved in the project folder
client.start()
print()

# Getting information about yourself (as necessary)
me = client.get_me()
print("[x] INFO ABOUT CURRENT USER")
print("[1] Id:        ", me.id)
print("[2] Username:  ", me.username)
print("[3] First name:", me.first_name)
print("[4] Last name: ", me.last_name)
print("[5] Phone:     ", me.phone)
print()

# This method returns a list of Dialog (get_dialogs() IMPORTANT!)
client.get_dialogs()


# Handler for event:
# new message '_tag' -> def tag
@client.on(events.NewMessage(chats=chat_name, pattern='_tag'))
async def tag(event):
    # This method returns a list of participants
    await client.get_participants(chat_name)

    counter = 0
    async for user in client.iter_participants(chat_name):
        # Send message: [visible text](user's link)
        # Adding * at the beginning - for empty name
        mes = str('[*' + str(user.first_name) + '](tg://user?id=' + str(user.id) + ')')
        await client.send_message(chat_name, mes)

        # Write in console (log)
        counter += 1
        print("{0:>4} | {1:>10} | {2:20} | {3}".format(counter, user.id, str(user.username), user.first_name))


# The above code is executed while the client is active (connected)
client.run_until_disconnected()
