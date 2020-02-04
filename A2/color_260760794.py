Sock,C,K=map(int, input().split())
colours=sorted(list(map(int, input().split())))


if Sock<=C:
    washers=1
else:
    washers=low=0

    while True:
        if low>=S:
            break
        
        high=C+low-1
 
        if high>=Sock:
            high=Sock-1

        while high>=low:
            if K>=(colours[high]-colours[low]):
                low=high+1
                washers=washers+1
                break

            high=high-1




print(washers)