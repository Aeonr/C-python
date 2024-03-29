sum_a = 0
sum_b = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum_a += i
    else:
        sum_b += i
print("1-100中所有奇数和为:", sum_a)
print("1-100中所有偶数和为:", sum_b)
