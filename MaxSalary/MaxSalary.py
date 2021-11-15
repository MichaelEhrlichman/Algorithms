
n = int(input())
nums = [int(x) for x in input().split()]

ans = []
while nums:
    maxDigit = nums[0]
    for num in nums[1:]:
        if str(num)+str(maxDigit) >= str(maxDigit)+str(num):
            maxDigit = num
    ans.append(maxDigit)
    nums.remove(maxDigit)

print(''.join([str(i) for i in ans]))
