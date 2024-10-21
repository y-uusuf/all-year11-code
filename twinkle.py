import time


def twinkle_twinkle():
 print('Twinkle twinkle, little star.\n')
 time.sleep(2)
 print('How I wonder what you are.\n')
 time.sleep(2)
 print('Up above the world so high.\n')
 time.sleep(2)
 print('Like a diamond in the sky.\n')
 time.sleep(2)

def song():
 print('CR [Nines]\n')
 time.sleep(3)
 print('Skinny N**** with a fat belly,\n')
 time.sleep(2)
 print('Selling cheese straight off the BlackBerry,\n')
 time.sleep(2)
 print('In the night, I be chillin\' with a bad b****,\n')
 time.sleep(2)
 print('I was born broke but guaranteed I\'d die rich.\n')
 time.sleep(2)

choice = int(input('[1]  Twinkle Twinkle\n\n[2]  CR: Nines.\n>> '))

if choice == 1:
 twinkle_twinkle()
elif choice == 2:
 song()
else:
 exit