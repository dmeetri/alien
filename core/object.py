class Object:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    
    @property
    def get_pos(self):
        return self.x, self.y
    
    def set_pos(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} {self.y}'