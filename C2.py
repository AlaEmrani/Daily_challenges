# my second day challenge

# num ways with 1, 2 steps
def num_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    result = num_ways(n-1) + num_ways(n-2)
    return result


print(num_ways(5))

# num ways with a list of steps
def num_ways_set(n, s):
    if n == 0:
        return 1
    total = 0
    for item in s:
        if n - item >=0:
            total += num_ways_set(n-item, s)
    return total


print(num_ways_set(2, [1,2,3]))

# efficient num ways with DP
def bottom_up_num_ways(n, s):
    if n ==0:
        return 1
    all_num_ways = [None]*(n+1)
    all_num_ways[0] = 1
    for i in range(1, n+1):
        total = 0
        for item in s:
            if i-item >=0:
                total += all_num_ways[i-item]
        all_num_ways[i] = total
    print(all_num_ways)
    return all_num_ways[n]

print(bottom_up_num_ways(5,[1,2]))