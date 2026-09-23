# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,item):
#         self.stack.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return None
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             return None
#     def is_empty(self):
#         return len(self.stack)==0
#     def size(self):
#         return len(self.stack)
# stack=Stack()
# stack.push(5)
# stack.push(3)

# print(stack.peek())
# print(stack.pop())
# print(stack.size())





# WRITE A PYTHON FUNCTION THAT USES A STACK TO REVERSE A GIVEN LIST.

# def myCode(Arr):
#     stack=[]   # stack initialization
#     for i in Arr:
#         stack.append(i)   #pushing elements into stack
#     reversed_list=[]       #initializing reversed list
#     while stack:
#         reversed_list.append(stack.pop())       #poping elements from stack
#     return reversed_list
# Arr=[1,2,3,4,5,6]
# print(myCode(Arr))




# from collections import deque
# def myCode(player_turn):
#     data_after_each_round=deque(player_turn)
#     for i in range(5):
#         data_after_each_round.rotate(-1)
#         print("Round",i+1,":",list(data_after_each_round))
# player_turn=["player1","player2","player3"]
# myCode(player_turn)




# from collections import deque
# class Queue:
#     def __init__(self):
#         self.queue=deque()
#     def enqueue(self,item):
#         self.queue.append(item)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.popleft()
#         else:
#             return None
#     def peek(self):
#         if not self.is_empty():
#             return self.queue[0]
#         else:
#             return None
#     def is_empty(self):
#         return len(self.queue)==0
#     def size(self):
#         return len(self.queue)
# queue1=Queue()
# queue1.enqueue(10)
# queue1.enqueue(20)
# print(queue1.peek())
# print(queue1.dequeue()) 
# print(queue1.size())




def mult(a,b):
    return a*b
a=2
b=3
print(mult(a,b))