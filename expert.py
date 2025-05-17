from tkinter import Tk, simpledialog, messagebox

# Функция для считывания данных их текстового файла
def read_from_file():
    with open('cyber_attacks_data.txt', encoding='utf-8') as file:
        for line in line:
            line = line.rstrip('\n')  # Удаляет символ "перевод строки"
            attack, definition = line.split('/')  # Символ '/' разделяет строку, в attack попадают названия кибер-атак, а в definition - их определения
            cyber_attack[attack] = definition  # attack является ключом, а definition - значением

# Функция для записи данных в текстовый файл
def write_to_file(attack_type, definition_text):
    with open('cyber_attack_data.txt', ' a', encoding='utf-8') as file:
        file.write('\n', attack_type, '/', definition_text)  # Записывает в файл тип атаки (attack_type) и ее определение (definition_text)

print('The Expert - Cyber Attacks')
root = Tk()
root.withdraw()

cyber_attacks = {}  # Создаем пустой словарь для хранения кибер-атак и их определений
