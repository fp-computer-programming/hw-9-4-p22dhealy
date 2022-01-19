#author: DMH 1/18/22

def products(num, value):
    for i, v in enumerate(num):
        num[i] = v * value
        v *= value
    return num

print(products([40, 10], 1))