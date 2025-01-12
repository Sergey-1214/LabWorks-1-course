
try:
    with open('example.txt','r') as file:
        print(content:=file.read())
except FileNotFoundError:
    print('Извините, файл не найден')