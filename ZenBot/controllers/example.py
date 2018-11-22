import math
import time

from ZenBot.utils.math import velocity2D, distance2D
from .controller import Controller


class ExampleController(Controller):
    def execute(self, target, target_speed):
        location = target.local_location
        angle_to_ball = math.atan2(location.y, location.x)
        current_speed = velocity2D(self.agent.me)

        # Steering
        if angle_to_ball > 0.1:
            self.controller.steer = self.controller.yaw = 1

        elif angle_to_ball < -0.1:
            self.controller.steer = self.controller.yaw = -1

        else:
            self.controller.steer = self.controller.yaw = 0

        # Throttle
        if target_speed > current_speed:
            self.controller.throttle = 1.0

            if target_speed > 1400 and self.start > 2.2 and current_speed < 2250:
                self.controller.boost = True

        elif target_speed < current_speed:
            self.controller.throttle = 0

        # Dodging
        time_difference = time.time() - self.start
        if (
                time_difference > 2.2
                and distance2D(target.location, self.agent.me.location) > 1000
                and abs(angle_to_ball) < 1.3
        ):
            self.start = time.time()

        elif time_difference <= 0.1:
            self.controller.jump = True
            self.controller.pitch = -1

        elif time_difference >= 0.1 and time_difference <= 0.15:
            self.controller.jump = False
            self.controller.pitch = -1

        elif time_difference > 0.15 and time_difference < 1:
            self.controller.jump = True
            self.controller.yaw = self.controller.steer
            self.controller.pitch = -1

        return self.controller
