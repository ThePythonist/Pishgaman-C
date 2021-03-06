#!/usr/bin/python3.9
import telepot
import time
import urllib3

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

bot = telepot.Bot('Token')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    message = msg['text']

    if content_type == 'text':
        if message == "/start" :
            bot.sendMessage(chat_id, "Hello! Welcome to my bot")
        else :
            bot.sendMessage(chat_id, "You said '{}'".format(message))


bot.message_loop(handle)

print ('Bot is online ...')

# Keep the program running.
while True:
    time.sleep(10)
