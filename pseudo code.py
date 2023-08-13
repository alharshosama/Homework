
sample_number = int(input("Number to be reversed: "))
test_number = 0
while(sample_number>0):
    remainder_number = sample_number % 10
    test_number = (test_number * 10) + remainder_number
    sample_number = sample_number//10
print("Value after reverse : {}".format(test_number))

for i in range(1,100):
     if i % 3 == 0 and i % 5 == 0:
       print('FizzBuzz')
     elif i % 3 == 0:
       print('Fizz')
     elif i % 5 == 0:
      print('Buzz')
     else:
      print(i)

      
print("n".join(["Fizz" * (i % 3 == 0) + "Buzz" *(i % 5 == 0) or str(i) for i in range(1, 100)]))