print("Even Numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("\nOdd Numbers:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
sum_even = 0
sum_odd = 0
count_even = 0
count_odd = 0

for i in range(1, 21):
    if i % 2 == 0:
        sum_even += i
        count_even += 1
    else:
        sum_odd += i
        count_odd += 1

avg_even = sum_even / count_even
avg_odd = sum_odd / count_odd

print("\nSum of Even Numbers:", sum_even)
print("Sum of Odd Numbers:", sum_odd)

print("\nCount of Even Numbers:", count_even)
print("Count of Odd Numbers:", count_odd)

print("\nAverage of Even Numbers:", avg_even)
print("Average of Odd Numbers:", avg_odd)