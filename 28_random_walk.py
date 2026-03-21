class Walking:
    def random_walk(n):
        """Return coordinate after n block random walk"""
        x = 0
        y = 0
        for i in range(n):
            step = random.choice(['N','S','E','W'])
            if step == 'N':
                y +=1
            elif step == 'S':
                x += 1
            elif step == 'E':
                x -=1
            else:
                y-=1
            #TODO implement elif
        return step