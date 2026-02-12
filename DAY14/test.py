"""sECOND Largest ele"""

# def second(arr):
#   first = second = float('-inf')

#   for num in arr:
#     if num > first:
#       second = first
#       first = num
#     elif num > second and num != first:
#       second = num
  
#   return second if second != float('-inf') else None

# print(second([10,30,50,20]))

"""Best timr to buy and sell stack"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


print(max_profit([7,1,5,3,6,4]))

"""Move 0's to end"""

def move_zeroes(arr):
    pos = 0

    for num in arr:
        if num != 0:
            arr[pos] = num
            pos += 1

    for i in range(pos, len(arr)):
        arr[i] = 0

    return arr


print(move_zeroes([0,1,0,3,12]))

"""Max subarray"""

def max_subarray(arr):
    curr = maxi = arr[0]

    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])
        maxi = max(maxi, curr)

    return maxi


print(max_subarray([-2,1,-3,4,-1,2,1]))