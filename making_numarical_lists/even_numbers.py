#we can als use the range() function tp tell python to skip numbers in a given range
#if you pass a third arguement to range(), python uses that value as a step size when generating numbers...EG--:
#here is how you list even numbers btn 1 and 10

even_numbers = list(range(2,11,2))
print(even_numbers)               #[2, 4, 6, 8, 10]

#in this example, the range() function starts with the value 2 and then adds 2 to that value
#it adds 2 repeatedly until it reaches or passes the end value, 11, and produces the result