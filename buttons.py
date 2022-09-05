from telegram import InlineKeyboardButton, ReplyKeyboardMarkup
from telegram import Update, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters

from backend import DBHelper

db = DBHelper('base')

class buttons:
    db.__init__()
    # def __init__(self):
    #     self.