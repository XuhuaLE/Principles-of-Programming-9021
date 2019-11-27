from collections import deque

# Insert your code here
import sys

N = input('Input final configuration: ').replace(' ', '')
test_1 = {'1', '2', '3', '4', '5', '6', '7', '8'}
test_2 = set()
for i in N:
    test_2.add(i)
if len(N) != 8 or test_1 != test_2:
    print('Incorrect configuration, giving up...')
    sys.exit()

def row_exchange(S1):
    S2 = S1[::-1]
    return S2

def right_circular_shift(S1):
    S2 = S1[3]+ S1[0:3]+ S1[5:]+ S1[4]
    return S2

def middle_clockwise_rotation(S1):
    S2 = S1[0] + S1[6] + S1[1] + S1[3] + S1[4] + S1[2] + S1[5] + S1[7]
    return S2

initial = '12345678'
steps = 0
states = set([initial])
if initial == N:
    pass
else:
    while True:
        steps += 1
        temp = []
        A = [row_exchange(i) for i in states]
        B = [right_circular_shift(j) for j in states]
        C = [middle_clockwise_rotation(k) for k in states]
        D = A + B + C
        temp.append(D)
        for e in temp[-1]:
            states.add(e)
        if N in states:
            break

if steps == 0:
    print('0 step is needed to reach the final configuration.')
else:
    print(f'{steps} steps are needed to reach the final configuration.')
