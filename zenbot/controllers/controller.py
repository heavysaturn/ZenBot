import time

from rlbot.agents.base_agent import SimpleControllerState


class Controller:
    def __init__(self, agent):

        self.agent = agent
        self.start = time.time()
        self.controller = SimpleControllerState()

