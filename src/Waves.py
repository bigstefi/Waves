from manim import *
import numpy as np


def ColorGroupRandomly(group):
    colors = [
        RED,
        GREEN,
        BLUE,
        YELLOW,
        ORANGE,
        PURPLE,
        PINK,
        TEAL,
        GOLD,
        MAROON,
        #CYAN,
        #MAGENTA,
    ]
    idxColors = 0

    for e in group:
        #e.set_color(random_bright_color())
        e.set_color(colors[idxColors])
        idxColors += 1
    
    return (group)

class WaveScene(Scene):
    def construct(self):
        #create axes
        axes = Axes(x_range=[-20, 20], y_range=[-8, 8])
        self.add(axes)

        #create the graph
        graph = axes.plot(lambda x: 
                          np.sin(x) + 
                          np.sin(x * 0.737) + 
                          np.cos(x / 2) +
                          np.sin(x / 0.69) +
                          np.sin(x / 1.2) +
                          np.sin(x / 0.335) +
                          np.sin(x / 0.913) +
                          np.sin(x / 1.3911) +
                          np.sin(x / 0.81) +
                          np.sin(x / 0.9),
                          color=BLUE)
        self.add(graph)
        
        self.wait(3)

        g1 = axes.plot(lambda x: np.sin(x))
        g2 = axes.plot(lambda x: np.sin(x * 0.737))
        g3 = axes.plot(lambda x: np.cos(x / 2))
        g4 = axes.plot(lambda x: np.sin(x / 0.69))
        g5 = axes.plot(lambda x: np.sin(x / 1.2))
        g6 = axes.plot(lambda x: np.sin(x / 0.335))
        g7 = axes.plot(lambda x: np.sin(x / 0.913))
        g8 = axes.plot(lambda x: np.sin(x / 1.3911))
        g9 = axes.plot(lambda x: np.sin(x / 0.81))
        g10 = axes.plot(lambda x: np.sin(x / 0.9))

        group = VGroup(g1, g2, g3, g4, g5, g6, g7, g8, g9, g10)
        ColorGroupRandomly(group)

        #self.play(ApplyPointwiseFunction(lambda x: x * 2, graph))
        self.play(ReplacementTransform(graph, group))

        self.wait(3)