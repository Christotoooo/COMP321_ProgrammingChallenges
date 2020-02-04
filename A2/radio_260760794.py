def best_so_far(input):
    
    max_so_far_til_now = max_so_far = input[0]
    
    for x in input[1:]:
        max_so_far_til_now = max(x, max_so_far_til_now + x)
        max_so_far = max(max_so_far, max_so_far_til_now)

    return max_so_far


path = int(input().split()[1])

intermediate = list(map(lambda z: int(z) - path, input().split()))

output = best_so_far(intermediate)

print(output)