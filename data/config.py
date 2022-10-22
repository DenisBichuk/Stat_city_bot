from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
IP = env.str("IP")  # Тоже str, но для айпи адреса хоста
ADMIN_ID = env.str('ADMIN_ID')

BOT_PHOTO_ID = env.str('BOT_PHOTO_ID')
TOP_ID = env.str('TOP_ID')
TOTAL_DOM_ID = env.str('TOTAL_DOM_ID')
PAYMENTS_ID = env.str('PAYMENTS_ID')
OZON_ID = env.str('OZON_ID')