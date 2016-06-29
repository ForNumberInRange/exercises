__author__ = 'dozie9'

num = int(input('Enter a number'))
divList = []
for i in range(1,num + 1):
    if num%i == 0 :
        divList.append(i)
print divList
