#left off 4:22
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
    def make_test_tuples():
        empty_tuple = () 
        test1 = ("a", )
        test2 = ("a", "b")
        test3 = ("a", "b", "c")
        return(empty_tuple+test1+test2+test3)
        
        test
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
    obj_instance = TuplesvLists
    tuples_count = obj_instance.get_list_prime()
    print("tuples size ", tuples_count)
    
    #print(dir(sys))
    #print(help(sys.getsizeof))
    