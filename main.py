from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Updater, CommandHandler, ConversationHandler, Filters
from backend import DBHelper
data = DBHelper()

STATE_1 = 1
STATE_2 = 2


def main(update:Update, context:CallbackContext):
    update.message.reply_html("Salom")

def start(update:Update, context:CallbackContext):
    update.message.reply_html(f"Salom <b>{update.effective_user.first_name }</b> ism, familiyangizni to'liq kiriting")
    return STATE_1

def state_1(update:Update, context:CallbackContext):
    text = update.message.text
    context.chat_data.update({"full_name": text})
    data.insert_bd(id = update.effective_user.id, name=text)
    update.message.reply_html("✅ Yaxshi. Yoshingizni kiriting")
    return STATE_2

def state_2(update:Update, context:CallbackContext):
    text = update.message.text
    a= data.select_db()
    w = ''
    for i in a:
        w= w + f'{i[0]} = > {i[1]}' + "\n"
    
    update.message.reply_html(f"{w}")

    


updater = Updater("5458398347:AAH57j41XT25BIE5gVt-HUp-LJSOWZtCd7o", use_context=True)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        STATE_1:[
            MessageHandler(Filters.all, state_1)
        ],
        STATE_2:[   
            MessageHandler(Filters.all, state_2)
        ]
    },
    fallbacks=[CommandHandler("start", start)]
)

updater.dispatcher.add_handler(CommandHandler("jobir", main))

updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()




