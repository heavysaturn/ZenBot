import math

from RLUtilities.LinearAlgebra import vec3, dot

from bot.constants import Colors
from bot.decorators import render


class Draw:
    """
    A class used to draw things in the game world.
    """

    def __init__(self, agent):

        # Initialize renderer
        self.agent = agent
        self.car = self.agent.info.my_car
        self.ball = self.agent.info.ball

    def _init_colors(self, renderer):
        """
        This is automatically called by the @render decorator.
        """
        # Initialize colors
        self.red = renderer.create_color(*Colors.red)
        self.green = renderer.create_color(*Colors.green)
        self.blue = renderer.create_color(*Colors.blue)
        self.white = renderer.create_color(*Colors.white)
        self.gray = renderer.create_color(*Colors.gray)
        self.purple = renderer.create_color(*Colors.purple)

    @render
    def waypoint(self, location):
        """
        Draws a waypoint at the requested location.
        :param location: Where to draw the waypoint
        """

        self.agent.renderer.draw_line_3d(
            location - 200 * vec3(1, 0, 0),
            location + 200 * vec3(1, 0, 0),
            self.yellow
        )

        self.agent.renderer.draw_line_3d(
            location - 200 * vec3(0, 1, 0),
            location + 200 * vec3(0, 1, 0),
            self.yellow
        )

        self.agent.renderer.draw_line_3d(
            location - 100 * vec3(0, 0, 1),
            location + 100 * vec3(0, 0, 1),
            self.yellow
        )

    @render
    def agent_to_ball(self):
        """
        Visualizes the relationship between
        the agent and the ball.
        :return:
        """

        # Get crucial vectors
        forward = self.car.forward()
        left = self.car.left()
        up = self.car.up()

        # Polyline angle
        radius = 200
        num_segments = 30

        # The vector from the car to the ball in local coordinates
        # delta_x: how far in front of my car
        # delta_y: how far to the left of my car
        # delta_z: how far above my car
        delta_local = dot(self.ball.pos - self.car.pos, self.car.theta)
        delta_x = delta_local[0]
        delta_y = delta_local[1]
        delta_z = delta_local[2]

        # The angle between the direction the car is facing
        # and the in-plane local position of the ball
        phi = math.atan2(delta_y, delta_x)

        # Draw guidelines for the ball and car.
        self.agent.renderer.draw_line_3d(self.car.pos, self.car.pos + delta_x * forward, self.red)
        self.agent.renderer.draw_line_3d(self.car.pos, self.car.pos + delta_y * left, self.green)
        self.agent.renderer.draw_line_3d(self.car.pos, self.car.pos + delta_z * up, self.blue)
        self.agent.renderer.draw_line_3d(self.car.pos, self.ball.pos, self.white)
        self.agent.renderer.draw_line_3d(self.ball.pos, self.ball.pos - delta_z * up, self.gray)
        self.agent.renderer.draw_line_3d(self.car.pos, self.ball.pos - delta_z * up, self.gray)

        # Draw the ball trajectory
        angle = []
        for i in range(num_segments):
            cos = math.cos(phi * float(i) / (num_segments - 1))
            sin = math.sin(phi * float(i) / (num_segments - 1))
            angle.append(self.car.pos + radius * (cos * forward + sin * left))
        self.agent.renderer.draw_polyline_3d(angle, self.purple)
