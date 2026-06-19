#!/usr/bin/env python3
import sys
numbers = [float(x) for x in sys.argv[1:]]
count = len(numbers)
total = sum(numbers)
mean = total / count
sorted_nums = sorted(numbers)
if count%2==1:
    median = sorted_nums[count // 2]
else:
    middle1=sorted_nums[count // 2 - 1]
    middle2=sorted_nums[count // 2]
    median=(middle1 + middle2) / 2
freq = {}
for num in numbers:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
max_freq = max(freq.values())
mode=[]
for num, count_value in freq.items():
    if (count_value==max_freq):
        mode.append(num)
variance=sum((x-mean)**2 for x in numbers)/count
std_dev=variance ** 0.5
print("Count:", count)
print("Sum:", total)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("\nBar Chart:")
for num in numbers:
    print(int(num) * "#")
