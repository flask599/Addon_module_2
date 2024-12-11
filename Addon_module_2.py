print('Задание "Слишком древний шифр"!')
print('--------------------------------')
n = int(input('Enter number "n": '))
result = ''
for i in range(1,n):
    for j in range(1,n):
        if i >= j:
            continue
        else:
            b = n % (i + j)
        if b == 0:
            result =  result + str(i) + str(j)

print('Enter the password to login:',result)







