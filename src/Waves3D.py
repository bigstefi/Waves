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

class Wave3DScene(ThreeDScene):
    def construct(self):
        #self.set_camera_orientation(zoom = 0.6, phi=45 * DEGREES, theta=45 * DEGREES, gamma=0 * DEGREES, distance = 4)
        #zoom 0.4 phi -0.4 theta =90*DEGREES
        #self.set_camera_orientation(zoom = 0.6, phi=-105 * DEGREES, theta=0 * DEGREES, gamma=90 * DEGREES, distance = 4)
        self.set_camera_orientation(zoom = 0.4, phi=-75 * DEGREES, theta=-10 * DEGREES, gamma=90 * DEGREES, distance = 4)

        valueTracker = ValueTracker(0)
                         
        #create axes
        axes = ThreeDAxes(x_range=[0, 35], y_range=[-8, 8], z_range=[-8, 8], x_length=25, y_length=8, z_length=8, 
                          axis_config={"include_tip": False})#.shift(RIGHT*5, UP*1.95).rotate_about_origin(40 * DEGREES, axis=UP)
        # label_x = axes.get_x_axis_label(Tex("X"))
        # label_y = axes.get_y_axis_label(Tex("Y"))
        # label_z = axes.get_z_axis_label(Tex("Z"))

        # self.add(axes, label_x, label_y, label_z)   
        self.add(axes)

        #create the graph
        graph = always_redraw(lambda: axes.plot(lambda x: 
                          np.sin(x + valueTracker.get_value()) + 
                          np.sin(x * 0.737 + valueTracker.get_value()) + 
                          np.cos(x / 2 + valueTracker.get_value()) +
                          np.sin(x / 0.69 + valueTracker.get_value()) +
                          np.sin(x / 1.2 + valueTracker.get_value()) +
                          np.sin(x / 0.335 + valueTracker.get_value()) +
                          np.sin(x / 0.913 + valueTracker.get_value()) +
                          np.sin(x / 1.3911 + valueTracker.get_value()) +
                          np.sin(x / 0.81 + valueTracker.get_value()) +
                          np.sin(x / 0.9 + valueTracker.get_value()),
                          color=BLUE)
                          #.SHIFT(OUT*(-1.5)*2)
                          #.rotate_about_origin(40 * DEGREES, axis=UP)
                          )
        self.add(graph)
        self.play(valueTracker.animate.set_value(-20), run_time=10, rate_func=linear)

        # self.wait(3)

        # g1 = always_redraw(lambda: axes.plot(lambda x: np.sin(x * 0.5 - 0.1 + valueTracker.get_value()) * 1.4, color=RED).shift(UP*1.2))
        # g2 = always_redraw(lambda: axes.plot(lambda x: np.sin(x * 0.737 * 0.5 - 0.2 + valueTracker.get_value()) * 2.0, color=GREEN).shift(UP*1.4))
        # g3 = always_redraw(lambda: axes.plot(lambda x: np.cos(x / 2 * 0.5 - 0.23 + valueTracker.get_value()), color=BLUE).shift(UP*1.6))
        # g4 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.69 * 0.5 - 0.27 + valueTracker.get_value()) * 3.0, color=YELLOW).shift(UP*1.8))
        # g5 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 1.2 * 0.5 - 4.0 + valueTracker.get_value()) * 1.2, color = ORANGE).shift(UP*2.0))
        # g6 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.335 * 0.5 - 0.54 + valueTracker.get_value()) * 2.74, color=PURPLE).shift(DOWN*2.0))
        # g7 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.913 * 0.5 - 0.52 + valueTracker.get_value()) * 3.32, color=PINK).shift(DOWN*1.8))
        # g8 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 1.3911 * 0.5 - 0.68 + valueTracker.get_value()), color=TEAL).shift(DOWN*1.6))
        # g9 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.81 * 0.5 - 0.93 + valueTracker.get_value()) * 2.3, color=GOLD).shift(DOWN*1.4))
        # g10 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.9 * 0.5 - 0.99 + valueTracker.get_value()) * 1.6, color=MAROON).shift(DOWN*1.2))

        g1 = always_redraw(lambda: axes.plot(lambda x: np.sin(x - 0.1 + valueTracker.get_value()) * 0.4, color=RED).shift(LEFT*1.2))
        g2 = always_redraw(lambda: axes.plot(lambda x: np.sin(x * 0.737 - 0.2 + valueTracker.get_value()) * 0.8, color=GREEN).shift(LEFT*1.4))
        g3 = always_redraw(lambda: axes.plot(lambda x: np.cos(x / 2 - 0.23 + valueTracker.get_value()), color=BLUE).shift(LEFT*1.6))
        g4 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.69 - 0.27 + valueTracker.get_value()) * 1.3, color=YELLOW).shift(LEFT*1.8))
        g5 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 1.2 - 4.0 + valueTracker.get_value()) * 1.2, color = ORANGE).shift(LEFT*2.0))
        g6 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.335 - 0.54 + valueTracker.get_value()) * 0.74, color=PURPLE).shift(RIGHT*2.0))
        g7 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.913 - 0.52 + valueTracker.get_value()) * 1.32, color=PINK).shift(RIGHT*1.8))
        g8 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 1.3911 - 0.68 + valueTracker.get_value()), color=TEAL).shift(RIGHT*1.6))
        g9 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.81 - 0.93 + valueTracker.get_value()) * 1.3, color=GOLD).shift(RIGHT*1.4))
        g10 = always_redraw(lambda: axes.plot(lambda x: np.sin(x / 0.9 - 0.99 + valueTracker.get_value()) * 0.6, color=MAROON).shift(RIGHT*1.2))

        group = VGroup(g1, g2, g3, g4, g5, g6, g7, g8, g9, g10)

        #self.Add(group)
        # #self.play(ApplyPointwiseFunction(lambda x: x * 2, graph))
        self.play(ReplacementTransform(graph, group, run_time=2), valueTracker.animate.set_value(0), run_time=2, rate_func=linear)
        #self.add(group)
        self.play(valueTracker.animate.set_value(-20), run_time=10, rate_func=linear)

        #self.wait(3)