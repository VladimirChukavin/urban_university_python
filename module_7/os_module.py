# Файлы в операционной системе

import os

print('Current directory:', os.getcwd())
# os.mkdir('one')

if os.path.exists('one'):
    os.chdir('one')
else:
    os.mkdir('one')
    os.chdir('one')

print('Current directory:', os.getcwd())

# os.makedirs(r'two\test')

print(os.listdir())

for i in os.walk('.'):
    print(i)

os.chdir(r'D:\myexperiences\urban_university_python\module_7')
print('Current directory:', os.getcwd())
print(os.listdir())

file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(file)
print(dirs)

# os.startfile(file[3])

print(os.stat(file[3]))
print(os.stat(file[3]).st_size)

# os.system('pip list')

print(os.name)