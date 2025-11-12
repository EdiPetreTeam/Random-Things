n = 1
n2 = 2
timer = 19 # factorial you want minus 1 ex. !20 = 20 - 1

while timer != 0:
    n = n*n2
    n2 = n2 + 1
    timer = timer - 1
    print(f"number is: {n}")
    print(f"timer is: {timer}")

print(f"number is: {n}")
