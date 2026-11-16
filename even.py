def filterEVEN(nums):
    array = []

    for num in nums:
        if num % 2 == 0:
            array.append(num)

    return array

print(filterEVEN([1, 2, 3, 4]))
