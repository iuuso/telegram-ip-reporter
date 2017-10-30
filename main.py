import urllib.request
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
					level=logging.INFO)

try:
	from telegram.ext import Updater
	from telegram.ext import CommandHandler
except ImportError:
	print("Err: Requirements are missing. Install them with pip:")
	print("'pip3 install -r requirements.txt'")

def get_public_ip():
	return(urllib.request.urlopen('http://ident.me').read().decode('utf8'))

def start(bot, update):	
	message_text = "My public address is " + get_public_ip()
	bot.send_message(chat_id=update.message.chat_id, text=message_text)

def main():
	updater = Updater(token="392089838:AAGsmWV3PVqFk6QTuzvjGLgS2vUrvaaWntI")
	dispatcher = updater.dispatcher

	start_handler = CommandHandler('start', start)
	dispatcher.add_handler(start_handler)
	updater.start_polling()
	print("All done, exiting")
	return

if __name__ == "__main__": main()
