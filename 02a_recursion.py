class Math:
    def fibonacci(n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == "__main__":
for n in range(1,11):
    print(n, ":", fibonacci(n))