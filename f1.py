# def find_maxi_index(a):
#     maxi = a[0]
#     index = 0
#     k = 0
#     ind = []
#     for number in a:     
#         if number > maxi:
#             maxi = number
#     for number in a:
#         index += 1
#         if maxi == number:  
#             ind += [index - 1]    
#     for every in ind:
#         k += 1
#     if k == 1:
#         return ind[0]    
#     else:
#         return ind[-2]           
# print(find_maxi_index([1, 2, 3, 4, 5]))


# def find_median(a, b, c):
#     if a > b:
#         if a < c:
#             return a
#         elif b > c:
#             return b
#         else:
#             return c
#     else:
#         if a > c:
#             return a
#         elif b < c:
#             return b
#         else:
#             return c
# print(find_median(7, 2, 1))




# def secondMax(list):
#     maximum = 0
#     second_max = list[0]
#     index = 0  
#     for x in list:
#         index += 1
#         if x > maximum:
#             second_max = maximum 
#             maximum = x 
#         elif x > second_max and x != maximum:
#             second_max = x
#             second_maxindex = index
#     return second_maxindex - 1
        
# print(secondMax([15, 6, 1, 10, 13, 2, 3, 5]))


# def findSimilar(a, b, c):
#     if a == b:
#         if b == c:
#             return 3
#         else:
#             return 2
#     else:
#         if b == c:
#             return 2
#         elif a == c:
#             return 2
#         else:
#             return 0
               
# print(findSimilar(1, 2, 0))


    