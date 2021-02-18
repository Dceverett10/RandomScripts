import random
print('You are Philip Rivers, on the journey to win a Superbowl!')
print('You begin your journey in SoFi Stadium, and you have met your first enemy, Derek Carr! He\'s wearing eyeliner, this should be easy.')




derekHealth = 100
while True:
    print('Would you like to throw or run?')
    play = input()
    if play == 'throw':
        r1 = random.randint(1,30)
        if r1 <= 21:
                print ('Pass complete! You are one step closer to defeating Derek Carr! ' + str(derekHealth - r1) + ' yards to go!')
                derekHealth = derekHealth - r1
        if r1 == 22:
                print ('Pass intercepted!')
        if r1 > 22:
                print('Pass incomplete!')
    if play == 'run':
        r2 = random.randint(1,13)
        if r2 <= 8:
            print ('Austin Ekeler takes the handoff. You run for a minimum gain. You will not defeat Derek Carr by running the ball without blocking. Someone should tell the Coach! ' +str(derekHealth - r2) + ' yards to go')
            derekHealth = derekHealth - r2
        if r2 == 9:
            print('Melvin Gordon takes the handoff, FUMBLE!')
        if r2 >= 10:
            print ('Austin Ekeler takes the handoff. You run for a solid gain! I guess establishing the run really does work! ' +str(derekHealth - r2) + ' yards to go')
            derekHealth = derekHealth - r2
    break
while True:
    print('Would you like to throw or run Derek?')
    play = input()
    if play == 'throw':
        r1 = random.randint(1,30)
        if r1 <= 21:
                print ('Pass complete! You are one step closer to defeating Derek Carr! ' + str(derekHealth - r1) + ' yards to go!')
                derekHealth = derekHealth - r1
        if r1 == 22:
                print ('Pass intercepted!')
        if r1 > 22:
                print('Pass incomplete!')
    if play == 'run':
        r2 = random.randint(1,13)
        if r2 <= 8:
            print ('Austin Ekeler takes the handoff. You run for a minimum gain. You will not defeat Derek Carr by running the ball without blocking. Someone should tell the Coach! ' +str(derekHealth - r2) + ' yards to go')
            derekHealth = derekHealth - r2
        if r2 == 9:
            print('Melvin Gordon takes the handoff, FUMBLE!')
        if r2 >= 10:
            print ('Austin Ekeler takes the handoff. You run for a solid gain! I guess establishing the run really does work! ' +str(derekHealth - r2) + ' yards to go')
            derekHealth = derekHealth - r2









    




