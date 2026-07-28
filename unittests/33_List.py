class ListComp:
    def __init__(self, list1, list2, list3):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
    
    def get_comps(self):
        comp1 = [item * 2 for item in self.list1]
        comp2 = [item ** 2 for item in range(1,101)]
        #get remainder when divide by 3
        remainders5 = [item**2 % 5 for item in range(1,101)]
        remainders5_list1 = [item **2 % 5 for item in self.list1]
        return comp1
        