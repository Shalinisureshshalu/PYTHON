# Sum of Digits

T = int(input())  

for _ in range(T):
    N = int(input())   
    total = 0
    while N > 0:
        digit = N % 10       
        total += digit       
        N //= 10             
    print(total)

INPUT: 3
       12345
       31203
       2123

OUTPUT: 15
        9
        8

# Second Largest

T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    nums = [A, B, C]
    nums.sort()
    print(nums[1])

INPUT: 3
120 11 400
10213 312 10
10 3 450

OUTPUT: 120
312
10

# Little Elephant and Candies

def canMakeElephantsHappy(N, C, A):
    total_required = sum(A)
    if total_required <= C:
        return "Yes"
    else:
        return "No"
T = int(input())

for _ in range(T):
    N, C = map(int, input().split())
    A = list(map(int, input().split()))
    print(canMakeElephantsHappy(N, C, A))
  
INPUT: 2 3
1 1
3 7
4 2 2

OUTPUT: Yes
        No

# Movie Weekend

T = int(input())
for _ in range(T):
    n = int(input())   
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    best_index = 0
    best_value = L[0] * R[0]
    best_rating = R[0]
    for i in range(1, n):
        value = L[i] * R[i]
        if (value > best_value) or \
           (value == best_value and R[i] > best_rating) or \
           (value == best_value and R[i] == best_rating and i < best_index):
            best_index = i
            best_value = value
            best_rating = R[i]
    print(best_index + 1)

INNPUT: 2
2
1 2
2 1
4
2 1 4 1
2 4 1 4

OUTPUT: 1
2

# Uncle Johny

def uncleJohnyPosition(N, songs, K):
    uncle_length = songs[K-1]   
    sorted_songs = sorted(songs)
    return sorted_songs.index(uncle_length) + 1
T = int(input())

for _ in range(T):
    N = int(input())
    songs = list(map(int, input().split()))
    K = int(input())
    print(uncleJohnyPosition(N, songs, K))

INPUT:
3
4
1 3 4 2
2
5
1 2 3 9 4
5
5
1 2 3 9 4
1

OUTPUT:
3
4
1

# Buying New Tablet

ef maxTabletArea(N, B, tablets):
    max_area = -1
    for w, h, p in tablets:
        if p <= B:   
            area = w * h
            if area > max_area:
                max_area = area
    return max_area

# Read number of test cases
T = int(input())

for _ in range(T):
    N, B = map(int, input().split())
    tablets = []
    for _ in range(N):
        W, H, P = map(int, input().split())
        tablets.append((W, H, P))
    
    result = maxTabletArea(N, B, tablets)
    if result == -1:
        print("no tablet")
    else:
        print(result)

INPUT:
3
3 6
3 4 4
5 5 7
5 2 5
2 6
3 6 8
5 4 9
1 10
5 5 10

OUTPUT:
12
no tablet
25

# The Minimum Number Of Moves

def min_moves(salaries):
    min_salary = min(salaries)
    moves = sum(w - min_salary for w in salaries)
    return moves
T = int(input())
for _ in range(T):
    N = int(input())
    salaries = list(map(int, input().split()))
    print(min_moves(salaries))

INPUT:
2
3
1 2 3
2
42 42

OUTPUT:
3
0

# Tanu and Head-bob

T = int(input())

for _ in range(T):
    N = int(input())          
    gestures = input().strip()  
    if 'I' in gestures:
        print("INDIAN")
    elif 'Y' in gestures:
        print("NOT INDIAN")
    else:
        print("NOT SURE")

INPUT:
3
5
NNNYY
6
NNINNI
4
NNNN

OUTPUT:
NOT INDIAN
INDIAN
NOT SURE

# Lapindromes

def isLapindrome(s):
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        left = s[:mid]
        right = s[mid:]
    else:
        left = s[:mid]
        right = s[mid+1:]
    return sorted(left) == sorted(right)
T = int(input())
for _ in range(T):
    S = input().strip()
    if isLapindrome(S):
        print("YES")
    else:
        print("NO")

INPUT:
6
gaga
abcde
rotor
xyzxy
abbaab
ababc

OUTPUT:
YES
NO
YES
YES
NO
NO

# Jewels and Stones

T = int(input())   
for _ in range(T):
    J = input().strip()   
    S = input().strip()   
    
    count = 0
    for ch in S:
        if ch in J:
            count += 1
    print(count)

INPUT:
4
abc
abcdef
aA
abAZ
aaa
a
what
none

OUTPUT:
3
2
1
0

# Is it a VOWEL or CONSONANT

 = input().strip()   
if C in ['A', 'E', 'I', 'O', 'U']:
    print("Vowel")
else:
    print("Consonant")


INNPUT: Z
OUTPUT: Consonant

# Squats

t = int(input())
for i in range(0,t):
    x = int(input())
    total_squats = x * 15   
    print(total_squats)

INPUT:
3
1
4
99

OUTPUT:
15
60
1485

# Age Limit

t = int(input())
for i in range(0,t):
    x,y,a = map(int,input().split())
    if a >= x and a < y:
        print("YES")
    else:
        print("NO")

INPUT:
5
21 34 30
25 31 31
22 29 25
20 40 15
28 29 28

OUTPUT:
YES
NO
YES
NO
YES

# Water Consumption

t = int(input())
for i in range(0,t):
    x =  int(input())
    if x >= 2000:
        print("YES")
    else:
        print("NO")

INPUT:
3
2999
1450
2000

OTUPUT:
YES
NO
YES

# Reverse The Number

