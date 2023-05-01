def print_fibonacci(length):
    pass
    list = [0,1]
    if length == 0:
        list.clear()   
    elif length == 1:
        list.remove(1)
    elif length > 2:
        for i in range(length-2):
            list.append(list[-1]+list[-2])
    print(list)
 


    # print(print_fibonacci)

# def print_fibonacci(length):
#     pass
#     fibonacci_sequence = []
#     if length > 0:
#         fibonacci_sequence.append(0)
#         if length > 1:
#             fibonacci_sequence.append(1)
#             if length > 2:
#                 for i in range (2, length):
#                     fibonacci_sequence.append(fibonacci_sequence[i-1]+fibonacci_sequence[i-2])
                

                
    

#     print(fibonacci_sequence)