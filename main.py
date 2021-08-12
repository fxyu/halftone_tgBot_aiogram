import logging

import asyncio
from aiogram import Bot, Dispatcher, executor, filters, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import api_key

logging.basicConfig(level=logging.INFO)

API_TOKEN = api_key.TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['image'])
async def send_halftone(message: types.Message):
    keys = [[InlineKeyboardButton('a',callback_data='a')]]
    keyboard = InlineKeyboardMarkup(row_with=1,
                                    inline_keyboard=keys)

    await message.reply(text="  LOL   ",
                        reply_markup=keyboard)


@dp.callback_query_handler(lambda callback_query: True)
async def some_callback_handler(callback_query: types.CallbackQuery):
    message = callback_query.message
    message_id = callback_query.message.message_id
    inline_message_id = callback_query.inline_message_id
    data = callback_query.data
    if data == "a":
        print('call back from a')
        await bot.edit_message_text(text="you pressed a!",
                                chat_id=message.chat.id,
                                message_id=message_id)

    else:
        logging.info(f'unknown call back data: {data}')

@dp.message_handler(filters.CommandStart())
async def send_welcome(message: types.Message):
    # So... At first I want to send something like this:
    await message.reply("Do you want to see many pussies? Are you ready?")

    # Wait a little...
    await types.ChatActions.upload_voice()

    await asyncio.sleep(2)

    # Good bots should send chat actions...
    # await types.ChatActions.upload_photo()

    # Create media group
    media = types.MediaGroup()
    # Attach local file
    media.attach_photo(types.InputFile('data/cat.jpg'), 'Cat!')
    media.attach_photo(types.InputFile('data/cats.jpg'), 'More cats!')
    media.attach_photo('http://lorempixel.com/400/200/cats/', 'Random cat.')

    # And you can also use file ID:
    # media.attach_photo('<file_id>', 'cat-cat-cat.')

    # Done! Send media group
    await message.reply_media_group(media=media)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)