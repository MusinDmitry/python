number = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
          "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

def number_translate(word):
    return number.get(word)

print(number_translate(input("Введите число от 0 до 10 на англ: ")))