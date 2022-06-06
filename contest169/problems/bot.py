import logging
import math

from aiogram import Bot, Dispatcher, executor, types

tk = input()

API_TOKEN = tk
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['factorial'])
async def send_welcome(message: types.Message):
    nums = message.text.replace('/factorial', '').strip().split(' ')
    if len(nums) != 1:
        await message.reply('Error')
    else:
        try:
            n = int(nums[0])
            if n < 0:
                await message.reply('Error')
            else:
                await message.reply(str(math.factorial(n)))
        except:
            await message.reply('Error')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
