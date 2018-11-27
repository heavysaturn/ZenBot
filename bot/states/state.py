from rlbot.agents.base_agent import SimpleControllerState


class State:
    def __init__(self, agent):
        self.expired = False
        self.agent = agent
        self.action = None
        self.controls = SimpleControllerState()

