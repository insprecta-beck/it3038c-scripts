import time
start_time = time.time()

print('What is your name?')
myName = input()

## Prompt for specfic name.
while myName != 'your name':
    print('This is not your name. Please type "your name"?')
    myName = input()
while myName != 

print('hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())

# determine message based on age.
if myAge < 13:
    print("Learning young. That's good.")
elif myAge == 13:
    print("Hey you're a teenager now.")
elif myAge > 13:
    print("Still young. Still learning.")

programAge = int(time.time() - start_time)
print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2))

time.sleep(3)
print("I'm tired. I go sleep now")