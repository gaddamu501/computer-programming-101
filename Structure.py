count = int(input("How many numbers? "))
nums = []
for i in range(count):
    num = int(input("Enter a number: "))
    nums.append(num)
if len(nums) < 2:
    print("Need at least 2 numbers")
else:
    nums.sort()
    nums.reverse()
    print("Second largest:", nums[1])