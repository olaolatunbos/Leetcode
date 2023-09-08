data = [1, 5, 20, 15, 10]

# for each element, what position does it occupy in sorted list
# Highest to Lowest
ranked_data_ = [sorted(data, reverse=True).index(x) + 1 for x in data]

# Lowest to Highest
ranked_data = [sorted(data).index(x) + 1 for x in data]

li = [1,2,3,5]
li.remove(3)
print(li)

