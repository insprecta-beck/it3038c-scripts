#This program asks for an int input 
#and outputs all the prime numbers between
#the input int and 0.

start_val = 1
n = int(input("Type a number! Any number!:"))
for num in range(start_val, n+1):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
print('Those are all the prime numbers between ' + str(n) + ' and 0.')
