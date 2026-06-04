# PALINDROME

str1 = input()
if str1 == str1[::-1]:
  print("palindrome")
else
  print("not palindrome")
   
INPUT: madam
OUTPUT: plaindrome

# FACTORIAL

n = int(input())
fact = 1
for i in range(1, n + 1):
  fact = fact*i
  print("factorial", fact)

  INPUT: 5
  OUTPUT: factorial 1
          factorial 2
          factorial 6
          factorial 24
          factorial 120

# Amstrong

 a = int(input())
 length = len(str(a))
 s = 0
 t = a
 while(t>0):
  d = t%10
  s += d**length
  t = t//10
 if(s==a):
  print("Amstrong")
 else:
  print("Not an amstrong")

  INPUT: 150
  OUTPUT: Amstrong

  # PRIME NUMBER

for num in range(1, 50):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

OUTPUT:
1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47

# LARGEST TWO NO

a = int(input())
b = int(input())
if a>b:
  print("A is a largest Number")
else:
  print("B is a largest Number")

INPUT: 4
       7

OUTPUT: B is a largest Number

# FAHRENHET TO CELSIUS

F = float(input("Enter temperature of fahrenhet"))
C = (F-32)*5/9
print(C)

INPUT:Enter temperature of fahrenhet 123.5
OUTPUT: 50.833333333333336

# CELSIUS TO FAHRENHET

c = float(input("Enter temperature of celsius"))
f = (c*9/5)+32
print(f)

INPUT: Enter temperature of celsius 234.5
OUTPUT: 454.1

# THREE NO AVERAGE

a = int(input())
b = int(input())
c = int(input())
d = (a+b+c)/3
print(d)

INPUT: 20
       30
       40
OUTPUT: 30.0

#swapping method

a = int(input())
b = int(input())
a, b = b, a
print("After swapping")
print("a =", a)
print("b =", b)

INPUT: 10
       20
OUTPUT: After swapping a = 20 b = 10

#vowels

a = input()
vowels = "aeiouAEIOU"
for i in a:
  if i in vowels:
    print(i)

INPUT: butterfly
OUTPUT: u e

# FIND LARGEST AND SAMMLEST NUMBER
n = [3, 17, 2, 9, 7, 65, 92]

smallest = min(n)
largest = max(n)

print("Smallest number:", smallest)
print("Largest number:", largest)

OUTPUT: Smallest number: 2
        Largest number: 92

# calculate operators

a = int(input())
b = int(input())
print("Addition:", a+b)
print("Subraction:", a-b)
print("multiplication:", a*b)
print("division:", a/b)

INPUT: 89
       11
OUTPUT: Addition: 100
        Subraction: 78
        multiplication: 979
        division: 8.090909090909092

# GCD AND LCM

from ast import Yield
a = int(input())
b = int(input())
x = a
y = b
while y != 0:
  x, y = y, x % y
  gcd = x
  lcm = (a*b)
  print("GCD is:", gcd)
  print("LCM is:", lcm)

INPUT: 12
       18
OUTPUT: GCD is: 18
        LCM is: 216
        GCD is: 12
        LCM is: 216
        GCD is: 6
        LCM is: 216

# CHECK NO POSITIVE, NEGATIVE, ZERO

a = int(input())
if a > 0:
  print("positve")
elif a < 0:
  print("negative")
else:
  print("zero")

INPUT: 76
OUTPUT: positive

# LEAP YEAR

a = int(input())
if a % 4 == 0:
  print("leap year")
else:
  print("not leap year")

INPUT: 2026
OUTPUT: not leap year

# EVEN AND ODD NUMBER

a = int(input())
if a % 2 == 0:
  print("even number")
else:
  print("odd number")

INPUT: 8448
OUTPUT: even number

#ANNAGRAM

s1 = input()
s2 = input()
if sorted (s1) == sorted (s2):
  print("anagram")
else:
  print("not anagram")

INPUT: listen  silent
OUTPUT: anagram

#NUMBER PATTEN

for i in range(1,6):
  for j in range(1, i+1):
    print(j,end =" ")
  print()

OUTPUT:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

# STAR PATTEN

n = 6
for i in range(n):
  print(" " * i + "*" * (n - i))

OUTPUT:
******
 *****
  ****
   ***
    **
     *

# DIAMOND PATTEN

n = 4
for i in range(1, n + 1):
  print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
  print(" " * (n - i) + "* " * i)

OUTPUT:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

# HALF DIAMOD

n = 5
for i in range(1, n + 1):
  print(" " * (n - i) + "* " * i)

OUTPUT:
   *
   * *
  * * *
 * * * *
* * * * *

# FIND 3 LARGEST NO WITHOUT USING IF ELSE

a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))


INPUT: 8
       67
       89
OUTPUT: 89.

# CHECK ANAGRAM WITHOUT SORTED

s1 = input()
s2 = input()
if len(s1) == len(s2):
  for i in s1:
    if i not in s2:
      print("Not anagram")
      break

  else:
      print("Anagram")
else:
    print("not anagram")

INPUT: dog
god
OUTPUT: not anagram

# CHECKD IF NO IS POWER OF 2 WITHOUT LOOP

n = int(input())
if n > 0 and (n & (n - 1)) == 0:
  print("power of 2")
else:
  print("not power of 2")

INPUT: 8
OUTPUT: power of 2

# Right Angled Triangle Pattern

for i in range(1, 6):
    print("*" * i)

OUTPUT:
*
**
***
****
*****

# Square Pattern of Stars

for _ in range(4):
    print("****")

OUTPUT:
****
****
****
****

# palindrome remove any letter in the word

s = input("Enter the message: ")
def is_palindrome(text):
    return text == text[::-1]
for i in range(len(s)):
    new_s = s[:i] + s[i+1:]
    if is_palindrome(new_s):
        print("YES")
        break
else:
    print("NO")

INPUT: ADDA
OUTPUT: YES

# MISSING NO

n = int(input())
sensors=set(map(int,input().split()))
expected=n*(n+1)//2
actual=sum(sensors)
print (expected -actual)

INPUT: 5
1 2 4 5
OUTPUT: 3

# DUPLICATE FOUND

products = input().split()
for p in products:
    if products.count(p) > 1:
        print("Duplicate Found")
        break
else:
    print("No Duplicate")

INPUT: 5 7 8 9
OUTPUT: No Duplicate
