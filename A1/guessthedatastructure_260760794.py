#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
lines = sys.stdin.readlines()

k = 0

while k < len(lines):
    n = int(lines[k].strip())
    j = 0
    
    queue = []
    queue_output = []
    
    priority_queue = []
    priority_queue_output = []
    
    stack = []
    stack_output = []
    
    output = []

    while j < n:
        k = k + 1

        tmp = list(map(int, lines[k].strip().split()))
        
        if tmp[0] == 1:
            stack.append(tmp[-1])
            queue.append(tmp[-1])
            priority_queue.append(tmp[-1])
        else:
            stack_output.append(stack.pop())
            
            queue_output.append(queue[0])
            queue.remove(queue[0])
            
            priority_queue_output.append(max(priority_queue))
            priority_queue.remove(max(priority_queue))
            
            output.append(tmp[-1])
        
        j = j + 1
    
    
    
    result = 0
    if output == priority_queue_output:
        result = result + 1
    if output == queue_output:
        result = result + 1
    if output == stack_output:
        result = result + 1

    if result > 1:
        print("not sure")
    elif result == 0:
        print("impossible")
    elif output == queue_output:
        print("queue")
    elif output == stack_output:
        print("stack")
    else:
        print("priority queue")
    
    k += 1




# input = sys.stdin
# while input[0]:
#     n = int(input)
#     stack, s = [], True
#     queue, q = [], True
#     pri_queue, p = [], True
#     input = input[1:]
#     for k in range(n):
#         inputs = input[k].split(" ")
#         if inputs[0] == "1":
#             stack.append(int(inputs[1]))
#             queue.append(int(inputs[1]))
#             pri_queue.append(int(inputs[1]))
#             pri_queue.sort(reverse=True)
#         else:
#             o1 = stack.pop()
#             s = str(o1) == inputs[1]
#             o2 = queue.pop(0)
#             q = str(o2) == inputs[1]
#             o3 = pri_queue.pop(0)
#             p = str(o3) == inputs[1]
    
#     if s+q+p == 0:
#         print("impossible")
#     elif s+q+p > 1:
#         print("not sure")
#     elif s:
#         print("stack")
#     elif q:
#         print("queue")
#     elif p:
#         print("priority queue")
    
#     input = input[n:]
    
    
            
        

