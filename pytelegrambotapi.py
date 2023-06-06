import asyncio
from telebot.async_telebot import AsyncTeleBot
from environs import Env


class SimpleAsyncTeleBot:
    """Класс-обертка для плоского вызова методов"""

    def __init__(self, token):
        self.bot = AsyncTeleBot(token)

    async def __aenter__(self):
        return self.bot

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.bot.close_session()
        if exc_val:
            return True


async def main(token, chat_id):
    async with SimpleAsyncTeleBot(token) as bot:
        await bot.send_message(chat_id=chat_id, text='test')


if __name__ == '__main__':
    env = Env()
    env.read_env()

    loop = asyncio.new_event_loop()
    loop.run_until_complete(
        main(
            token=env.str('TOKEN'), chat_id=env.str('CHAT_ID')
        )
    )
