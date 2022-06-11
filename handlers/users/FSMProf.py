from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

from loader import dp, bot
from . import start_keyboard as kb
from .states import FSMProf


@dp.message_handler(lambda message: message.text == "MPstats(Профессиональный)💹")
async def info(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/total_dom.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Mpstats (Тариф "Профессиональный")🚀️\n\n\n'
                         '✔️ Тариф "Профессиональный"\n'
                         '✔️ Цена - 2800₽ в месяц / вместо 28.000₽\n'
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
async def pay_choise(message: types.Message, state: FSMContext):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите способ оплаты:', reply_markup=kb.payments_kb)
    prof_pay_choise = message.text
    await state.update_data(
        {
            'prof_pay_choise': prof_pay_choise
        }
    )
    await FSMProf.prof_pay_choise.set()


@dp.message_handler(state=FSMProf.prof_pay_choise)
async def any_or_sbor(message: types.Message, state=FSMContext):
    data = await state.get_data()
    choise = data.get('prof_pay_choise')
    if choise == 'Любой картой✅':
        await message.reply('Вы производите оплату доступа к сервису Mpstats (Тариф "Профессиональный") на 30 дней.', reply_markup=kb.pay_2800_any)
        await FSMProf.prof_pay_2800_any.set()
    elif choise == 'Тинькофф Сбор☑':
        await message.reply('Вы производите оплату доступа к сервису Mpstats (Тариф "Профессиональный") на 30 дней.\n\n'
'🚫Обязательно указать комментарий: на путешествие, на отдыхn\n\n'
'❗️После оплаты отправьте скрин чека нам в личные сообщения 👇\n\n'
'По всем вопросам: @AndreasBel_admin)', reply_markup=kb.pay_2800_sbor)
        await FSMProf.prof_pay_2800_sbor.set()


@dp.message_handler(state=FSMProf.prof_pay_2800_any)
async def pay_2800_any(message: types.Message, state=FSMContext):
    await message.reply('<a href="https://clicks.su/mjqPMX">Any card</a>', parse_mode="HTML")
    await state.finish()


@dp.message_handler(state=FSMProf.prof_pay_2800_sbor)
async def pay_2800_any(message: types.Message, state=FSMContext):
    await message.reply('<a href="https://clicks.su/9qGqRg">Tinkoff Sbor</a>', parse_mode="HTML")
    await state.finish()
