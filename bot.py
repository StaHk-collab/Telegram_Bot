from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='1596598822:AAEzm_NvwZkg-gnRGImfsFWCBm3UvM66YdM', use_context=True) 
dispatcher = updater.dispatcher
import requests
import json

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello User \nYou can type /help to know the instructions')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Type /1 for getting notifications on COVID 19 \nType /2 for asking any query')

def one(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Here is the latest COVID-19 news :')

    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200):   # Everything went okay, we have the data
        data = response.json()
        print(data['Global'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=data['Global'])
    else:   # something went wrong
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")


def two(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='What is your query ?')

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

one_handler = CommandHandler('1', one)
dispatcher.add_handler(one_handler)

two_handler = CommandHandler('2', two)
dispatcher.add_handler(two_handler)

updater.start_polling()