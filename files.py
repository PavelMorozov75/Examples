# r (read) - открыть для чтения (по умолчанию)
# w (write) - открыть для записи, содержимое файла стирается
# a (append) - открыть для записи, запись ведется в конец
'''
f = open("test.txt")
#d = f.read()
d = f.readline().rstrip()
print(d)
d = f.readline().rstrip()
print(d)
'''
# d = d.splitlines()
# print(d)

'''
for line in f:
    line = line.rstrip()
    print(repr(line))
x = f.read(5)
print(repr(x)) 

f.close()
'''

'''
f = open("test1.txt", "w") # в случае отсутствия файл создастся
lines = ["Line 1", "Line 2", "Line 3"]
contents = "\n".join(lines)
f.write(contents)
f.close()

f = open("test_append.txt", "a")
f.write("Hello\n")
f.close()

with open("test.txt") as f, open("test_copy.txt", "w") as w:
    for line in f:
        w.write(line)

'''

'''
f1 = open('test.txt', 'r')
f2  = open('test_new.txt', 'w')
lst = []
#a  = [line.rstrip() for line in f1]
#print(a)

for line in f1:
    lst.append(line.rstrip())
lst.reverse()
count = 1
for i in lst:
    if count  < len(lst):
        f2.write(i+'\n')
        count +=1
    else:
        f2.write(i)


f1.close()
f2.close()
'''

'''
f1 = open('test.txt', 'r')
f2  = open('test_new.txt', 'w')
lst2 = []
while True:
    stro = f1.readline().rstrip()
    if stro == '': # при окончании файла считываем пустую строку
        break
    else:
        lst2.append(stro)
lst2.reverse()
count = 1
for i in lst2:
    if count  < len(lst2):
        f2.write(i+'\n') # во все строки кроме последней добавляем перенос строки
        count +=1
    else:
        f2.write(i) # в последнюю строку перенос строки не добавляем

print(lst2)
f1.close()
f2.close()
'''

'''
import sys
sys.path.insert(1, './pages')
'''

'''
import os
import os.path
print(os.listdir('c:/FAR'))
print(os.listdir())# содержание текущей директории
current_dir = os.getcwd()
print(current_dir)
print(os.pardir)
#os.chdir(os.pardir)
print(current_dir)
print(os.path.exists('main.py'))
print(os.path.isfile('main.py'))
print(os.path.isdir('main.py'))
print(os.path.abspath('main.py'))
#for current_dir, dirs, files in os.walk("."):
    #print(current_dir, dirs, files)

#import shutil
#shutil.copy('test.txt', 'test25.txt')
#shutil.copytree('test', 'test/test')# копируем каталог целиком
'''
