print("PlayHow will be millionaire")

# Доступные подсказки
pod50 = True
podzn = True
summa = 0
n_summa = 0


def dost_podsazki():
    print(f"\t\t\tТекущая сумма: {summa} грн")
    print("\t\t\tДоступные подсказки:")
    if pod50 and podzn:
        print("\t\t\t1. 50 на 50")
        print("\t\t\t2. Помощь друга")
    elif pod50:
        print("\t\t\t1. 50 на 50")
    elif podzn:
        print("\t\t\t2. Помощь друга")
    else:
        print("\t\t\tНет доступных подсказок")


def podskazki(a, b):
    global pod50, podzn
    question = input("Хотите использовать подсказку? (да/нет): ").lower()
    if question in ["да", "yes"]:
        if not pod50 and not podzn:
            print("Нет доступных подсказок")
            return
        if pod50 and podzn:
            pods = input("Выберите подсказку (50 на 50 / помощь друга): ").lower()
        elif pod50:
            pods = "50 на 50"
        else:
            pods = "помощь друга"
        
        if pods == "50 на 50":
            print(f"1. {a}\t2. {b}")
            pod50 = False
        elif pods == "помощь друга":
            print(f"Друг советует выбрать: {b}")
            podzn = False
        else:
            print("Некорректный выбор подсказки")


def question(num, text, a1, a2, a3, a4):
    print(f"Вопрос №{num}: {text}")
    print(f"1. {a1}\t2. {a2}")
    print(f"3. {a3}\t4. {a4}")


def loose():
    print("К сожалению, вы проиграли!")
    print(f"Ваш выигрыш составил: {n_summa} грн")
    exit()


# Начало игры
begin = input("Хотите начать игру? (да/нет): ").lower()
if begin not in ["да", "yes"]:
    exit()

Continue = True

dost_podsazki()
question(1, "Какой континент состоит только из одной страны?", "Европа", "Азия", "Африка", "Австралия")
podskazki("Европа", "Австралия")
answer = input("Введите ответ: ").lower()
if answer == "австралия":
    print("Верно!")
    summa = 500
else:
    loose()

# Второй вопрос
dost_podsazki()
question(2, "Где растут подсолнухи?", "На земле", "На солнце", "В небе", "В океане")
podskazki("На земле", "На солнце")
answer = input("Введите ответ: ").lower()
if answer == "на земле":
    print("Верно!")
    summa = 1000
else:
    loose()

# Третий вопрос
dost_podsazki()
question(3, "Какой из этих вариантов не является валютой?", "Гривна", "Ложь", "Доллар", "Лира")
podskazki("Лира", "Ложь")
answer = input("Введите ответ: ").lower()
if answer == "ложь":
    print("Верно!")
    summa = 2000
else:
    loose()

# Четвертый вопрос
dost_podsazki()
question(4, "Как называется беспилотный летательный аппарат?", "Дрон", "Максон", "Анион", "Фантом")
podskazki("Анион", "Дрон")
answer = input("Введите ответ: ").lower()
if answer == "дрон":
    print("Верно!")
    summa = 10000
    n_summa = 10000
else:
    loose()

# Пятый вопрос
dost_podsazki()
question(5, "В какой игре не используется мяч?", "Баскетбол", "Теннис", "Бейсбол", "Керлинг")
podskazki("Теннис", "Керлинг")
answer = input("Введите ответ: ").lower()
if answer == "керлинг":
    print("Верно!")
    summa = 25000
else:
    loose()

# Финальный вопрос
dost_podsazki()
question(6, "Какой химический элемент получил название из-за синей линии в спектре?", "Родий", "Индий", "Церий", "Нептун")
podskazki("Родий", "Индий")
answer = input("Введите ответ: ").lower()
if answer == "индий":
    print("Поздравляем! Вы выиграли 1 000 000 грн!")
else:
    loose()
