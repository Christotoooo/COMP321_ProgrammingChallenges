#!/usr/bin/env python
# coding: utf-8

# In[ ]:


input = input()
if input == "":
	# when the input is empty
    print(1)
else:
	# init the original configuration
    current_act = [1,0,0]

    for action in input:
        if action == "A":
            temp_number = current_act[0]
            current_act[0] = current_act[1]
            current_act[1] = temp_number
        elif action == "B":
            temp_number = current_act[1]
            current_act[1] = current_act[2]
            current_act[2] = temp_number
        else: 
        	# "C"
            temp_number = current_act[0]
            current_act[0] = current_act[2]
            current_act[2] = temp_number

    print(current_act.index(1) + 1)


