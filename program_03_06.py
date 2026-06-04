# SECOND LARGEST NO WITHOU USING SORTED AND MAX

n = list(map(int,input().split()))
F=s=-1
for i in n:
  if(i>F):
    s=F
    F = i
  elif(i>s):
    s=i
print(s)

INPUT: 12 45 67 23 89 67
OUTPUT: 67

# FIRST UNIQUE CHARACTER IN A STRING

s = "Swiss"
for ch in s:
  if s.count(ch)==1:
    print("firstcharacter",ch)
    break

OUTPUT: firstcharacter 5

# ROTATE LIST BY K POSITIONS:

n = [1, 2, 3, 4, 5]
K = 2
rotated = n[-K:] + n[:-K]
print(rotated)

OUTPUT: [4, 5, 1, 2, 3]

# ODD-EVEN REARRANGEMENT

n = list(map(int,input().split()))
odd = []
even = []

for num in n:
    if num % 2 != 0:
        odd.append(num)
    else:
        even.append(num)

rearrange_n = even + odd
print(rearrange_n)

INPUT: 7 2 5 4 9 8
OUTPUT: [2, 4, 8, 7, 5, 9]

# NESTED LIST PROGRAM

def total(lst):
    s = 0
    for i in lst:
        if isinstance(i, list):
            s += total(i)
        else:
            s += i
    return s

print(total([1,[2,3],[4,[5,6]]]))


OUTPUT: 21

# SPECIAL NUMBER PATTEN

for i in range(1, 101):
  n = str(i)
  if(len(n)==1):
    print(i, end=" ")
  else:
      if(int(n[0]) + int(n[1])) == int(n[0]) * int(n[1]):
        print(i, end=" ")

OUTPUT: 1 2 3 4 5 6 7 8 9 22

# PAIR SUM PROBLEM

arr = [2, 7, 11, 15, 3, 6]
t = 9

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):  
        if arr[i] + arr[j] == t:
            print((arr[i], arr[j]))

OUTPUT: (2, 7) (3, 6)
