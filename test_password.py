from dotenv import load_dotenv
from os import getenv

load_dotenv()

password = getenv("SECRET_PASSWORD")

if password == "12345678":
    print("Доступ открыт!")
else:
    print("Доступ запрещён!")