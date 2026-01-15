import random

difTry = 0
again = 'yes'

name = "Player"
Iwin = 0
ask_money = 'nothing'
Player_win = 0
Max = -2
Try = -10
guess = -2
money = 0

mode = 'nothing'

while mode not in ('easy', 'normal', 'hard', 'costume'):
    mode = input(f' nice to meet you {name} ,now you gone choose the mode.\n there are 4 mods '
                 f'\n -easy-:range 0-10, with 3 chances'
                 f'\n -Normal-:range 0-20 with 3 chances '
                 f'\n -HARD-:range 0-30 with   4 chances '
                 f'\n You also can choose -costume- mode'
                 f'\n so what would you like to choose? \n ').lower()
    if mode == 'easy':
        Max = 10
        Try = 3
    elif mode == 'normal':
        Max = 20
        Try = 4
    elif mode == 'hard':
        Max = 30
        Try = 4
    elif mode == 'costume':
        while Max < 2:
            try:
                Max = int(input('it have to be more then 1 ,chose the max distance of my mystery number?\n'))
            except ValueError:
                print('try again')
        while Try < 1:
            try:
                Try = int(input('it should be more then 0, chose how many trys you want to have?\n'))
            except ValueError:
                print('try again')
    else:
        print(f'please {name} print the mode name correctly like in the text above \n')

while again != 'no':
    if again == 'yes':
        guess = -2
        while ask_money != 'yes' and ask_money != 'no':
            ask_money = input('do you want to put money in the game ? yes or no\n').lower()
            if ask_money == 'yes':
                while money < 1:
                    try:
                        money = int(input('it have to be more then 0,how many you invest?\n'))
                    except ValueError:
                        print("try again")

        x = random.randint(0, Max)
        print(f'My number is between 0 and {Max} , you have {Try} tries \n')

        while Try != 0:

            while guess < 0 or guess > Max:
                try:
                    print(f'take a guess, guess need to be between 0 and {Max}:\n')
                    guess = int(input())
                except ValueError:
                    print('try again ,only numbers ')

            Try -= 1
            difTry += 1

            player_guess = guess

            if guess == x:
                print('you guessed right')
                break
            elif guess > x:
                print('too high')
            elif guess < x:
                print('too low')

            guess = -2

        print('the number was ', x)

        if player_guess == x:
            print('you won')
            if ask_money == 'yes':
                print(f'you won {money * 2} money !oo')
            Player_win += 1
        else:
            print('you loose!! ;D Nooooob')
            if ask_money == 'yes':
                print(f'you loosed {money} money! ')
            Iwin += 1

        print(f'I won {Iwin} times ,you won {Player_win} times')

        ask = 'nothing'
        while ask != 'yes' and ask != 'no':
            ask = input('you want to keep play? \n'
                        f' yes or no \n').lower()
        again = ask
        ask_money = 'nothing'
        Try = Try + difTry
        difTry = 0
        guess = -2

print(f'ok see you {name}')


















