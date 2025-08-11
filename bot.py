import os
import telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])  # 從環境變量讀取 Token

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "我喺 GitHub 度運行緊！🚀")

bot.polling()  # 長期運行
