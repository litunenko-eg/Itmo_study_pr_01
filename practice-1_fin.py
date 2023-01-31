import string

sym_count = 0  # Подсчитывает общее количество символов в файле
spl_count = 0  # Подсчитывает общее количесто символов без пробелов
sgl_count = 0  # Подсчитывает количество символов без знаков препинания
word_count = 0  # Подсчитывает количество слов в файле
sent_count = 0  # Подсчитывает количество предложений

sent_final = {'.', '?', '!'} # знаки конца предложения
syntax = set(string.punctuation+string.digits) # знаки пунктуации и цифры
punctuation = {'.', ',', '?', '!', '`', ';', '/', '-', '[', ']', '"', '_', ':', '{', '}', "'", '(', ')'} # знаки препинания
punct_count = 0


with open("aristotle.txt", "r", encoding='utf-8-sig') as file1:
    for line in file1:
        l = len(line)
        sym_count += l  # подсчет количества символов в строке
        spl_count += l - line.count(' ') # подсчет количества символов без пробелов

        for i in punctuation: # подсчет количества знаков препинания
            punct_count += line.count(i)

        for i in range(l - 2): # подсчет количества предложений
            if line[i] in sent_final:
                if line[i + 1] == '\n' or (line[i + 1] == ' ' and line[i + 2].isupper()) or line[i + 1] == '\'':
                    sent_count += 1
            i += 1
        if (line[l - 2] in sent_final) or (line[l - 1] in sent_final):
            sent_count += 1

        for i in syntax: # подсчет количества слов
            if i in line:
                line = line.replace(i, ' ')
        line = line.split()
        word_count += len(line)

sgl_count = sym_count - punct_count # подсчет количества символов без знаков препинания

print('Количество символов в тексте (с учетом символа переноса коретки):', sym_count)
print('Количество символов в тексте без пробелов (с учетом символа переноса коретки):', spl_count)
print('Количество символов в тексте без знаков препинания, но с пробелами (с учетом символа переноса коретки):',
      sgl_count)
print('Количество слов в тексте:', word_count)
print('Количество предложений в тексте:', sent_count)
