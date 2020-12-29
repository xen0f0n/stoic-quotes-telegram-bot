from telegram import Bot
import schedule

from config import bot_token_id, channel_chat_id
from utils import get_quote


def post_quote():
    quote, author = get_quote()
    message = f'{quote}\n\n{author}'

    bot = Bot(token=bot_token_id)
    bot.sendMessage(chat_id=channel_chat_id, text=message)


if __name__ == '__main__':

    schedule.every(8).hours.do(post_quote).tag('stoic-quote')

    while 1:
        schedule.run_pending()
