#!/usr/bin/python
from twitter import *
import telepot
bot = telepot.Bot(#')
myId = '#'
config = {}
execfile("config.py", config)
twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
user = "@A1S0N_"
results = twitter.statuses.user_timeline(screen_name = user)
def main():
    f = open('tweets.tw','r+')
    content = f.read()
    for status in results:
        var = status["text"].encode("ascii", "ignore")
        if var in content:
            pass
        else:
            bot.sendMessage(myId, var)
            f.write(var)
    f.close()

main()
