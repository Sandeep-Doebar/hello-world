hello = "hello world"
print(hello+"!")
while True:
    Y = "Y"
    firstname = input('What is your first name?\n')
    lastname = input('What is your last name?\n')
    print ("your name is " + firstname + " " + lastname )
    correct = input('is this correct? Answer in Y or N\n')
    if correct == Y:
        print ("Nice to meet you " + firstname)
        break
    print("Please try again")