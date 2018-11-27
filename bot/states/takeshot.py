import math

from RLUtilities.LinearAlgebra import dot, clip

from bot.states.state import State
from bot.utils.draw import Draw


class TakeShot(State):

    def __init__(self, agent, powershot=False):
        super().__init__(agent)

        self.ball = self.agent.info.ball
        self.car = self.agent.info.my_car
        self.powershot = powershot
        self.renderer = Draw(agent)

    def distance_to_ball(self):

        difference = self.ball.pos - self.car.pos
        return math.sqrt(
            difference[0] ** 2
            + difference[1] ** 2
            + difference[2] ** 2
        )

    def execute(self):

        # the vector from the car to the ball in local coordinates:
        # delta_local[0]: how far in front of my car
        # delta_local[1]: how far to the left of my car
        # delta_local[2]: how far above my car
        delta_local = dot(self.ball.pos - self.car.pos, self.car.theta)

        # the angle between the direction the car is facing
        # and the in-plane local position of the ball
        phi = math.atan2(delta_local[1], delta_local[0])

        # a simple steering controller that is proportional to phi
        self.controls.steer = clip(2.5 * phi, -1.0, 1.0)

        # just set the throttle to 1 so the car is always moving forward
        self.controls.throttle = 1.0

        # Boost if the ball is close and it's a powershot
        if self.powershot and self.distance_to_ball() < 100:
            self.controls.boost = True
        else:
            self.controls.boost = False

        # We've hit the ball!
        if self.distance_to_ball() <= 1:
            self.expired = True

        # Render some guidelines
        self.renderer.agent_to_ball()

        return self.controls







