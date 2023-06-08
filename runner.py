import string
from nltk.corpus import stopwords
from nltk import PorterStemmer as Stemmer
import nltk

import os
import discord
from discord.ext import commands
import asyncio


def process2(text):
    # lowercase it
    text = text.lower()
    # remove punctuation
    text = ''.join([t for t in text if t not in string.punctuation])
    # remove stopwords
    text = [t for t in text.split() if t not in stopwords.words('english')]
    # stemming
    st = Stemmer()
    text = [st.stem(t) for t in text]
    # return token list
    return text


import pickle
testclass = pickle.load(open('goodspam.sav', 'rb'))


def check2(s):
    out = testclass.predict([s])[0]
    return 'The message is unlikely to be spam' if int(out) == 0 else 'The message is likely to be spam'


bot = commands.Bot(command_prefix='$', description="This is a spam checker bot")


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command(name='spam', description='Checks spam')
async def spam(ctx):
    reply = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    await ctx.send(check2(str(reply.content)))

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)

while True:
    input()