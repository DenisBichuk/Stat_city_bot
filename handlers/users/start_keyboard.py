from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

analitics = KeyboardButton('Выбрать сервис аналитики📊')
about = KeyboardButton('О складчине💭')
chat_and_reviews = KeyboardButton('Чат и отзывы👥')
top = KeyboardButton('В Топе на маркетплейс 8.0🔥')
total_domination = KeyboardButton('Тотальное доминирование на МП🦾🔝')
need_help = KeyboardButton('Обратится в поддержку✍')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(analitics, about, chat_and_reviews, top, total_domination, need_help)


professional = KeyboardButton('MPstats(Профессиональный)💹')
premium = KeyboardButton('Moneyplace(Premium)📈')
composite = KeyboardButton('MarketGuru(Комбинированый)📉')
main_menu = KeyboardButton('Главное меню🗂')
analitic_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(professional, premium, composite, main_menu)

choise = KeyboardButton('Выбрать сервис💹')
main_menu = KeyboardButton('Главное меню🗂')
about_sklad_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(choise, main_menu)

chat = KeyboardButton('Чат👥')
reviews = KeyboardButton('Отзывы💬')
main_menu = KeyboardButton('Главное меню🗂')
chat_and_reviews_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(chat, reviews, main_menu)

top_at = KeyboardButton('Оплатить и получить доступ✅')
main_menu = KeyboardButton('Главное меню🗂')
top_at_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(top_at, main_menu)

total_dom = KeyboardButton('Оплатить и получить доступ✅')
main_menu = KeyboardButton('Главное меню🗂')
total_dom_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(total_dom, main_menu)

contact_tp = KeyboardButton('Написать в тех. подержку✍')
chat_tp = KeyboardButton('Чат👥')
main_menu = KeyboardButton('Главное меню🗂')
tp_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(contact_tp, chat_tp, main_menu)

pay_and_get = KeyboardButton('Оплатить и получить доступ✅')
about_sklad = KeyboardButton('О складчине💭')
go_to_tp = KeyboardButton('Обратится в поддержку✍')
main_menu = KeyboardButton('Главное меню🗂')
tarifs_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(pay_and_get, about_sklad, go_to_tp, main_menu)

any_card = KeyboardButton('Любой картой✅')
tinkoff_sbor = KeyboardButton('Тинькофф Сбор☑')
main_menu = KeyboardButton('Главное меню🗂')
payments_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(any_card, tinkoff_sbor, main_menu)


pay_2800_any = KeyboardButton('Оплатить 2800₽')
main_menu = KeyboardButton('Главное меню🗂')
any_card_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(pay_2800_any, main_menu)

pay_2800_sbor = KeyboardButton('Oплатить 2800₽')
main_menu = KeyboardButton('Главное меню🗂')
tinkoff_sbor_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(pay_2800_sbor, main_menu)