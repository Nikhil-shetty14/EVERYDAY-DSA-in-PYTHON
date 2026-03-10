"""Count occurances of Element"""

def count_occ(arr,n,x):
    
    if n == 0:
        return 0

    count = count_occ(arr,n-1,x)

    if arr[n-1] == x:
        return count +1

    return count

arr = [1,2,3,2,2,5]

print(count_occ(arr,len(arr),2))

"""Generate All Subsequence"""

def subsequences(s,current="",index=0):
    if index == len(s):
        print(current)
        return 
    
    subsequences(s,current + s[index],index + 1)

    subsequences(s, current,index + 1)

subsequences("abc")