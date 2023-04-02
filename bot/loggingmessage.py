import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def forward_messages_to_user(bot: Bot, update: Update, chat_id: int):
    message = update.message
    bot.send_message(chat_id=chat_id, text=message.text)

def configrun():
  updater = Updater(os.environ['TELEGRAM_BOT_TOKEN'])
  dp = updater.dispatcher
  chat_id = -961761939
  dp.add_handler(MessageHandler(Filters.all, forward_messages_to_user, pass_args=True, pass_job_queue=True, pass_chat_data=True))