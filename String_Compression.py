import itertools 

## Use the itertools to group the string

def compress(string):
    grouped = ''.join(
            str(len(list(group))) + letter 
            for letter, group in itertools.groupby(string))
    
    ## remove 1 from the compressed string, e.g, 1A would be A
    grouped_final = grouped.strip('1')
    
    ## Print the final string for debugging cases
    print(grouped_final)
    
    ## return the grouped string
    return grouped_final


compress('ABCDDDEFG')
## just for debugging purpose



def solution(s,k):
    shortest = compress(s)
    temp = ''
    ## Keep testing some removed characters to find the shortest compression combination
    for i in range(k,len(s)):
        temp =  compress(s[:i-k]+s[i:])
        if len(temp)< len(shortest):
            shortest = temp          
    return len(shortest) 

## To test the final solution
solution('ABBBCCDDCCC', 3)
