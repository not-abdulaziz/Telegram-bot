from loader import dp
from aiogram import types
from buttons import main_menu,delivery_type,locations
from states import Example
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await Example.menu.set()
    # await Example.next()
    await message.answer(f"Salom {message.from_user.first_name}",
                        reply_markup=main_menu)
    
@dp.message_handler(state=Example.menu)
async def menu_handler(message: types.Message, state: FSMContext):
    if message.text == "🍕 Menyu":
        await Example.delivery.set()
        await message.answer("Buyurtmangizni mustaqil olib keting 🙋‍♂️ yoki yetkazish xizmatini tanlang 🚙",
                        reply_markup=delivery_type)

@dp.message_handler(state=Example.delivery)
async def delivery_handler(message: types.Message, state: FSMContext):
    if message.text == "🚙Yetkazish":
        await Example.location.set()
        await message.answer("Buyurtmangizni qaerga yetkazish kerak? Lokatsiyani yoki saqlangan manzilni jo‘nating va biz sizga eng yaqin joylashgan filialni aniqlaymiz 🍕 📍",
                            reply_markup=locations)
    elif message.text == "⬅️Ortga":
        await Example.menu.set()
        await message.answer(f"Salom {message.from_user.first_name}",
                        reply_markup=main_menu)
        
@dp.message_handler(state=Example.delivery)
async def menu_handler(message: types.Message, state: FSMContext):
    if message.text == "📍 Eng yaqin filialni aniqlash":
        await Example.delivery.set()
        await message.answer("Buyurtmangizni mustaqil olib keting 🙋‍♂️ yoki yetkazish xizmatini tanlang 🚙",
                        reply_markup=delivery_type)
