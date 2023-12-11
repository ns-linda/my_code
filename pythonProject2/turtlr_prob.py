# def finalPosition():
#     countUp, countDown = 0, 0
#     countLeft, countRight = 0, 0
#
#     while True:
#         data = input(">")
#         if (data == 'U'):
#             countUp += 1
#
#         elif (data == 'D'):
#             countDown += 1;
#
#         elif (data == 'L'):
#             countLeft += 1;
#
#         elif (data == 'R'):
#             countRight += 1;
#
#         elif (data == 'M'):
#             if countLeft !=0:
#                 countLeft -= 1
#                 countRight += 1
#             else:
#                 countRight += 1
#
#         elif data == 'Q':
#             print("Robot shutting down.")
#             break
#         print("Final Position: (", (countLeft ),
#                   ", ", (countRight), ")");
#
# finalPosition()

# import turtle library
import turtle
my_pen = turtle.Turtle()
for i in range(50):
   my_pen.forward(50)
   my_pen.right(144)
turtle.done()