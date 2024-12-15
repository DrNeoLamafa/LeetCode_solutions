nums = [1,2,3,4,5,6,7]
k = 3
print(nums[-k:])
print(nums[:len(nums)-k])
nums = nums[-k:] + nums[:len(nums)-k]
print(nums)
#not work