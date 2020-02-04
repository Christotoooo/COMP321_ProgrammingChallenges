#!/usr/bin/env python
# coding: utf-8

# In[ ]:



total_width, n_part = [int(x) for x in input().split()]

parts = [int(x) for x in input().split()] + [total_width]

tous = set()

for part in parts:
    tous.add(part)
    
    for another_part in parts:
        if part != another_part:
            tous.add(abs(part - another_part))

print(" ".join(str(x) for x in sorted(tous)))

