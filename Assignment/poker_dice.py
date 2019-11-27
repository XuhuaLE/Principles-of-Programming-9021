from random import randint

cards = {0 : 'Ace', 1 :'King', 2 : 'Queen', 3 : 'Jack', 4 : '10', 5 : '9'}
values = {'Ace' : 0, 'King' : 1, 'Queen' : 2, 'Jack' : 3, '10' : 4, '9' : 5}

def play():
    numbers_1 = [randint(0, 5) for _ in range(5)]
    numbers_1 = sorted(numbers_1)
    roll_1 = [cards[i] for i in numbers_1]
    a = ''
    for e in roll_1:
        a += e
        a += ' '
    print('The roll is: ', end = '')
    print(a[:-1])
    roll_type(roll_1)
    while True:
        second = input('Which dice do you want to keep for the second roll? ').split()
        if second == ['All'] or second == ['all']:
            print('Ok, done.')
            return
        if second == '':
            break
        if not all(roll_1.count(i) >= second.count(i) for i in second) or len(second) > 5:
            print('That is not possible, try again!')
        if all(roll_1.count(i) >= second.count(i) for i in second) and len(second) <= 5:
            break
    if all(roll_1.count(i) == second.count(i) for i in roll_1):
        print('Ok, done.')
        return
    if second == '':
        temp = [randint(0, 5) for _ in range(5)]
        numbers_2 = sorted(temp)
        roll_2 = [cards[i] for i in numbers_2]
        a = ''
        for e in roll_2:
            a += e
            a += ' '
        print('The roll is: ', end = '')
        print(a[:-1])
        roll_type(roll_2)
    else:
        temp = [randint(0, 5) for _ in range(5 - len(second))]
        second = [values[i] for i in second]
        second.extend(temp)
        numbers_2 = sorted(second)
        roll_2 = [cards[i] for i in numbers_2]
        a = ''
        for e in roll_2:
            a += e
            a += ' '
        print('The roll is: ', end = '')
        print(a[:-1])
        roll_type(roll_2)
    while True:
        third = input('Which dice do you want to keep for the third roll? ').split()
        if third == ['All'] or third == ['all']:
            print('Ok, done.')
            return
        if third == '':
            break
        if not all(roll_2.count(i) >= third.count(i) for i in third) or len(third) > 5:
            print('That is not possible, try again!')
        if all(roll_2.count(i) >= third.count(i) for i in third) and len(third) <= 5:
            break
    if all(roll_2.count(i) == third.count(i) for i in roll_2):
        print('Ok, done.')
        return
    if third == '':
        temp = [randint(0, 5) for _ in range(5)]
        numbers_3 = sorted(temp)
        roll_3 = [cards[i] for i in numbers_3]
        a = ''
        for e in roll_3:
            a += e
            a += ' '
        print('The roll is: ', end = '')
        print(a[:-1])
        roll_type(roll_3)
    else:
        temp = [randint(0, 5) for _ in range(5 - len(third))]
        third = [values[i] for i in third]
        third.extend(temp)
        numbers_3 = sorted(third)
        roll_3 = [cards[i] for i in numbers_3]
        a = ''
        for e in roll_3:
            a += e
            a += ' '
        print('The roll is: ', end = '')
        print(a[:-1])
        roll_type(roll_3)
    
def roll_type(L):
    num = {}
    for i in L:
        num[i] = L.count(i)
    counts = []
    for v in num.values():
        counts.append(v)
    if L == ['Ace', 'King', 'Queen', 'Jack', '10'] or L == ['King', 'Queen', 'Jack', '10', '9']:
        print('It is a Straight')
    if 5 in counts:
        print('It is a Five of a kind')
    elif 4 in counts:
        print('It is a Four of a kind')
    elif 3 in counts and 2 in counts:
        print('It is a Full house')
    elif 3 in counts:
        print('It is a Three of a kind')
    elif counts.count(2) == 2:
        print('It is a Two pair')
    elif counts.count(2) == 1:
        print('It is a One pair')
    else:
        print('It is a Bust')

def simulate(num):
    Five_of_a_kind = 0
    Four_of_a_kind = 0
    Full_house = 0
    Straight = 0
    Three_of_a_kind = 0
    Two_pair = 0
    One_pair = 0
    for i in range(num):
        numbers = [randint(0, 5) for _ in range(5)]
        numbers = sorted(numbers)
        roll = [cards[e] for e in numbers]
        Dict = {}
        for c in roll:
            Dict[c] = roll.count(c)
        counts = []
        for v in Dict.values():
            counts.append(v)
        if roll == ['Ace', 'King', 'Queen', 'Jack', '10'] or roll == ['King', 'Queen', 'Jack', '10', '9']:
            Straight += 1
        if 5 in counts:
            Five_of_a_kind += 1
        elif 4 in counts:
            Four_of_a_kind += 1
        elif 3 in counts and 2 in counts:
            Full_house += 1
        elif 3 in counts:
            Three_of_a_kind += 1
        elif counts.count(2) == 2:
            Two_pair += 1
        elif counts.count(2) == 1:
            One_pair += 1
    A = Five_of_a_kind / num * 100
    B = Four_of_a_kind / num * 100
    C = Full_house / num * 100
    D = Straight / num * 100 
    E = Three_of_a_kind / num * 100
    F = Two_pair / num * 100
    G = One_pair / num * 100
    print(f'Five of a kind : {A:.2f}%')
    print(f'Four of a kind : {B:.2f}%')
    print(f'Full house     : {C:.2f}%')
    print(f'Straight       : {D:.2f}%')
    print(f'Three of a kind: {E:.2f}%')
    print(f'Two pair       : {F:.2f}%')
    print(f'One pair       : {G:.2f}%')
