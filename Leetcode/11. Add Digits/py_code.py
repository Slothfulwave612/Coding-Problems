## Add Digits

def add_digit(num):
    while num > 9:
        num = [int(x) for x in str(num)]
        num = sum(num)
    return num

num = 38
print(add_digit(num))