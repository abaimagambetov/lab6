# 1
# import numpy
# l = [1, 2, 3, 4, 5]
# print(numpy.prod(l))


# 2
# s = "KaZaKhStAnI"
# cntu = 0
# cntl = 0
#
# for i in s:
#     if i.isupper():
#         cntu += 1
#     if i.islower():
#         cntl += 1
#
# print("Number of uppercase letters: ", cntu)
# print("Number of lowercase letters: ", cntl)


# 3
# s = "Tnti"
# s = s.lower()
# copy_s = s[::-1]
#
# flag = 0
#
# for i in range(len(s)):
#     if ord(s[i]) != ord(copy_s[i]):
#         flag = 1
#         break
#
# if flag == 1:
#     print("NO")
# else:
#     print("YES")


# 4
# from time import sleep
#
# def delay(t, n):
#     sleep(t / 1000)
#     return pow(n, 0.5)
#
#
# t = 1
# n = 16
# print("Square root of", n, "after", t, "milliseconds is", delay(t, n))


# 5
# t = (1, 2, 3, 4)
# print(all(t))
