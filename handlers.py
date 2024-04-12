# from aiogram import F, Router, types
# from aiogram.filters import Command, Text
# from aiogram.fsm.context import FSMContext
#
# router = Router()
#
# @router.message(Command("start"))
# async def main(message: types.Message):
#     await message.reply('Привет!')
#
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# @router.message(Command("add_to_list"))
# async def cmd_add_to_list(message: types.Message):
#     await message.answer("Введите число:")
#     @router.message()
#     async def add_to_list(message: types.Message):
#         print(message.text)
#         try:
#             sas = int(message.text)
#             print(sas)
#         except ValueError:
#             await message.answer("Некорректный ввод. Пожалуйста, введите число.")
#             return
#
#         mylist.append(sas)
#         await message.answer(f"Ваш список: {mylist}")
#
# @router.message(Command("show_list"))
# async def cmd_show_list(message: types.Message):
#     await message.answer(f"Ваш список: {mylist}")




from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery


class Statemenu(StatesGroup):
    add_to_list = State()
    show_list = State()

mylist = []
router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await message.answer('Hello')
    await state.set_state(Statemenu.add_to_list)

@router.message(Command("add_to_list"))
async def add_to_list(message: Message, state: FSMContext):
    print(message.text)
    await message.answer('введите число:')
    sas = int(message.text)
    print(sas)
    try:
        mylist.append(sas)
    except ValueError:
        await message.answer("Некорректный ввод. Пожалуйста, введите число.")
    finally:
        await message.answer(f"Ваш список: {mylist}")

@router.message(F.text =='/show_list')
async def show_list(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Ваш списокc: {mylist}")
