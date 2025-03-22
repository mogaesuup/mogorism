def SUBSET(nums):
    result = []

    def subset(index, path):
        result.append(path)
        for i in range(index, len(nums)):
            subset(i+1, path+[nums[i]])

    subset(0, [])
    return result


result = SUBSET([1, 2, 3])
print(result)
