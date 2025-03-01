import os

path = r"."
allItems = os.listdir(path)

directories = [d for d in allItems if os.path.isdir(os.path.join(path,d))]

files = [f for f in allItems if os.path.isfile(os.path.join(path,f))]

print(f"directories: {directories}")
print(f"files: {files}")
print(f"all items: {allItems}")
print()

# 2
print(f'is path exist? {os.path.exists(path)}')
print(f'is it readable? {os.access(path, os.R_OK)}')
print(f'is it writeable? {os.access(path, os.W_OK)}')
print(f'it is executable? {os.access(path, os.X_OK)}')
print() 

# 3 
if os.path.exists(path):
    print(f'path exists: {path}')
    print(f'directory: {os.path.dirname(path)}')
    print(f'fale nime: {os.path.basename(path)}')
    print()
else: 
    print('directory not exist')
    print()

# 4 
filename = 'built-inFunc.py'

with open(filename, "r", encoding = "utf-8") as file:
    lineCount = len(file.readlines())
print(f'number of lines : {lineCount}')

# 5
data = ['#hehe', '#haha', '#hoho']

with open(filename, 'w', encoding = 'utf-8') as file:
    for item in data:
        file.write(item + '\n')
print('datas succesfully written')
print()

# 6 

for i in range(26):
    letter = chr(ord("A")+i)
    filename = f'{letter}.txt'

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f'This is file {filename}\n')

# 7
source = 'A.txt'
destination = "B.txt"
with open(source, "r", encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
    for line in src:
        dest.write(line)

# 8

filePath = 'Z.txt'

if os.path.exists(filePath):
    if os.access(filePath, os.R_OK) and os.access(filePath, os.W_OK):
        os.remove(filePath)
    else: 
        print('not allowed')
else:
    print('file doesnt exist')


