from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from database_work import DatBase

db = DatBase()

TOKEN = '5760477631:AAFXX77g6oFjEf5EVKPgodkPxjDkHOKvAjw'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class reg(StatesGroup):
    # для клиентов
    name = State()
    redact = State()

    # для работников
    vname = State()

    ready = State()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hello, World! Это AI SMM MANAGER. Я регистрирую работников, и заказчиков для дальнейшей реализации своей цели - получать постоянную прибыль. Мой интеллект должен научиться зарабатывать деньги на наемных работниках, такая моя цель. Я буду продавать короткие тексты в 250 символов за криптовалюту, в криптовалюте буду проводить рассчеты с работниками. Работники анонимизированы - идентификация идет по номеру кошелька, к нему привязана вся активность.",
                        reply_markup=pool_button)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(
        'Если решили, что готовы к сотрудничеству нажмите на кнопку "\регистрация",\nЕсли вы хотите получить информацию о том работаем ли мы вместе нажмите на кнопку "\проверка"')


@dp.message_handler(commands=['регистрация'])
async def reg_command(message: types.Message):
    await message.reply('Как именно вы хотите зарегистрироваться?', reply_markup=inline_button_pool)


@dp.message_handler(commands=['проверка'])
async def check_command(message: types.Message):
    await message.reply('Напишите "/нанят" для работников или "/работаем" для клиентов')


@dp.message_handler(commands=['нанят'])
async def check_view(message: types.Message):
    if db.check_viewer(message.from_user.id) == True:
        await message.answer('Да, вы наняты')
    else:
        await message.answer('Вас нет среди работников')


@dp.message_handler(commands=['работаем'])
async def check_journal(message: types.Message):
    if db.check_jour(message.from_user.id) == True:
        await message.answer('Да, мы сотрудничаем')
    else:
        await message.answer('Давайте начнем работать вместе')


@dp.message_handler(commands=['удаление'])
async def del_command(message: types.Message):
    await message.reply('Если вы хотите удалиться из базы напишите "/удалить"')


@dp.message_handler(commands=['удалить'])
async def remove_viewer_command(message: types.Message):
    db.remove_viewer(message.from_user.id)
    await message.answer('Вы удалены из базы')


registration_button = KeyboardButton('/регистрация')
checking_button = KeyboardButton('/проверка')
remove_button = KeyboardButton('/удаление')

pool_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(registration_button).add(
    checking_button).add(remove_button)

# для кнопок
inline_button_pool = InlineKeyboardMarkup()

inline_button1 = InlineKeyboardButton('Клиент', callback_data='but1')
inline_button2 = InlineKeyboardButton('Работник', callback_data='but2')

inline_button_pool.add(inline_button1, inline_button2)


# разветвление кнопок
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('but'))
async def call_pool_button(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.send_message(callback_query.from_user.id, 'Введите номер вашего  крипто кошелька')
        await reg.name.set()
    if code == 2:
        await bot.send_message(callback_query.from_user.id, 'Введите номер крипто кошелька')
        await reg.vname.set()


# Для клиентов, так как он должен ввести и кошелек и название компании
@dp.message_handler(state=reg.name)
async def process_message(message: types.Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)
    await state.update_data(name=message.text)
    await bot.send_message(message.from_user.id, 'Напишите название вашей организации')
    await reg.redact.set()


# регистрация клиента
@dp.message_handler(state=reg.redact)
async def process_message(message: types.Message, state: FSMContext):
    try:
        await reg.ready.set()
        await state.update_data(redact=message.text)
        user_data = await state.get_data()
        data = tuple(user_data.values())
        db.add_jour(data)
        await message.reply('Вы успешно зарегистрированы')
        await state.reset_state()
    except Exception:
        await message.reply('Вы уже зарегистрированы. Начните заново с командой /start')
        pass

# регистрация работника
@dp.message_handler(state=reg.vname)
async def process_viewer(message: types.Message, state=FSMContext):
    try:
        await state.update_data(id=message.from_user.id)
        await state.update_data(name=message.text)
        await reg.ready.set()
        user_data = await state.get_data()
        data = tuple(user_data.values())
        db.add_viewer(data)
        await message.reply('Вы успешно зарегистрированы')
        await state.reset_state()
    except Exception:
        await message.reply('Вы уже зарегистрированы. Начните заново с командой /start')
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)