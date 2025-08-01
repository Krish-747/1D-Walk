import random

lenth = 20
default_value = 5000


arraya = [0] * (lenth - int(lenth/2))

for i in range(int(lenth/2)):
    arraya.append(default_value)


def repeat_again(given_array):
    mean = sum(given_array) / len(given_array)

    for value in given_array:
        if abs(value - mean) > mean/10:
            return True

    return False

# array of length 20 with default value 750 initialised


while True:
    newarray = [0] * lenth
    for ind in range(lenth):
        for ball in range(arraya[ind]):
            a = random.randint(0, 1)
            b = arraya[ind]

            if ind == 0:
                if a == 1:
                    newarray[ind + 1] += 1
                else:
                    newarray[ind] += 1
            elif ind == lenth - 1:
                if a == 0:
                    newarray[ind - 1] += 1
                else:
                    newarray[ind] += 1
            else:
                if a == 0:
                    newarray[ind - 1] += 1
                else:
                    newarray[ind + 1] += 1

    arraya = newarray
    print(arraya)

    if not repeat_again(arraya):
        break

