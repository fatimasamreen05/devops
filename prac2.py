#2 Write a Python program to generate prime numbers less than 50.
print("Prime numbers less than 50:")

for num in range(2, 50):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
  
