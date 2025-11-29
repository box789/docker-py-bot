import os


# Получаем все переменные среды. Переменные среды — это пары ключ-значение, 
# которые определяют аспекты окружения, в котором работает программа.
spis = os.environ

# Итерируем по каждой паре ключ-значение
for key, value in spis.items():
    print(f"{key} = {value}")


psw = os.getenv("MYPASSWORD", "00000000")
print(psw)
