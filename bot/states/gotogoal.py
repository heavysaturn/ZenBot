import math
import random

from RLUtilities.LinearAlgebra import vec3, dot
from RLUtilities.Maneuvers import Drive
from rlbot.agents.base_agent import SimpleControllerState

from bot.constants import Colors
from bot.states.state import State
from bot.util.draw import draw_waypoint


class GoToGoal(State):

    def __init__(self, agent, own_goal=True):
        super().__init__(agent)

        # Set the target
        if own_goal:
            self.steer = -1
            self.facing_goal = self.agent.info.their_goal.center
            target_pos = vec3(
                self.agent.info.my_goal.center[0],
                self.agent.info.my_goal.center[1] + 1000,
                0
            )
        else:
            self.steer = 1
            self.facing_goal = self.agent.info.my_goal.center
            target_pos = vec3(
                self.agent.info.their_goal.center[0],
                self.agent.info.their_goal.center[1] - 1000,
                0
            )
        target_speed = 1450
        self.action = Drive(self.agent.info.my_car, target_pos, target_speed)

    def execute(self):

        # Drive towards the goal.
        if not self.action.finished:
            self.action.step(0.01666)
            self.agent.controls = self.action.controls
            draw_waypoint(self.action.target_pos, Colors.yellow, self.agent)

        # We have reached the goal, time to turn around
        else:
            delta_local = dot(self.facing_goal - self.agent.info.my_car.pos, self.agent.info.my_car.theta)
            phi = math.atan2(delta_local[1], delta_local[0])
            if abs(phi) > 0.3:
                print(phi)
                self.agent.controls.steer = -1
                self.agent.controls.throttle = 0
                self.agent.controls.slide = True
                self.agent.controls.boost = False
            else:
                print(phi)
                self.agent.controls = SimpleControllerState()
                self.expired = True





