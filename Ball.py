# from Ball import Ball
import random
class Ball():
    def __init__(self,radius,rect,x_v,y_v):
        self.rect= rect
        self.radius = radius
        self.x_v = x_v
        self.y_v = y_v

        self.centre_pos = (rect.left+radius,rect.top+radius)


    def make_move(self,move_of):
   
        self.rect.top += self.y_v
        self.rect.left += self.x_v
        self.centre_pos = (self.rect.left+self.radius,self.rect.top+self.radius)


        if self.rect.top <= -10:
            # print("EEEEEEEEEEEEEEEEEE")
            self.rect.top = 695
            if move_of == 1 and self.rect.left <= 300:
                self.rect.left = 900 - self.rect.left - 300
            else:
                self.rect.left = 900 - self.rect.left

            if move_of == -1 and self.rect.left >= 600:
                self.rect.left = 900 - self.rect.left + 300
            else:
                self.rect.left = 900 - self.rect.left
        elif self.rect.top >= 710:
            self.rect.top = 3

            if move_of == 1 and self.rect.left <= 300:
                self.rect.left = 900 - self.rect.left - 300
            else:
                self.rect.left = 900 - self.rect.left

            if move_of == -1 and self.rect.left >= 600:
                self.rect.left = 900 - self.rect.left + 300
            else:
                self.rect.left = 900 - self.rect.left

    def check_win(self):
        if self.rect.left <=0:
            return 1
        elif self.rect.left >=900:
            return -1
    def collision_detect(self,slides):
        for i in slides:
            if self.rect.colliderect(i.rect):
                self.x_v = -self.x_v
                self.y_v = self.y_v + random.randint(-2,2)
                return i.side
