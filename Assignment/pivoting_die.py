from math import sqrt

while True:
    N = input('Enter the desired goal cell number: ')
    if N.isdigit():
        N = int(N)
        if N >= 1:
            break
        else:
            print('Incorrect value, try again')
    else:
        print('Incorrect value, try again')

def right(L):
    new_L = [7 - L[2]] + [L[1]] +[L[0]]
    return new_L
    
def forwards(L):
    new_L = [L[1]] + [7 - L[0]] +[L[2]]
    return new_L

def left(L):
    new_L = [L[2]] + [L[1]] +[7 - L[0]]
    return new_L

def backwards(L):
    new_L = [7 - L[1]] + [L[0]] +[L[2]]
    return new_L

if sqrt(N) - int(sqrt(N)) == 0 and (int(sqrt(N)) - 1) % 6 == 0:
    die = [3, 2, 1]
elif sqrt(N) - int(sqrt(N)) == 0 and (int(sqrt(N)) - 3) % 6 == 0:
    die = [2, 1, 3]
elif sqrt(N) - int(sqrt(N)) == 0 and (int(sqrt(N)) - 5) % 6 == 0:
    die = [1, 3, 2]
else:
    a = int(sqrt(N))
    if a % 2 == 1:
        n = a
    else:
        n = a - 1
    A = n ** 2
    B = (n + 2) ** 2
    mid = (A + B) // 2
    if (n - 1) % 6 == 0:
        die_A = [3, 2, 1]
        die_B = [2, 1, 3]
    elif (n - 3) % 6 == 0:
        die_A = [2, 1, 3]
        die_B = [1, 3, 2]
    elif (n - 5) % 6 == 0:
        die_A = [1, 3, 2]
        die_B = [3, 2, 1]
    if N == mid:
        die = right(die_A)
        for _ in range(n):
            die = backwards(die)
        for _ in range(n + 1):
            die = left(die)
    elif N > mid:
        temp1 = (mid + B) // 2
        if N == temp1:
            die = left(die_B)
            for _ in range(n):
                die = left(die)
        if N > temp1:
            die = left(die_B)
            for _ in range(B - N - 1):
                die = left(die)
        if N < temp1:
            die = left(die_B)
            for _ in range(n):
                die = left(die)
            for _ in range(temp1 - N):
                die = backwards(die)
    elif N < mid:
        temp2 = (A + mid) // 2
        if N == A + 1:
            die = right(die_A)
        elif A + 1 < N <= temp2:
            die = right(die_A)
            for _ in range(N - A - 1):
                die = backwards(die)
        elif N > temp2:
            die = right(die_A)
            for _ in range(n):
                die = backwards(die)
            for _ in range(N - temp2):
                die = left(die)

print(f'On cell {N}, {die[0]} is at the top, {die[1]} at the front, and {die[2]} on the right.')

