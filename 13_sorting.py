class Earth:
    #stopped 1:46
    def __init__(self, metals, metals_tuple):
        self.metals = ["Beryllium", "Magnesium", "Calcium"]
        self.metals_tuple = ("Beryllium", "Magnesium", "Calcium")
        #stored in immutable tuple will cause error
    def sorter(self, metals):
        sorted_metals = metals.sort()
        return sorted_metals
    