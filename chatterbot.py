print("What is your name? ")

name = input().lower

if name == "anakin":
    print("How do you do Anakin?")
elif name == "leia":
    print("The force is with you.")
else:
    print(f'Nice name, {name}.')

print('\n How\'s the weather today?')


weather = input().upper

if weather == 'COLD':
    print('You must be freezing!')
elif weather == 'HOT':
    print('Drink a lot of water.')
else:
    print("I can't help you with that.")


print('\n Do you like the colour blue?')

answer = input().lower

if answer == 'yes':
    print('I like blue too!')
else:
    print('Thats a shame because I really like blue.')

print('\n\n Have a good day!')

