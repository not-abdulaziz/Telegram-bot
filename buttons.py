from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🍕 Menyu")],
        [
            KeyboardButton("📖 Mening buyurtmalarim"),
            KeyboardButton("🍕 Filiallarimiz")
        ],
        [
            KeyboardButton("☎️ Qayta aloqa"),
            KeyboardButton("⚙️ Sozlamalar")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


delivery_type = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🚙Yetkazish"),
            KeyboardButton("🏃‍♂️Olib ketish")
        ],
        [
            KeyboardButton("⬅️Ortga")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

locations = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📍 Eng yaqin filialni aniqlash"),
        ],
        [
            KeyboardButton("🗺 Mening manzillarim")
        ],
        [
            KeyboardButton("⬅️Ortga")
        ]
    ]
)

locations1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(""),
        ],
       
        [
            KeyboardButton("⬅️Ortga")
        ]
    ]
)

