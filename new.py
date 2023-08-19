store = {"foo" : [["bar", 1],  ["bar1", 2],  ["bar3", 3], ["bar4", 4], ["bar5", 5]]}
values = store.get("foo", [])
print(values)

def bs(nums, time):
    l, r = 0, len(values) - 1
    while l <= r:
        mid = (l + r) // 2
        if values[mid][1] < time:
            l = mid + 1
        elif values[mid][1] > time:
            r = mid + 1
        else:
            return values[mid][0]
    return -1

print(bs(values, 2))