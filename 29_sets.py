class Jojo:
    def __init__(self, volume, name):
        self.volume = volume
        self.name = name
    
    def create_set_manga():
        """ Creates a set of manga for JJBA """
        manga = set()
        #dir(manga) provides a reminder on how to use set
        manga.add("Stell Ball Run")
        manga.add(True)
        manga.add("Volume")
        manga.add(1)
        manga.remove(1)
        #.remove can throw an error if object not in set
        manga.discard(34)
        #does not return anything
        #can add different elements
        #sets doesn't order elements, doesn't contain duplicates
        #len(manga)
        #help(manga.remove)
        #can remove elements
        #2:46
        return manga
    
    def create_set_anime():
        anime = set([1, True, "Phantom Blood", "Volume"])
        anime_copy = set([2, True, "Battle Tendency"])
        anime_copy.clear()
        return anime
    def create_union():
        obj_init = create_set_manga()
        obj_2_init = create_set_anime()
        return obj_init.union(obj_2_init)
    def create_intersection():
        obj_init = create_set_manga()
        obj_2_init = create_set_anime()
        return obj_init.intersection(obj_2_init)
    def test_cases():
        obj_init = create_set_manga()
        obj_2_init = create_set_anime()
        test_1 = 2 in obj_init
        return test_1
    
    