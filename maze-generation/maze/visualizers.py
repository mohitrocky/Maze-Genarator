import time

def visualize_algorithm(maze, canvas, generator, speed):
    def inner():
        maze.draw(canvas)
        for action, (c1, c2) in generator(maze):
            if action == 'connect':
                maze.connect(c1, c2)
                maze.draw_line_between(canvas, c1, c2, color='white')
            elif action == 'disconnect':
                maze.disconnect(c1, c2)
                maze.draw_line_between(canvas, c1, c2, color='black')
            time.sleep(speed)             
    canvas.do(inner)
