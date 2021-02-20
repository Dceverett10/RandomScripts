import random
print('You are Philip Rivers, on the journey to win a Superbowl!')
print('You begin your journey in SoFi Stadium, and you have met your first enemy, Derek Carr! He\'s wearing eyeliner, this should be easy.')




derekHealth = 100
riversHealth = 100
while True:
    while True:
        print('Would you like to throw or run?')
        play = input()
        if play == 'throw':
            r1 = random.randint(1,30)
            if r1 <= 21:
                    print ('Pass complete for ' + str(r1) + ' yards! ' + str(derekHealth - r1) + ' yards to go!')
                    derekHealth = derekHealth - r1
            if r1 == 22:
                    print ('Pass intercepted!')
            if r1 > 22:
                    print('Pass incomplete!')
        if play == 'run':
            r2 = random.randint(1,13)
            if r2 <= 8:
                print ('Austin Ekeler takes the handoff. You run for only ' + str(r2) + ' yards. You will not defeat Derek Carr by running the ball without blocking. Someone should tell the Coach! ' +str(derekHealth - r2) + ' yards to go')
                derekHealth = derekHealth - r2
            if r2 == 9:
                print('Melvin Gordon takes the handoff, FUMBLE!')
            if r2 >= 10:
                print ('Austin Ekeler takes the handoff. You run for ' + str(r2) + ' yards. I guess establishing the run really does work! ' +str(derekHealth - r2) + ' yards to go')
                derekHealth = derekHealth - r2
        if derekHealth <= 0:
            print('TOUCHDOWN CHARGERS! FTR')
        break
    while True:
        print('The Raiders are choosing a play...')
        r3 = random.randint(1,10)
        if r3 <= 6:
            print('The Raiders throw the ball.')
            r4 = random.randint(1,30)
            if r4 <= 21:
                print('The raiders have completed the pass for ' + str(r4) + ' yards. ' + str(riversHealth - r4) + ' yards to go!')
                riversHealth = riversHealth - r4
            if r4 == 22:
                print ('You have intercepted the pass!')
            if r4 > 22:
                print ('Pass incomplete!')
        if r3 > 6:
            print('The Raiders have run the ball.')
            r5 = random.randint (1,13)
            if r5 <= 8:
                print ('Josh Jacobs takes the handoff and runs for ' + str(r5) + ' yards. ' +str(riversHealth - r5) + ' yards to go!')
                riversHealth = riversHealth - r5
            if r5 == 9:
                print('Josh jacobs takes the handoff, FUMBLE!')
            if r5 >= 10:
                print('Josh Jacobs takes the handoff and runs for ' + str(r5) + ' yards! ' +str(riversHealth - r5) + ' yards to go')
                riversHealth = riversHealth - r5
        if riversHealth <=0:
            print('TOUCHDOWN RAIDERS!')
        break









    




