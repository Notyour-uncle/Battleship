class tile:
    def __init__(self):
        self.has_ship = False
        self.been_hit = False

    def set_ship(self):
        self.has_ship = True

    def get_hit(self):
        self.been_hit = True

    def print_self(self, enemy):
        if not enemy:
            if self.has_ship and not self.been_hit:
                print('S|', end='')
            elif not self.has_ship and not self.been_hit:
                print('W|', end='')
            elif self.has_ship and self.been_hit:
                print('X|', end='')
            elif not self.has_ship and self.been_hit:
                print('M|', end='')
        elif enemy:
            if not self.been_hit:
                print('?|', end='')
            elif self.has_ship:
                print('X|', end='')
            elif not self.has_ship:
                print('M|', end='')

    