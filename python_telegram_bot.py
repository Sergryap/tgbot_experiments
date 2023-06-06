import asyncio
from telegram._bot import Bot
from environs import Env


async def main(bot, chat_id):
    await bot.send_message(chat_id=chat_id, text='test')


if __name__ == '__main__':
    env = Env()
    env.read_env()
    token = env.str('TOKEN')
    current_bot = Bot(token=token)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(
        main(
            bot=current_bot, chat_id=env.str('CHAT_ID')
        )
    )
