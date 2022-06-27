from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
IP = env.str("IP")  # Тоже str, но для айпи адреса хоста
ADMIN_ID = env.str('ADMIN_ID')
