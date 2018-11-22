from zenbot.controllers.example import ExampleController
from zenbot.states.state import State
from zenbot.utils.math import velocity2D, distance2D


class BallChase(State):
    def execute(self):
        target = self.agent.ball
        target_speed = velocity2D(self.agent.ball) + (distance2D(self.agent.ball, self.agent.me) / 1.5)
        controller = ExampleController(self.agent)

        return controller.execute(target, target_speed)