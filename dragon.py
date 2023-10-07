import random
start=['india','how','today','very beautifull']
middle=['car','wonderfull','tree']
s_last=['cute','bangloore','very happy']
last=['bore','kerala','flower','america is very cold']
player=100
dragon=100
for i in range(20):
    player_a=random.randint(5,20)
    dragon_b=random.randint(5,20)
    print(random.choice(start),random.choice(middle),random.choice(s_last),random.choice(last))
    player=player-player_a
    dragon=dragon-dragon_b
    if player<=0 and dragon<=0:
        if player>dragon:
            print('HP of player =',player)
            print('HP of dragon =',dragon)
            print('player win')
            exit()
        else:
            print('HP of player =',player)
            print('HP of dragon=',dragon)
            print('dragon win')
            exit()
    if player<=0:
            print('HP of player=',player)
            print('HP of dragon =',dragon)
            print('dragon win')
            exit()
    elif dragon<=0:
            print('HP of player=',player)
            print('HP of dragon=',dragon)
            print('player win')
            exit()
    print('HP of player=',player)
    print('HP of dragon=',dragon)

