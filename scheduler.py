from telegram import Bot
import schedule
import os

from utils import get_quote


def post_quote():
    bot_token_id = os.environ.get('BOT_TOKEN_ID')
    channel_chat_id = os.environ.get('CHANNEL_CHAT_ID')

    quote, author = get_quote()
    message = f'{quote}\n\n{author}'

    bot = Bot(token=bot_token_id)
    bot.sendMessage(chat_id=channel_chat_id, text=message)


if __name__ == '__main__':

    schedule.every(8).hours.do(post_quote).tag('stoic-quote')

    while 1:
        schedule.run_pending()
