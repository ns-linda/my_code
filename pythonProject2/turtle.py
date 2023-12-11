







# def finalPosition(move):
#     l = len(move);
#     countUp, countDown = 0, 0;
#     countLeft, countRight = 0, 0;
#
#     # traverse the instruction string
#     # 'move'
#     while move !== Q:
#
#         # for each movement increment
#         # its respective counter
#         if (move == 'U'):
#             countUp += 1;
#
#         elif (move == 'D'):
#             countDown += 1;
#
#         elif (move == 'L'):
#             countLeft += 1;
#
#         elif (move == 'R'):
#             countRight += 1;
#
#         elif (move == 'Q'):
#             break
#
#             # required final position of robot
#     print("Final Position: (", (countRight - countLeft),
#           ", ", (countUp - countDown), ")");
#
#
# # Driver program to test above
# if __name__ == '__main__':
#     move = input("\nËnter L or R or M\n")
#     finalPosition(move);