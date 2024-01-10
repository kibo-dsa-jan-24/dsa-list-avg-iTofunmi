from operator import add
from functools import reduce

class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.total = reduce(add, lst)
    
    def __str__(self):
        return str(self.lst)

    def add(self, num):
        self.lst.append(num)
        self.total += num
        
    def compute_avg(self):
        total = 0
        for num in self.lst:
            total += num
        return total / len(self.lst)

    def compute_avg_faster(self):
        # implement this method
        return self.total/len(self.lst)


# # Create an instance of ListAverage
# test_loop = ListAverage([1,2,3])
# print(test_loop.compute_avg())

# test_loop.add(6)
# print(test_loop) 

# test_reduce = ListAverage([1, 2, 3, 4])
# print(test_reduce.compute_avg_faster())

# test_reduce.add(5)
# print(test_reduce)
# print(test_reduce.compute_avg_faster())











# class ListAverage:
#     def __init__(self, lst):
#         self.lst = lst.copy()

#     def add(self, num):
#         self.lst.append(num)

# # Create an instance of ListAverage
# my_list_average = ListAverage([1, 2, 3, 4, 5])

# # Add a number to the list
# my_list_average.add(6)

# # Print the updated list
# print(my_list_average.lst)


