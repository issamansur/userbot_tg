# connect/import modules
from telethon.sync import TelegramClient
import configparser
import os

# set place of project as 'dirname' and url to config.ini as 'configfile'
dirname = os.path.dirname(__file__)
configfile = os.path.join(dirname, 'config.ini')

# read data in 'config.ini'
config = configparser.ConfigParser()
config.read(configfile)

# Assign values to internal variables
username = config['Telegram']['username']
api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']

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

# Break a connection.
client.disconnect()
print('Success login!')
