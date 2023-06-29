class Slider():
    def __init__(self,side,rect,Move_speed):

        self.side  = side
        self.rect = rect
        self.move_speed = Move_speed


    def clamp_move(self,dir,constraint):
        if dir == -1:
            self.rect.top -= self.move_speed
        elif dir == 1:
            self.rect.top += self.move_speed

        if self.rect.top <= constraint[0]:
            self.rect.top = constraint[0]
        if self.rect.top + 70 >= constraint[1]:
            self.rect.top = constraint[1] - 70

