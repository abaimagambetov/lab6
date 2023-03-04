import os

# 1
# print("Only directories: ", [i for i in os.listdir(r'C:\Users\Amir\PycharmProjects\lab6') if os.path.isdir(os.path.join(r'C:\Users\Amir\PycharmProjects\lab6', i))])
# print("Only files: ", [i for i in os.listdir(r'C:\Users\Amir\PycharmProjects\lab6') if not os.path.isdir(os.path.join(r'C:\Users\Amir\PycharmProjects\lab6', i))])
# print("Files and all directories: ", os.listdir(os.getcwd()))


# 2
# print("existence: ", os.access(r'C:\Users\Amir\PycharmProjects\lab6', os.F_OK))
# print("readability: ", os.access(r'C:\Users\Amir\PycharmProjects\lab6', os.R_OK))
# print("writability: ", os.access(r'C:\Users\Amir\PycharmProjects\lab6', os.W_OK))
# print("executability: ", os.access(r'C:\Users\Amir\PycharmProjects\lab6', os.X_OK))


# 3
# if os.access(r'C:\Users\Amir\PycharmProjects\lab6\dirandfiles.py', os.F_OK):
#     print("File name: ", os.path.basename('dirandfiles.py'))
#     print("Directory name: ", os.path.dirname('dirandfiles.py'))
# else:
#     print("Such path does not exist.")


# 4
# f = open('input.txt', 'r')
# x = f.readlines()
# print(len(x))


# 5
# f = open('input.txt', 'w')
# s = input()
# f.write(s)
# f.close()
# f = open('input.txt', 'r')
# print(f.read())


# 6
# if not os.path.exists("letters"):
#     os.mkdir("letters")
#
# for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     with open(i + ".txt", "w") as f:
#         f.writelines(i)


# 7
# first = open('input.txt', 'r')
# second = open('copyinput.txt', 'w')
#
# for i in first:
#     second.write(i)
#
# second = open('copyinput.txt', 'r')
# print(second.read())


# 8
# if os.path.exists('input.txt'):
#     os.remove('input.txt')
#     print("done")
# else:
#     print("there is no such file")
