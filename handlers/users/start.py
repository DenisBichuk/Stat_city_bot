from aiogram import types
from aiogram.dispatcher import FSMContext
from data import config
from loader import dp, bot
from . import start_keyboard as kb
from .states import FSMProf, FSMPrem, FSMComposite, FSMTop, FSMTotalDom


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(
        f"Привет, {message.from_user.full_name} Рады вас видеть😊\n\nС помощью этого бота вы сможете получить доступ к сервису аналитики для маркетплейсов, который подходит именно вам.",
        reply_markup=kb.start_kb)


@dp.message_handler(lambda message: message.text == "Выбрать сервис аналитики📊", state='*')
async def tarifs(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите интересующий вас сервис из доступных на данный момент:', reply_markup=kb.analitic_kb)


@dp.message_handler(lambda message: message.text == "О складчине💭", state='*')
async def about(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Что такое «складчина»?\n\n'
                         "Складчина - совместная покупка доступа к тому или иному онлайн продукты (в нашем случае). Таким образом каждый человек может пользоваться полноценным функционалом сервисов за доступные средства.\n\n"
                         "Например, 10 человек хотят купить MPstats за 28.000 рублей, то каждому из них нужно скинуться примерно по 2800 рублей.\n\n"
                         "🔘 Есть ли график пользования или очередь ? - графика и очередей НЕТ, заходите и пользуетесь полным функционалом, когда вам удобно.\n\n"
                         "🔘 Могу ли я подвязать свой личный кабинет WB через API в аккаунт мпстат ? - Да, вы можете это сделать.\n\n"
                         "🔘 Через какой браузер предоставляется доступ в аккаунт - Любой, который удобен вам.\n\n"
                         "🔘 Могу ли я купить доступ и использовать его с друзьями ? - Нет, один доступ в одни руки.\n\n"
                         "🔘 Могу ли я зайти с MacBook? - Да, вы сможете пользоваться сервисом, под любыми операционными системами.\n\n"
                         "🔘 Как мне понять, что вы меня не обманите? - По вашему запросу мы предоставим вам видео ОПЛАЧЕННОГО ТАРИФА ПРОФЕССИОНАЛЬНЫЙ с датой и временем \n\n"
                         "🔘 Какая механика захода в сервис? - Вход по ссылке через любой браузер",
                         reply_markup=kb.about_sklad_kb)


@dp.message_handler(lambda message: message.text == "Чат и отзывы👥", state='*')
async def about(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Для перехода в нужный раздел нажмите соответствующую кнопку:',
                         reply_markup=kb.chat_and_reviews_kb)


@dp.message_handler(content_types=['photo'], state='*')
async def scan_message(msg: types.Message):
    document_id = msg.photo[0].file_id
    file_info = await bot.get_file(document_id)
    print(f'file_id: {file_info.file_id}')
    print(f'file_path: {file_info.file_path}')
    print(f'file_size: {file_info.file_size}')
    print(f'file_unique_id: {file_info.file_unique_id}')


@dp.message_handler(lambda message: message.text == "В Топе на маркетплейс 8.0🔥", state='*')
async def top(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.TOP_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer("Дорогие участники!\n\n"
                         "Курс Лео Шевченко 8.0 куплен.✅\n\n"
                         "Старт: 25.02.2022\n\n"
                         "Длительность: 30 дней\n\n"
                         "Тариф: ULTIMATE 🔥\n\n\n"
                         "9 основных модулей:\n\n"
                         "МОДУЛЬ 0✅ - ПРИНИМАЕМ ПРАВИЛА ИГРЫ И СМОТРИМ В БУДУЩЕЕ\n\n"
                         "МОДУЛЬ 1✅ - КАК ПОПАСТЬ В ТОП\n\n"
                         "МОДУЛЬ 2✅ - СОЗДАЕМ ТОПОВЫЙ КОНТЕНТ"
                         "МОДУЛЬ 3✅ - ВЫВОДИМ ТОВАРЫ В ТОП\n\n"
                         "МОДУЛЬ 4✅ - ПРОДВИЖЕНИЕ ТОВАРА\n\n"
                         "МОДУЛЬ 5✅ - РЕПУТАЦИЯ БРЕНДА КАК СПОСОБ ПРОДВИЖЕНИЯ\n\n"
                         "МОДУЛЬ 6✅ - ДОПОЛНИТЕЛЬНЫЕ ИНСТРУМЕНТЫ ДЛЯ ПОВЫШЕНИЯ ПРИБЫЛИ\n\n"
                         "МОДУЛЬ 7✅ - ЗАКУПАЙ КАК ПРОФИ\n\n"
                         "МОДУЛЬ 8✅ - OZON ТОЖЕ КАЧНЕМ\n\n"
                         "МОДУЛЬ 9✅ - СИСТЕМАТИЗАЦИЯ БИЗНЕСА И УПРАВЛЕНИЕ КОМАНДОЙ\n\n"
                         "+ Созвоны по ZOOM\n\n"
                         "Стоимость курса - 3500₽", reply_markup=kb.top_at_kb)
    await FSMTop.top_pay_and_get.set()


@dp.message_handler(state=FSMTop.top_pay_and_get)
async def pay_choise(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.PAYMENTS_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите способ оплаты:', reply_markup=kb.payments_kb)
    await FSMTop.top_pay_choise.set()


@dp.message_handler(state=FSMTop.top_pay_choise)
async def any_or_sbor(message: types.Message):
    prof_choise = message.text
    if prof_choise == 'Любой картой✅':
        await message.reply('Вы производите оплату курса Лео Шевченко 8.0')
        await message.reply('<a href="https://clicks.su/mVejzQ">Оплатить 3500₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    elif prof_choise == 'Тинькофф Сбор☑':
        await message.reply('Вы производите оплату курса Лео Шевченко 8.0"\n\n'
                            '🚫Обязательно указать комментарий: на путешествие, на отдых\n\n'
                            '❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
                            'По всем вопросам: @AndreasBel_admin')
        await message.reply('<a href="https://clicks.su/yRjNAy">Оплатить 3500₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    await bot.send_message(chat_id=message.chat.id, text='После осуществления перевода введите слово: Оплачено 👇')
    await FSMTop.top_paid.set()


@dp.message_handler(lambda message: message.text == "Оплачено", state=FSMTop.top_paid)
async def top(message: types.Message, state: FSMContext):
    admin_chat_id = config.ADMIN_ID
    date_and_time = message.date
    await message.answer('Оплата успешно произведена ✅\n\n'
                         'Ожидайте сообщения от администратора.')
    await bot.send_message(chat_id=admin_chat_id, text=f'Stat_city_bot, [{date_and_time}]\n'
                                                       f'{message.from_user.id}\n'
                                                       f'Логин: {message.from_user.username}\n'
                                                       f'Имя: {message.from_user.first_name}\n'
                                                       f'Оплатил(а) Лео Шевченко 8.0✅')
    await state.finish()


@dp.message_handler(lambda message: message.text == "Тотальное доминирование на МП🦾🔝", state='*')
async def top(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.TOTAL_DOM_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer("Дорогие участники!\n\n"
                         "Вы можете приобрести:\n"
                         'Курс "Тотальное доминирование на маркетплейсах"\n\n'
                         "Содержание:\n\n"
                         "МОДУЛЬ 0✅ - Подготовка к курсу\n\n"
                         "МОДУЛЬ 1✅ - Как выбрать товар который будет продаваться\n\n"
                         "МОДУЛЬ 2✅ - Инвестиции и старт бизнеса\n\n"
                         "МОДУЛЬ 3✅ - Оформление и подготовка к первой поставке на маркетплейсе\n\n"
                         "МОДУЛЬ 4✅ - Дизайн и оформление карточки\n\n"
                         "МОДУЛЬ 5✅ - Продвижение товара\n\n"
                         "МОДУЛЬ 6✅ - Аналитика\n\n"
                         "МОДУЛЬ 7✅ - Команда\n\n"
                         "МОДУЛЬ 8✅ - Автоматизация бизнеса\n\n"
                         "МОДУЛЬ 9✅ - Построение бренда\n\n"
                         "МОДУЛЬ 10✅ - Продажа бизнеса\n\n\n"
                         "🔸общие групповые созвоны\n"
                         "🔸сео оптимизация от Павла Шевченко\n"
                         "🔸итоговое мероприятие, контакты", reply_markup=kb.total_dom_kb)
    await FSMTotalDom.total_dom_pay_and_get.set()


@dp.message_handler(state=FSMTotalDom.total_dom_pay_and_get)
async def pay_choise(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.PAYMENTS_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите способ оплаты:', reply_markup=kb.payments_kb)
    await FSMTotalDom.total_dom_pay_choise.set()


@dp.message_handler(state=FSMTotalDom.total_dom_pay_choise)
async def any_or_sbor(message: types.Message):
    prof_choise = message.text
    if prof_choise == 'Любой картой✅':
        await message.reply('Вы производите оплату курса "Тотальное доминирование на маркетплейсах".')
        await message.reply('<a href="https://clicks.su/yoJ7R0">Оплатить 4000₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    elif prof_choise == 'Тинькофф Сбор☑':
        await message.reply('Вы производите оплату курса "Тотальное доминирование на маркетплейсах".\n\n'
                            '🚫Обязательно указать комментарий: на путешествие, на отдых\n\n'
                            '❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
                            'По всем вопросам: @AndreasBel_admin')
        await message.reply('<a href="https://clicks.su/yM5vEy">Оплатить 4000₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    await bot.send_message(chat_id=message.chat.id, text='После осуществления перевода введите слово: Оплачено 👇')
    await FSMTotalDom.total_dom_paid.set()


@dp.message_handler(lambda message: message.text == "Оплачено", state=FSMTotalDom.total_dom_paid)
async def top(message: types.Message, state: FSMContext):
    admin_chat_id = config.ADMIN_ID
    date_and_time = message.date
    await message.answer('Оплата успешно произведена ✅\n\n'
                         'Ожидайте сообщения от администратора.')
    await bot.send_message(chat_id=admin_chat_id, text=f'Stat_city_bot, [{date_and_time}]\n'
                                                       f'{message.from_user.id}\n'
                                                       f'Логин: {message.from_user.username}\n'
                                                       f'Имя: {message.from_user.first_name}\n'
                                                       f'Оплатил(а) "Тотальное доминирование на маркетплейсах"✅')
    await state.finish()


@dp.message_handler(lambda message: message.text == "Обратится в поддержку✍", state='*')
async def top(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Вы можете написать администратору либо обратиться с вопросом в чат складчины:',
                         reply_markup=kb.tp_kb)


@dp.message_handler(lambda message: message.text == "MPstats(Профессиональный)💹", state='*')
async def info(message: types.Message):
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Mpstats (Тариф "Профессиональный")🚀️\n\n\n'
                         '✔️ Тариф "Профессиональный"\n'
                         '✔️ Цена - 2500₽ в месяц / вместо 25.000₽\n'
                         '✔️ Никакого графика и очередей\n\n'
                         '(Окно выборки данных: 91 день)\n\n\n'
                         '✅Пользоваться можно без ограничений\n\n'
                         '✅Работает 24 часа в сутки\n\n'
                         '✅Отдельный закрытый чат для общения и поддержки по MPstats\n\n\n'
                         '❗️Вам будет выдан личный логин и пароль, благодаря такой системе входа вы не будете вылетать и полноценно сможете пользоваться сервисом.\n\n'
                         'После оплаты с вами свяжется менеджер и проведет проверку на подставного покупателя, это происходит быстро. 😊\n\n\n'
                         "💥Новый метод входа в WEB MPSTATS !\n\n"
                         "🔸НЕ ВЫЛЕТАЕТ ИЗ МПСТАТ\n\n "
                         '🔸Работает плагин мпстат c кнопой "Открыть в MPstats"\n\n'
                         "🔸Можете добавить свой Api ключ из Wildberries\n\n "
                         "🔸Без очередей и с удобного вам браузера и устройства Macbook, IPhone, Windows, Android\n\n "
                         "🔸Не нужно скачивать никаких программ и прочих некомфортных действий",
                         reply_markup=kb.tarifs_kb)
    await FSMProf.prof_pay_and_get.set()


@dp.message_handler(state=FSMProf.prof_pay_and_get)
async def pay_choise(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.PAYMENTS_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите способ оплаты:', reply_markup=kb.payments_kb)
    await FSMProf.prof_pay_choise.set()


@dp.message_handler(state=FSMProf.prof_pay_choise)
async def any_or_sbor(message: types.Message):
    prof_choise = message.text
    if prof_choise == 'Любой картой✅':
        await message.reply('Вы производите оплату доступа к сервису Mpstats (Тариф "Профессиональный") на 30 дней.')
        await message.reply('<a href="https://clicks.su/gx7zL1">Оплатить 2500₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    elif prof_choise == 'Тинькофф Сбор☑':
        await message.reply('Вы производите оплату доступа к сервису Mpstats (Тариф "Профессиональный") на 30 дней.\n\n'
                            '🚫Обязательно указать комментарий: на путешествие, на отдых\n\n'
                            '❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
                            'По всем вопросам: @AndreasBel_admin')
        await message.reply('<a href="https://clicks.su/9qGqRg">Оплатить 2500₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    await bot.send_message(chat_id=message.chat.id, text='После осуществления перевода введите слово: Оплачено 👇')
    await FSMProf.prof_paid.set()


@dp.message_handler(lambda message: message.text == "Оплачено", state=FSMProf.prof_paid)
async def top(message: types.Message, state: FSMContext):
    admin_chat_id = config.ADMIN_ID
    date_and_time = message.date
    await message.answer('Оплата успешно произведена ✅\n\n'
                         'Ожидайте сообщения от администратора.')
    await bot.send_message(chat_id=admin_chat_id, text=f'Stat_city_bot, [{date_and_time}]\n'
                                                       f'{message.from_user.id}\n'
                                                       f'Логин: {message.from_user.username}\n'
                                                       f'Имя: {message.from_user.first_name}\n'
                                                       f'Оплатил(а) Mpstats✅')
    await state.finish()


@dp.message_handler(lambda message: message.text == "Moneyplace(Premium)📈", state='*')
async def prem_tarif(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Moneyplace (Тариф "Premium") 🚀\n\n'
                         '✔️ Тариф "Premium"\n'
                         '✔️ Цена - 2500р в месяц\n\n'
                         '✔️ Никакого графика и очередей\n\n\n'
                         '✅Пользоваться можно без ограничений\n\n'
                         '✅Работает 24 часа в сутки\n\n'
                         '✅Отдельный закрытый чат для общения и поддержки по Moneyplace\n\n\n'
                         '❗️Вам будет выдан личный логин и пароль, благодаря такой системе входа вы не будете вылетать и полноценно сможете пользоваться сервисом.\n\n'
                         'После оплаты с вами свяжется менеджер и проведет проверку на подставного покупателя, это происходит быстро. 😊\n\n\n'
                         '💥Новый метод входа в WEB MONEYPLACE !\n\n'
                         '🔸НЕ ВЫЛЕТАЕТ ИЗ MONEYPLACE\n\n'
                         '🔸Можете добавить свой Api ключ из Wildberries\n\n'
                         '🔸Без очередей и с удобного вам браузера и устройства Macbook, IPhone, Windows, Android\n\n'
                         '🔸Не нужно скачивать никаких программ и прочих некомфортных действий\n\n'
                         '🔸Наша команда гарантирует помощь при любых проблемах', reply_markup=kb.tarifs_kb)
    await FSMPrem.prem_pay_and_get.set()


@dp.message_handler(state=FSMPrem.prem_pay_and_get)
async def pay_choise(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.PAYMENTS_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите способ оплаты:', reply_markup=kb.payments_kb)
    await FSMPrem.prem_pay_choise.set()


@dp.message_handler(state=FSMPrem.prem_pay_choise)
async def any_or_sbor(message: types.Message):
    prof_choise = message.text
    if prof_choise == 'Любой картой✅':
        await message.reply('Вы производите оплату доступа к сервису Moneyplace (Тариф "Premium") на 30 дней.')
        await message.reply('<a href="https://clicks.su/gx7zL1">Оплатить 2500₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    elif prof_choise == 'Тинькофф Сбор☑':
        await message.reply('Вы производите оплату доступа к сервису Moneyplace (Тариф "Premium") на 30 дней.\n\n'
                            '🚫Обязательно указать комментарий: на путешествие, на отдых\n\n'
                            '❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
                            'По всем вопросам: @AndreasBel_admin')
        await message.reply('<a href="https://clicks.su/9qGqRg">Оплатить 2500₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    await bot.send_message(chat_id=message.chat.id, text='После осуществления перевода введите слово: Оплачено 👇')
    await FSMPrem.prem_paid.set()


@dp.message_handler(lambda message: message.text == "Оплачено", state=FSMPrem.prem_paid)
async def top(message: types.Message, state: FSMContext):
    admin_chat_id = config.ADMIN_ID
    date_and_time = message.date
    await message.answer('Оплата успешно произведена ✅\n\n'
                         'Ожидайте сообщения от администратора.')
    await bot.send_message(chat_id=admin_chat_id, text=f'Stat_city_bot, [{date_and_time}]\n'
                                                       f'{message.from_user.id}\n'
                                                       f'Логин: {message.from_user.username}\n'
                                                       f'Имя: {message.from_user.first_name}\n'
                                                       f'Оплатил(а) Moneyplace✅')
    await state.finish()


@dp.message_handler(lambda message: message.text == "MarketGuru(Комбинированый)📉", state='*')
async def prem_tarif(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Личный аккаунт MarketGuru по стоимости 2000₽ (вместо 11000₽)\n\n'
                         '✔️ Тариф "Комбинированный"\n'
                         '✔️ Цена - 2000₽ в месяц / вместо 11000₽\n'
                         '✔️ Личный аккаунт в 1 руки (полный доступ)\n\n'
                         '✅Пользоваться можно без ограничений\n\n'
                         '✅Переходите на сайт Marketguru.ru и вводите логин и пароль\n\n'
                         '✅Отдельный закрытый чат для общения\n\n'
                         '❗️Вам будет выдан личный логин и пароль, благодаря такой системе входа вы не будете вылетать и полноценно сможете пользоваться сервисом.\n\n'
                         'После оплаты с вами свяжется менеджер и проведет проверку на подставного покупателя, это происходит быстро. 😊',
                         reply_markup=kb.tarifs_kb)
    await FSMComposite.composite_pay_and_get.set()


@dp.message_handler(state=FSMComposite.composite_pay_and_get)
async def pay_choise(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.PAYMENTS_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите способ оплаты:', reply_markup=kb.payments_kb)
    await FSMComposite.composite_pay_choise.set()


@dp.message_handler(state=FSMComposite.composite_pay_choise)
async def any_or_sbor(message: types.Message):
    prof_choise = message.text
    if prof_choise == 'Любой картой✅':
        await message.reply('Вы производите оплату доступа к сервису MarketGuru (Тариф "Комбинированный") на 30 дней.')
        await message.reply('<a href="https://clicks.su/gx7zL1">Оплатить 2000₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    elif prof_choise == 'Тинькофф Сбор☑':
        await message.reply(
            'Вы производите оплату доступа к сервису MarketGuru (Тариф "Комбинированный") на 30 дней.\n\n'
            '🚫Обязательно указать комментарий: на путешествие, на отдых\n\n'
            '❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
            'По всем вопросам: @AndreasBel_admin')
        await message.reply('<a href="https://clicks.su/9qGqRg">Оплатить 2000₽</a>', parse_mode="HTML",
                            reply_markup=kb.main_menu_kb)
    await bot.send_message(chat_id=message.chat.id, text='После осуществления перевода введите слово: Оплачено 👇')
    await FSMComposite.composite_paid.set()


@dp.message_handler(lambda message: message.text == "Оплачено", state=FSMComposite.composite_paid)
async def top(message: types.Message, state: FSMContext):
    admin_chat_id = config.ADMIN_ID
    date_and_time = message.date
    await message.answer('Оплата успешно произведена ✅\n\n'
                         'Ожидайте сообщения от администратора.')
    await bot.send_message(chat_id=admin_chat_id, text=f'Stat_city_bot, [{date_and_time}]\n'
                                                       f'{message.from_user.id}\n'
                                                       f'Логин: {message.from_user.username}\n'
                                                       f'Имя: {message.from_user.first_name}\n'
                                                       f'Оплатил(а) MarketGuru✅')
    await state.finish()


@dp.message_handler(lambda message: message.text == "Главное меню🗂", state='*')
async def main_menu(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(
        f"Привет, Denis! Рады вас видеть😊 \n \n С помощью этого бота вы сможете получить доступ к сервису аналитики для маркетплейсов, который подходит именно вам.",
        reply_markup=kb.start_kb)


@dp.message_handler(lambda message: message.text == 'Чат👥', state='*')
async def contact_tp(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.reply('<a href="https://clicks.su/ydaaKg">Chat</a>', parse_mode="HTML")


@dp.message_handler(lambda message: message.text == 'Отзывы💬', state='*')
async def contact_tp(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.reply('<a href="https://clicks.su/m0xm1m">Rewievs</a>', parse_mode="HTML")


@dp.message_handler(lambda message: message.text == "Написать в тех. подержку✍", state='*')
async def top(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    photo = config.BOT_PHOTO_ID
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('<a href="https://clicks.su/yYllW9">Help</a>', parse_mode="HTML")
