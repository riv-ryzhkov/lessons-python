# from typing import List, Tuple
#
#
# def count_chains(circles: List[Tuple[int, int, int]]) -> int:
#     res = []
#     c = 0
#     for i in range(len(circles)):
#         res.append(0)
#         for j in range(len(circles)):
#             distance = ((circles[i][0] - circles[j][0])**2 + (circles[i][1] - circles[j][1])**2)**(1/2)
#             if distance < (circles[i][2] + circles[j][2]) and not ((circles[i][0] == circles[j][0]) and (circles[i][1] == circles[j][1])):
#                 res[i] += 1
#
#     for k in res:
#         if k == 0:
#             c += 1
#     r = c + (len(res) - c)//2
#     if c == 0: r = 1
#     print('res=', res)
#     print('c=', c)
#     print('r=', r)
#     return r
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
#     assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
#     assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
#     assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
#     assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
#     assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
#     assert count_chains([[1,3,1],[2,2,1],[4,2,1],[5,3,1],[3,3,1]]) == 1, 'negative coordinates'
#     print("Coding complete? Click 'Check' to earn cool rewards!")