import random

length_of_array = 20
default_value = 5000


og_array = [0] * (length_of_array - int(length_of_array/2))

for i in range(int(length_of_array/2)):
    og_array.append(default_value)


def repeat_again(given_array):
    mean = sum(given_array) / len(given_array)

    for value in given_array:
        if abs(value - mean) > mean/10:
            return True

    return False

# array of length 20 with default value 750 initialised


while True:
    newarray = [0] * length_of_array
    for ind in range(length_of_array):
        for ball in range(og_array[ind]):
            a = random.randint(0, 1)
            b = og_array[ind]

            if ind == 0:
                if a == 1:
                    newarray[ind + 1] += 1
                else:
                    newarray[ind] += 1
            elif ind == length_of_array - 1:
                if a == 0:
                    newarray[ind - 1] += 1
                else:
                    newarray[ind] += 1
            else:
                if a == 0:
                    newarray[ind - 1] += 1
                else:
                    newarray[ind + 1] += 1

    og_array = newarray
    print(og_array)

    if not repeat_again(og_array):
        break

