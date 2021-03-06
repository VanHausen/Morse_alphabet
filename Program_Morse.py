import random # Импорт библиотеки random

morse_full = {   # Словарь с азбукой Морзе
  "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
  "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
  "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
  "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
  "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--",
  "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"
}

encode_list = ["transcendent", "werewolf", "microscope", "angel", "rhetorical", "succubus", ] # Список слов для шифрования Морзе
decode_list = ["-.-..--....-.-..-.-...-.-", ".--..-...-----.-....-.", "--..-.-..-.---...-.-.---.--..", ".--.--...-..",".-......----.-...-.-..-.-..", ".....--.-.-.-...--.....-...", ] # Список слов для шифрования Морзе

def get_word_encode(): # Функция - получает случайное слово из списка(encode)
  return random.choice(encode_list)

def get_word_decode(): # Функция - получает случайное слово из списка(decode)
  return random.choice(decode_list)

def morse_encode(word): # Функция - шифратор Морзе
    word_1 = ""
    for i in word.lower():
      if i in morse_full.keys():
        word_1 += morse_full[i] + ''
 #     if i == ' ':
 #       word_1 += ' | '  # Слова разделяются вертикальной чертой
    return word_1


def get_key(val, dct):  # Функция возвращает ключ словаря по значению(Для декода)
  for key, value in dct.items():
    if val == value:
      return key

def morse_decode(word): # Функция - дешифратор Морзе
  word_2, word = "", word.split()
  for i in word:
    if i in morse_full.values():
      word_2 += get_key(i, morse_full) + ''
 #   if i == ' ':
 #     word_2 += ' | '  # Слова разделяются вертикальной чертой
  return word_2


def print_statistics(answers):  # Функция статистики по списку
  print(f"Всего задачек: {6}")
  print(f"Отвечено верно: {len(answers)}")
  print(f"Отвечено неверно: {6 - len(answers)}")
  print("\n__________________КОНЕЦ ПРОГРАММЫ____________________\n")
  exit()



def changer_morse():  # Переключатель режимов кодировки/декодировкм
  count_word = 0
  while count_word < 6:
    count_word += 1
    answer = input('Выберите действие: Раскодировать или закодировать?\nВведите ENCODE - если хотите раскодировать, и '
                   'DECODE - если хотите закодировать: >>> ')
    if answer == 'ENCODE':
      answers =[]
      num_1 = 0
      i = 0
      for i in range(6):
        word_1 = get_word_encode()  # ПРИСВАИВАНИЕ ПЕРЕМЕННЫМ ФУНКЦИЙ(encode)
        word_encoded = morse_encode(word_1)
        i += 1
        num_1 += 1
        answ_1 = input(f'СЛОВО {num_1} - {word_1} \nВведите слово кодом Морзе: ')
        print(morse_encode(answ_1))
        if word_encoded == answ_1:
            print(f"Верно, {word_encoded}")
            answers.append(True)
        else:
            print(f"Неверно, {word_encoded}")
    elif answer == 'DECODE':
      answers = []
      num_2 = 0
      for i in range(6):
        word_2 = get_word_decode()  # ПРИСВАИВАНИЕ ПЕРЕМЕННЫМ ФУНКЦИЙ(decode)
        word_decoded = morse_decode(word_2)
        i += 1
        num_2 += 1
        answ_2 = input(f'СЛОВО {num_2} - {word_2} \nВведите слово для расшифровки с языка Морзе: ')
        print(answ_2)
        if word_decoded == answ_2:
            print(f"Верно, {word_decoded}!")
            answers.append(True)
        else:
            print(f"Неверно, {word_decoded}!")
    else:
      print('Введите корректную команду.')

    print_statistics(answers)

begin = input("Сегодня мы потренируемся расшифровывать азбуку Морзе.\nНажмите Enter и начнем: ") # Приветствие
if begin == "Enter":
  changer_morse()


else:
  print("Вы ввели неверную клавишу. Перезапустите программу дешифратора")
  exit()
