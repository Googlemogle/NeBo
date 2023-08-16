from aiogram import Bot, Dispatcher, types, utils
from config import token


bot = Bot(token=token, parse_mode='HTML')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(f'Здарова, {utils.markdown.hbold(message.from_user.full_name)}!')


if __name__ == "__main__":
    utils.executor.start_polling(dp)