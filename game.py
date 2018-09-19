import tkinter
import time
import random


class Snake:

    def __init__(self):
        self.body = [[200, x] for x in range(200, 250, 10)]
        self.color = ('#0A2A22', '#0B6138')
        self.move = 'right'
        self.score = 0
        self.speed = 0.1
        self.b = True
        self.tar = create_target()

    def stop(self, event):
        if self.b:
            self.b = False
            return
        self.b = True
        game()

    def move_up(self, event):
        if self.move != 'down': self.move = 'up'

    def move_down(self, event):
        if self.move != 'up': self.move = 'down'

    def move_left(self, event):
        if self.move != 'right': self.move = 'left'

    def move_right(self, event):
        if self.move != 'left': self.move = 'right'

    def draw(self):
        a, b = 0, 1
        for x, y in self.body:
            canv.create_rectangle(y, x, y + 10, x + 10, tag='rect', fill=self.color[a], outline=self.color[a])
            a, b = b, a

    def step(self):
        head = self.body[len(self.body) - 1][:]
        if self.move == 'up':
            head[0] -= 10
            if head[0] == -10: head[0] = 490
        elif self.move == 'down':
            head[0] += 10
            if head[0] == 500: head[0] = 0
        elif self.move == 'left':
            head[1] -= 10
            if head[1] == -10: head[1] = 490
        elif self.move == 'right':
            head[1] += 10
            if head[1] == 500: head[1] = 0

        self.body.append(head)
        del self.body[0]

        for x in self.body[:-1]:
            if x == head:
                self.b = False
                canv.create_text(250, 200, text='game over', font='Verdana 26', fill='#000')

        if head == self.tar:
            self.score += 1
            self.body.append(self.tar)
            self.tar = create_target()
            if self.speed > 0.02: self.speed -= 0.01
            panel.delete('score')
            panel.create_text(60, 16, text='score: ' + str(self.score), tag='score', font='Arial 12', fill='#FFF')


def game():
    while snake.b:
        canv.delete('rect')
        snake.step()
        snake.draw()
        canv.update()
        time.sleep(snake.speed)


def create_target():
    canv.delete('target')
    x = (random.randint(1, 49) * 10)
    y = (random.randint(1, 49) * 10)
    canv.create_rectangle(x, y, x + 10, y + 10, tag='target', fill='#AA0000')
    return [y, x]

root = tkinter.Tk()
root.title('Snake')
root.resizable(False, False)

canv = tkinter.Canvas(root, width=500, height=500, bg='#DDD')
canv.pack()

panel = tkinter.Canvas(root, width=500, height=40, bg='#AAA')
panel.pack()

for x in range(0, 500, 10):
    canv.create_line(0, x, 500, x, fill='#FFF')
for x in range(0, 500, 10):
    canv.create_line(x, 0, x, 500, fill='#FFF')

snake = Snake()

root.bind('<w>', snake.move_up)
root.bind('<s>', snake.move_down)
root.bind('<a>', snake.move_left)
root.bind('<d>', snake.move_right)
root.bind('<space>', snake.stop)

game()

root.mainloop()
