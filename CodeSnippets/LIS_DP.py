# This function extracts the longest increasing and decreasing subsequences from
# a sequence of integers.
# The function takes a list of integers and returns two lists of integers 
# containing the longest subsequences. If it gets passed an empty list, None,
# or something other then an integer list, the function returns two times None.
#   
# The subsequence length is not necessarily unique, in this case the elements of
# the longest increasing subsequence should be as small as possible, while the 
# elements of the longest decreasing subsequence should be as large as possible.

def get_longest_subsequences(sequence):


    #Longest Increasing Subsequence
    temp_ins=[] 
    lis=[]
    result=[]

    for i in range(len(sequence)):
        temp_ins.append([]) 
    temp_ins[0].append(sequence[0])  

    for i in range(1,len(sequence)):
        for j in range(0,i):
            if sequence[i]>sequence[j]:
                if len(temp_ins[i])<len(temp_ins[j])+1: 
                    temp_ins[i] = temp_ins[j].copy() 
        
        temp_ins[i].append(sequence[i]) 

    maxlenlis = max(len(x) for x in temp_ins ) 
    maxlenListlis=[]
    for a in temp_ins:
        if(len(a)==maxlenlis):
            maxlenListlis.append(a)
            

    sortedmaxlenListlis=sorted(maxlenListlis, key=lambda i: sorted(i, reverse=False), reverse=False)
    if not sortedmaxlenListlis[0]:
       result.append(None)
    else:

       result.append(sortedmaxlenListlis[0])

    #Longest Decreasing Subsequence

    temp_dec=[]
    lds=[]
    for i in range(len(sequence)):
        temp_dec.append([]) 
    temp_dec[0].append(sequence[0])     
            
    for i in range(1,len(sequence)):
        for j in range(0,i):
            if sequence[i]<sequence[j]:
                if len(temp_dec[i]) < len(temp_dec[j]) + 1: 
                    temp_dec[i] = temp_dec[j].copy() 


        temp_dec[i].append(sequence[i]) 

    maxlenlds = max(len(x) for x in temp_dec ) 

    maxlenListlds=[]
    for a in temp_dec:
        if(len(a)==maxlenlds):
            maxlenListlds.append(a)            

    sortedmaxlenListlds=sorted(maxlenListlds, key=lambda i: sorted(i, reverse=True), reverse=True)
    if not sortedmaxlenListlds[0]:
       result.append(None)
    else:

       result.append(sortedmaxlenListlds[0])
    
    return result
