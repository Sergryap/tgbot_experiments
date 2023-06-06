import asyncio
from aiogram import Bot
from environs import Env


async def main(bot: Bot, chat_id):
    await bot.send_message(chat_id=chat_id, text='test')
    # await asyncio.gather(
    #     bot.send_message(chat_id=chat_id, text='test')
    # )
    await bot.session.close()


if __name__ == '__main__':
    env = Env()
    env.read_env()
    token = env.str('TOKEN')
    current_bot = Bot(token=token)
    # asyncio.run(main(bot=current_bot, chat_id=env.str('CHAT_ID')))
    loop = asyncio.new_event_loop()
    loop.run_until_complete(
        main(
            bot=current_bot, chat_id=env.str('CHAT_ID')
        )
    )