T = int(input())
for _ in range(T):
    N = input().strip()   
    reversed_N = N[::-1]  
    print(int(reversed_N))

INPUT:
4
12345
31203
2123
2300

OUTPUT:
54321
30213
3212
32

# The Block Game

T = int(input())  
for _ in range(T):
    N = input().strip()  
    if N == N[::-1]:     
        print("wins")
    else:
        print("loses")

INPUT:
3
331
666
343

OUTPUT:
loses
wins
wins

# Lucky Four

t = int(input())
for i in range(t):
    n = input()
    count = 0
    for digit in n:
        if digit == '4':
            count += 1
    print(count)

INPUT:
5
447474
228
6664
40
81

OUTPUT:
4
0
1
1
0

# Small factorials

import math
t = int(input())  
for _ in range(t):
    n = int(input())
    print(math.factorial(n))

INPUT:
4
1
2
5
3

OUTPUT:
1
2
120
6

# Small Factorial

import math
T = int(input())
for _ in range(T):
    N = int(input())
    print(math.factorial(N))

INPUT:
3
3
4
5

OUTPUT:
6
24
120

# Life, the Universe, and Everything

while True:
    n = int(input())
    if n == 42:   
        break
    print(n)

INPUT:
1
2
88
42
99

OUTPUT:
1
2
88

# Ciel and Receipt

menu_prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
T = int(input())  
for _ in range(T):
    p = int(input())
    count = 0
    for price in reversed(menu_prices):
        if p >= price:
            count += p // price
            p = p % price
    print(count)

INPUT:
4
10
256
255
4096

OUTPUT:
2
1
8
2

# Add Two Numbers

t = int(input())
for i in range(0,t):
    a,b = map(int,input().split())
    print(a + b)

INPUT:
3
1 2
100 200
10 40

OUTPUT:
3
300
50

# Find Remainder

t = int(input())
for i in range(0,t):
    a,b = map(int,input().split())
    print(a%b)

INPUT:
3
1 2
100 200
40 15

OUTPUT:
1
100
10

# Number Mirror

N = 321
print(N)

INPUT: 123
OUTPUT: 123

# Enormous Input Test

(n, k) = map(int, input().split())

ans = 0

for i in range(n):
	x = int(input())
	if x % k == 0:
		ans += 1

print(ans)

INPUT:  
7 3
1
51
966369
7
9
999996
11

OUTPUT:
4

# Finding Square Roots

import math
T = int(input())

for _ in range(T):
    N = int(input())
    
    result = math.floor(math.sqrt(N))
    print(result)

INPUT: 3
10
5
10000

OUTPUT:
3
2
100

# First and Last Digit

T = int(input())  
for _ in range(T):
    N = input().strip()   
    first_digit = int(N[0])   
    last_digit = int(N[-1])   
    print(first_digit + last_digit)

INPUT: 3
1234
124894
242323

OUTPUT:
5
5
5

# Sum of Digits

T = int(input())  

for _ in range(T):
    N = int(input())   
    total = 0
    while N > 0:
        digit = N % 10       
        total += digit       
        N //= 10             
    print(total)

INPUT: 3
12345
31203
2123

OUTPUT:
15
9
8

# Gross Salary

t = int(input())
for i in range(t):
    bs = int(input())
    if bs<1500:
        HRA = 10 * bs/100
        DA = 90 * bs/100
        GS = bs + HRA + DA
    else:
        HRA = 500
        DA = 98 * bs/100
        GS = bs + HRA + DA
    print(GS)

INPUT: 3
1203
10042
1312

OUTPUT:
2406.00
20383.16
2624

# Valid Triangles

T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())

    if A + B + C == 180:
        print("YES")
    else:
        print("NO")

INPUT: 3
40 40 100
45 45 90
180 1 1

OUTPUT:
YES
YES
NO

# Grade The Steel

T = int(input())  

for _ in range(T):
    hardness, carbon, tensile = map(float, input().split())

    cond1 = hardness > 50
    cond2 = carbon < 0.7
    cond3 = tensile > 5600

    if cond1 and cond2 and cond3:
        grade = 10
    elif cond1 and cond2:
        grade = 9
    elif cond2 and cond3:
        grade = 8
    elif cond1 and cond3:
        grade = 7
    elif cond1 or cond2 or cond3:
        grade = 6
    else:
        grade = 5

    print(grade)

INPUT: 3
53 0.6 5602
45 0 4500
0 0 0

OUTPUT:
10
6
6

# Id and Ship

T = int(input())   

for _ in range(T):
    ch = input().strip()   

    if ch in ['B', 'b']:
        print("BattleShip")
    elif ch in ['C', 'c']:
        print("Cruiser")
    elif ch in ['D', 'd']:
        print("Destroyer")
    elif ch in ['F', 'f']:
        print("Frigate")

INPUT: 3
B
c
D

OUTPUT:
BattleShip
Cruiser
Destroyer

# Total Expenses

T = int(input())
for _ in range(T):
    quantity, price = map(int, input().split())
    total = quantity * price
    if quantity > 1000:
        total = total * 0.9   
    print(f"{total:.6f}")

INPUT: 3
100 120
10 20
1200 20

OUTPUT:
12000.000000
200.000000
21600.000000

# Mahasena

N = int(input())
weapons = list(map(int, input().split()))
lucky = 0
unlucky = 0
for w in weapons:
    if w % 2 == 0:
        lucky += 1
    else:
        unlucky += 1
if lucky > unlucky:
    print("READY FOR BATTLE")
else:
    print("NOT READY")

INPUT: 1
1

OUTPUT: NOT READY
