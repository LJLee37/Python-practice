nums = list(map(int,input().split()))
avg = 0
for i in nums:
    avg += i
print(avg/len(nums))