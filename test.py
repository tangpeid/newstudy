import pandas as pd


#
#
#
# def getpos(li):
#     re = []
#     temp = [-1, -1]
#     for i in range(len(l)):
#
#         if i != len(l) - 1:
#             if (l[i] + 1 == l[i + 1]) & (temp[0] == -1):
#                 temp[0] = i
#             if l[i] + 1 != l[i + 1]:
#                 temp[1] = i
#                 re.append(temp)
#                 temp = [-1, -1]
#         else:
#             if temp[0] == -1:
#                 temp[0] = len(l) - 1
#             temp[1] = len(l) - 1
#             re.append(temp)
#     for pos in re:
#         if pos[0] == -1:
#             pos[0] = pos[1]
#     return re
#
# if __name__ == "__main__":
#     l = list([1, 2, 3, 4, 6, 99, 7, 8, 12, 13, 14, 15, 20, 21, 24])
#     pl = pd.Series(l)
#     re = getpos(l)
#     print(re)
#     for pos in re:
#         print(pl[pos[0]:pos[1]+1])
