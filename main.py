# task 1
import os

print('Текущая директория: ', os.getcwd())
os.mkdir('folder')
os.chdir('folder')
print('Текущая директория изменилась на folder: ', os.getcwd())
os.makedirs('level_1/level_2/level_3')
text_file = open('text.txt', 'w')
text_file.write('Это текстовый файл')
os.rename('text.txt', 'renamed-text.txt')
os.replace('renamed-text.txt', 'folder/renamed-text.txt')
print('Все папки и файлы: ', os.listdir())
os.walk():
for dirpach, dirnames, filenames in os.walk('.'):
    for dirname in dirnames:
        print('Каталог: ', os.path.join(dirpach, dirname))
        for filename in filenames:
            print('Файл: ', os.path.join(dirpach, dirname))
os.remove('folder/renamed-text.txt')
os.rmdir('folder')
os.removedirs('level_1/level_2/level_3')
open('text.txt', 'w').write('Это текстовый файл: ')
print(os.stat('text.txt'))

# task 2
string = ('Подсудимая Эверт-Колокольцева Елизавета Александравна в судебном заседании '
          'вину инкриминируемого правонарушения признала в полном объёме и суду показала, '
          'что 14 сентября 1876 года, будучи в состоянии алькогольного опьянения от '
          'безысходности, в связи с состоянием здоровья позвонила со своего стационарного '
          'телефона в полицию, сообщив о том, что у неё в квартире якобы заложена бомба. '
          'После чего приехали сотрудники полиции, скорая и пожарные, которым она сообщила, '
          'что бомба - это она.')
print(re.sub(r'[А-ЯЁ]\w*'
             r'(?:-[А-ЯЁ]\w*)?'
             r'(?:[А-ЯЁ]\w*){2}', 'N', string)

# task 3
list = 'abc a bCd bC AbC BC BCD bcd ABC'
with open('file.txt', 'r') as f:
s = list(map(lambda i: i.strip('.,!?'), f.read().lower().split()))
m = max(sorted(s), key=lambda j: s.count(j))
print('%s %d' % (m, s.count(m)))

# task 4
with open('stop_words.txt') as stop_words, open(input()) as to_change:
    pattern, text = stop_words.read().split(), to_change.read()
text_lower = text.lower()
for word in pattern:
    text_lower = text_lower.replace(word, '*' * len(word))
result = ''.join((y, x)[x == '*'] for x, y in zip(text_lower, text))
print(result)

# task 5
f = open('text.txt')
suma = 0
n = 0
for i in f:
    g = int(i[len(i) - 2])
suma += g
n += 1
if g < 3:
    print(i[:-1])

    # task 6

    # task 7
