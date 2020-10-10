for a in range(1,101):
    if a%10 == 7:
        continue
    elif a//10 ==7:
        continue
    else:
        print(a)
    a+=1

