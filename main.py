# connect/import modules
from telethon.sync import TelegramClient, events
import configparser
import os

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
chat = config['Telegram']['chat_name']

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
# The session file will be saved in the project folder.
client.start()

# Getting information about yourself
print()
me = client.get_me()
print("Info about user:")
print("ID:        ", me.id)
print("Username:  ", me.username)
print("First_name:", me.first_name)
print("Last_name: ", me.last_name)
print("Phone:     ", me.phone)
print()

# This method returns a list of Dialog.
client.get_dialogs()

# Output
for user in client.iter_participants(chat):
    print("{0:>10} | {1:20} | {2}".format(user.id, str(user.username), user.first_name))

# Break a connection.
client.disconnect()
