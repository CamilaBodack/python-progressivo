file = open('list_languages.txt', 'r')
linguagens = file.readlines()

print("Existem", len(linguagens), "linguagens. Quantas deseja ver ?")
num = int(input())

for count in range(num):
    print(str(count+1), ":", linguagens[count].rstrip('\n'))


file.close()
