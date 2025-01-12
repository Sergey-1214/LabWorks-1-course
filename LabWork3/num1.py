
with open('example.txt','r') as file:
    print(content:=file.read())
    
with open('example.txt','r') as file:
    for line in file:
        print(line.strip())
