from manim import *
import numpy as np


class Orientation3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(zoom = 0.4, phi=-75 * DEGREES, theta=-10 * DEGREES, gamma=90 * DEGREES, distance = 4)

        #create axes
        axes = ThreeDAxes(x_range=[0, 35], y_range=[-8, 8], z_range=[-8, 8], 
                          x_length=25)
        # label_x = axes.get_x_axis_label(Tex("X"))
        # label_y = axes.get_y_axis_label(Tex("Y"))
        # label_z = axes.get_z_axis_label(Tex("Z"))

        # self.add(axes, label_x, label_y, label_z)   
        self.add(axes)

        #create the graph
        graph = axes.plot(lambda x: 
                          np.sin(x),
                          color=BLUE)
        self.add(graph)
        
        self.wait(1)

