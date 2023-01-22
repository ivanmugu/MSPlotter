# =============================================================================
# This file is part of MSPloter
# 
# BSD 3-Clause License
# 
# Copyright (c) 2022, Ivan Munoz Gutierrez
# 
# A full description of the license is given in the LICENSE file at:
# https://github.com/ivanmugu/MSPlotter
# =============================================================================

"""Class for plotting arrows horizontally.

It can be used to reprent genes.
"""

import matplotlib.pyplot as plt
import numpy as np

class Arrow:
    """Make coordinates to represent an arrow horizontally."""
    def __init__(
        self, x1, x2, y, ratio_tail_head_width=0.5, head_width=2,
        head_height=200,
    ):
        self.x1 = x1
        self.x2 = x2
        self.y = y
        self.ratio_tail_head_width = ratio_tail_head_width
        self.tail_width = head_width * ratio_tail_head_width
        self.head_width = head_width
        self.head_height = head_height
        self.head_shoulder = (head_width - self.tail_width) / 2

    def coordinates_arrow_forward(self):
        """Get forward arrow shape coordinates horizontally."""
        height = self.x2 - self.x1
        if height <= self.head_height:
            x_1 = self.x2 - self.head_height
            x_2 = self.x2 - self.head_height
            x_3 = self.x2
            x_4 = self.x2 - self.head_height
            x_5 = self.x2 - self.head_height
            y_1 = self.y
            y_2 = self.y + (self.head_width * 0.5)
            y_3 = self.y
            y_4 = self.y - (self.head_width * 0.5)
            y_5 = self.y
            x_values = np.array([x_1, x_2, x_3, x_4, x_5])
            y_values = np.array([y_1, y_2, y_3, y_4, y_5])
            return (x_values, y_values)
        # Tail x-values
        x_1 = self.x1
        x_2 = self.x1
        # Head x-values
        x_3 = self.x2 - self.head_height
        x_4 = self.x2 - self.head_height
        x_5 = self.x2
        x_6 = self.x2 - self.head_height
        x_7 = self.x2 - self.head_height
        # Tail x-values
        x_8 = self.x1
        x_9 = self.x1
        # Tail y-values
        y_1 = self.y
        y_2 = self.y + (self.tail_width * 0.5)
        # Head y-values
        y_3 = self.y + (self.tail_width * 0.5)
        y_4 = self.y + (self.tail_width * 0.5) + self.head_shoulder
        y_5 = self.y
        y_6 = self.y - (self.tail_width * 0.5) - self.head_shoulder
        y_7 = self.y - (self.tail_width * 0.5)
        # Tail y-values
        y_8 = self.y - (self.tail_width * 0.5)
        y_9 = self.y
        # make datapoints for plotting
        x_values = np.array(
            [x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9]
        )
        y_values = np.array(
            [y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8, y_9]
        )
        return (x_values, y_values)

    def coordinates_arrow_reverse(self):
        """Get reverse arrow shape coordinates horizontally."""
        height = self.x1 - self.x2
        if height <= self.head_height:
            x_1 = self.x2 + self.head_height
            x_2 = self.x2 + self.head_height
            x_3 = self.x2
            x_4 = self.x2 + self.head_height
            x_5 = self.x2 + self.head_height
            y_1 = self.y
            y_2 = self.y - (self.head_width * 0.5)
            y_3 = self.y
            y_4 = self.y + (self.head_width * 0.5)
            y_5 = self.y
            x_values = np.array([x_1, x_2, x_3, x_4, x_5])
            y_values = np.array([y_1, y_2, y_3, y_4, y_5])
            return (x_values, y_values)
        # Tail x-values
        x_1 = self.x1
        x_2 = self.x1
        # Head x-values
        x_3 = self.x2 + self.head_height
        x_4 = self.x2 + self.head_height 
        x_5 = self.x2
        x_6 = self.x2 + self.head_height
        x_7 = self.x2 + self.head_height
        # Tail x-values
        x_8 = self.x1
        x_9 = self.x1
        # Tail y-values
        y_1 = self.y
        y_2 = self.y - (self.tail_width * 0.5)
        # Head y-values
        y_3 = self.y - (self.tail_width * 0.5)
        y_4 = self.y - (self.tail_width * 0.5) - self.head_shoulder
        y_5 = self.y
        y_6 = self.y + (self.tail_width * 0.5) + self.head_shoulder
        y_7 = self.y + (self.tail_width * 0.5)
        # Tail y-values
        y_8 = self.y + (self.tail_width * 0.5)
        y_9 = self.y
        # make datapoints for plotting
        x_values = np.array(
            [x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9]
        )
        y_values = np.array(
            [y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8, y_9]
        )
        return (x_values, y_values)

    def get_coordinates(self):
        if self.x1 < self.x2:
            return self.coordinates_arrow_forward()
        else:
            return self.coordinates_arrow_reverse()

if __name__ == "__main__":
    ####################
    # Example of usage #
    ####################

    # Make arrow
    arrow1 = Arrow(x1=750, x2=2000, y=10)
    x_values, y_values = arrow1.get_coordinates()
    plt.fill(x_values, y_values, 'b')

    arrow2 = Arrow(x1=1250, x2=250, y=20)
    x_values, y_values = arrow2.get_coordinates()
    plt.fill(x_values, y_values, 'r')

    plt.show()