from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

analitics = KeyboardButton('Выбрать сервис аналитики📊')
about = KeyboardButton('О складчине💭')
chat_and_reviews = KeyboardButton('Чат и отзывы👥')
top = KeyboardButton('В Топе на маркетплейс 8.0🔥')
total_domination = KeyboardButton('Тотальное доминирование на МП🦾🔝')
ozon = KeyboardButton('Лео Шевченко «Выход в Топ на OZON»📉')
need_help = KeyboardButton('Обратится в поддержку✍')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(analitics, about, chat_and_reviews, top, total_domination, ozon, need_help)


professional = KeyboardButton('MPstats(Корпоративный)💹')
premium = KeyboardButton('Moneyplace(Premium)📈')
composite = KeyboardButton('MarketGuru(Профессиональный)📉')
main_menu = KeyboardButton('Главное меню🗂')
analitic_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(professional, premium, composite, main_menu)

choise = KeyboardButton('Выбрать сервис аналитики📊')
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

pay = KeyboardButton('Оплатить✅')
main_menu = KeyboardButton('Главное меню🗂')
payments_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(pay, main_menu)

main_menu = KeyboardButton('Главное меню🗂')
main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(main_menu)

trial = KeyboardButton('Пробный период на две недели(1600 руб.)')
extension = KeyboardButton('Продление тарифа(2300 руб.)')
full_month = KeyboardButton('Полный тариф на месяц(2500 руб.)')
main_menu = KeyboardButton('Главное меню🗂')
prof_choose_option_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(trial, extension, full_month, main_menu)

paid = KeyboardButton('Оплачено✅')
main_menu = KeyboardButton('Главное меню🗂')
paid_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(paid, main_menu)