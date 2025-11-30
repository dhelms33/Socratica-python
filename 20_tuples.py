#left off 2:22
import timeit
class TuplesvLists:
    def __init__(self):
        pass
    
    def get_tuple_squares():
        perfect_squares = (1,4,9,15,25,36)
        return perfect_squares
    def get_list_prime():
        prime_numbers = [2,3,5,7,11,13,17]
        return prime_numbers
    def iterator_ex_ps(perfect_squares):
        for item in perfect_squares:
            return("Prime: ", item)
    def iterator_ex_l(prime_numbers):
        for item in prime_numbers:
            return("Prime numbers:", item)
    #print("List methods")
    #print("tuples methods")
    #lists occupy more memory than tuples
    #tuples are immutable
    def get_time_list():
        list_test = timeit.timeit(stmt = "[1,2,3,4,5]", number=10000000)
        return list_test
    def get_time_tuple():
        tuple_test = timeit.timeit(stmt = "(1,2,3,4,5)", number = 10000000)
        return tuple_test
if __name__ == "__main__":
    
    
    #print(dir(sys))
    #print(help(sys.getsizeof))
    