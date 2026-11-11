# def power(base, exp):
#     """Return the area of a width x height rectangle."""
#     res = 1
#     for _ in range(exp):
#         res = res * base

#     return res

# n = int(input())

# for _ in range(n):
#     i = list(map(int, input().split()))

#     print(power(i[0], i[1]))

# def count_vowels(text):
#     """triple-quoted""" 
#     edited_text = text.lower()
#     count = 0

#     for i in edited_text:
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#             count += 1
#     return count

# n = int(input())

# for _ in range(n):
#     text = input()
#     print(count_vowels(text))

# def double(x):
#     """return twice"""
#     return 2*x

# def square(x):
#     """return double"""
#     return x**2

# def negate(x):
#     """return negative"""
#     return -x

# def apply_to_all(func, nums):
#     """return func"""
#     new_list = []

#     for i in nums:
#         new_list.append(func(i))

#     return new_list

# nums = list(map(int, input().split()))

# q = int(input())

# for _ in range(q):
#     name = input()
    
#     if name == "double":
#         res = apply_to_all(double, nums)
#         print(*res)
#     elif name == "square":
#         res = apply_to_all(square, nums)
#         print(*res)
#     elif name == "negate":
#         res = apply_to_all(negate, nums)
#         print(*res)

# import string

# def count_kinds(text):
#     """return count kinds"""
#     letters = 0
#     digits = 0
#     punctuations = 0
#     others = 0

#     for i in text:
#         if i in string.ascii_letters:
#             letters += 1
#         elif i in string.digits:
#             digits += 1
#         elif i in string.punctuation:
#             punctuations += 1
#         else:
#             others += 1

#     return [letters, digits, punctuations, others]

# n = int(input())

# for _ in range(n):
#     text = input()

#     res = count_kinds(text)
#     print(f"letters={res[0]} digits={res[1]} punctuation={res[2]} other={res[3]}")

# import math

# def circle_area(r):
#     """return circle area"""
#     return math.pi * math.pow(r,2)

# def circumference(r):
#     """return circumference"""
#     return 2 * math.pi * r

# n = int(input())

# for _ in range(n):
#     r = float(input())

#     ca = circle_area(r)
#     cf = circumference(r)

#     print(f"{ca:.2f} {cf:.2f}")

n = int(input())

found = 0

is_prime = False

for d in range (2, n):
    if n % d == 0:
        found = d
        is_prime = False
        break
    else:
        is_prime = True
    
if is_prime:
    print("prime")
else:
    print(f"divisible by {found}")

