import random

choices = ['Rock','Paper','Scissor']
winlist = [('Rock','Scissor'),('Paper','Rock'),('Scissor','Paper')]
print("random item from list is: ", )

user = ''
while not user=='q':
    user = input("Your Choise: ")
    pc = random.choice(choices)
    print(f'PC choice is {pc}')
    if user in choices:
        if user == pc:
            print('Tie')
        elif (user,pc) in winlist:
            print('You won!')
        else:
            print('PC won')
