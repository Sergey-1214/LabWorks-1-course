#2.1

with open('user_input.txt','w') as file:
    string = input("Введите текст для записи:")
    file.write(string)

#2.2
with open('user_input.txt','a') as file:
    string = input("Введите текст для записи:")
    file.write(string)
