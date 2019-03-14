
def executeQuery(query_arr, stack, max_tracker): #keep global maximum
    '''

    :type query_arr: list
    :type stack: list
    :param max_tracker: keeps consecutive maxes
    :type max_tracker: list 
    '''
    if len(max_tracker) == 0:
        max = 0
    else:
        max = max_tracker[-1]

    query_type = query_arr[0]
    if query_type == 1: #append
        el_value = query_arr[1]
        stack.append(el_value)
        if el_value >= max: #keeps duplicates
            max_tracker.append(el_value)    
            
    elif query_type == 2: #remove
        el_value = stack.pop()
        if el_value == max:
            max_tracker.pop()
        
    else: #query_type == 3 #print max
        print(max)
    
    #print("The stack is currently:", stack)
    #print("The max stack is currently:", max_tracker)
    
    return stack, max_tracker

if __name__ == '__main__':
 
    t = int(input())
      
    stack = []
    m = []
  
    for t_itr in range(t):
          
        query = list(map(int, input().rstrip().split()))
        stack, m = executeQuery(query, stack, m)
        
