import zmagi
import config
import telebot


bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def zmagi_all_messages(message):
    inpt = message.text.lower()
    words = inpt.split()

    output = ""
    for word in words:
        output += zmagi.zmagi(word) + " "

    message.text = output.replace("тш", "ч")
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)