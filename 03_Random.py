import random

#to see methods avaliable we should print dir
#left off 2:59
print(dir(random))

print(help(random.random))

#random(...) method of random.Random instance
    #random() -> x in the interval[0,1) can never return 1 can return 0

#display 10 random numbers from interval [0,1)

class Rando:
    def ten_random():
        numbers = []
        for i in range(10):
            num =  print(random.random())
            numbers.append(num)
        return numbers
    def scale_random():
        numbers_scaled = []
        #Scales a random number
        for i in range(10):
            nums = 4 * random.random() + 3
            numbers_scaled.append(nums)
        return numbers_scaled

if __name__ == '__main__':
    random_instance = Rando()
    print(random_instance.ten_random())