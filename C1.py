def num_ways(data):
    memo = [None]*(len(data)+1)
    return last_k_ways(data, len(data), memo)

def last_k_ways(data, k, memo):
    if k == 0:
        return 1
    s = len(data)-k
    if data[s] == 0:
        return 0
    if memo[k] is not None:
        return memo[k]
    result = last_k_ways(data, k-1, memo)
    if k>1 and int(data[s:s+2])<27:
        result += last_k_ways(data, k-2, memo)
    memo[k] = result
    return result

print(num_ways('1111'))