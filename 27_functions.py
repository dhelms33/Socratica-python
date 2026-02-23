class Demoman:
    def __init__(self,pipes,sword,stickies):
        self.pipes = pipes
        self.sword = sword
        self.stickies = stickies
    def detonate(self.stickies):
        exploded_stickies = "KABOOM! Exploded " + self.stickies + "stickies."
        return(exploded_stickies)
    def volume_stickies(r, self.stickies):
        v = (4.0/3.0) * math.pi * r**3
        v_stickies = v * self.stickies
        return v_stickies
