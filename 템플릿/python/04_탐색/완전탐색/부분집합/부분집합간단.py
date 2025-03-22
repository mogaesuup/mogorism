nums = [[25, "롯데"], [150, "전통"], [90, "DMZ"], [100, "갈라"], [400, "부산"]]
result = []


def subset(index, path, sums):
    result.append([sums, path])
    for i in range(index, len(nums)):
        subset(i + 1, path + [nums[i]], sums + nums[i][0])


subset(0, [], 80)
for r in sorted(result):
    print(r)
print(len(result))