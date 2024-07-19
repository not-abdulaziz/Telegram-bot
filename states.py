from aiogram.dispatcher.filters.state import State,StatesGroup

class Example(StatesGroup):
    menu = State()
    delivery = State()
    location = State()
    location1 = State()