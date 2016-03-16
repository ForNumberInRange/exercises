__author__ = 'dozie9'

num = input('Enter a number')
divList = []
for i in range(1,num/2 + 1):
    if num%i == 0 :
        divList.append(i)
print divList