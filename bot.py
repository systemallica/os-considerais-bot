import json
import logging
import os
from pathlib import Path
from random import randrange

from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler

# Enable logging
logger = logging.getLogger()
if logger.handlers:
    for h in logger.handlers:
        logger.removeHandler(h)
logging.basicConfig(level=logging.INFO)

# Define responses
OK_RESPONSE = {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps('ok')
}
ERROR_RESPONSE = {
    'statusCode': 400,
    'body': json.dumps('Oops, something went wrong!')
}

# Load words file
path = Path(__file__).parent / "raw/filtered_words.txt"
words_file = open(path, 'r')
words = words_file.readlines()

path = Path(__file__).parent / "raw/singular_words.txt"
singular_words_file = open(path, 'r')
singular_words = singular_words_file.readlines()


def configure_telegram():
    """
    Configures the bot with a Telegram Token.
    Returns a bot instance.
    """

    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    if not TELEGRAM_TOKEN:
        logger.error('The TELEGRAM_TOKEN must be set')
        raise NotImplementedError

    return Bot(TELEGRAM_TOKEN)


def set_up_dispatcher(dispatcher: Dispatcher) -> None:
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("consideracion", consideracion))
    dispatcher.add_handler(CommandHandler("contad_algo", contad_algo))


def start(update: Update, context):
    text = "Hello!"
    update.message.reply_text(text)
    logger.info('Message sent')


def consideracion(update: Update, context):
    word = words[randrange(len(words))]
    text = "¿Os consideráis " + word.strip() + "?"
    update.message.reply_text(text, quote=False)
    logger.info('Message sent')


def contad_algo(update: Update, context):
    word = singular_words[randrange(len(singular_words))]
    text = "Contad algo " + word.strip() + "."
    update.message.reply_text(text, quote=False)
    logger.info('Message sent')


# Initialize bot and dispatcher
bot = configure_telegram()
dp = Dispatcher(bot, None, use_context=True)
set_up_dispatcher(dp)


def handler(event, context):
    """
    Processes the received update and sends it to the dispatcher.
    """
    logger.info(f'Event: {event}')

    try:
        dp.process_update(Update.de_json(json.loads(event.get("body")), bot))
    except Exception as e:
        logger.error(e)
        return ERROR_RESPONSE

    return OK_RESPONSE


