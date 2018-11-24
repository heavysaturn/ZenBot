from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from RLUtilities.GameInfo import GameInfo

from bot.states.gotogoal import GoToGoal


class ZenBot(BaseAgent):

    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        self.info = GameInfo(index, team)
        self.controls = SimpleControllerState()
        self.state = None
        self.own_goal = True
        self.counter = 0

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:

        self.preprocess(packet)

        if self.state is None:
            self.state = GoToGoal(self)
        if not self.state.expired:
            self.state.execute()
#        else:
#            self.own_goal = not self.own_goal
#            self.state = GoToGoal(self, self.own_goal)
        return self.controls

    def preprocess(self, packet):
        """
        This reads all the game info into a super convenient object.
        Example output:
        {
            'time': 16.703845287475588,
            'ball': <RLUtilities.Simulation.Ball object at 0x00000264BF6769D0>,
            'pitch': <RLUtilities.Simulation.Pitch object at 0x00000264BF676ED8>,
            'my_goal': <RLUtilities.Goal.Goal object at 0x00000264BF676BA8>,
            'their_goal': <RLUtilities.Goal.Goal object at 0x00000264BF678AC8>,
            'team': 0,
            'index': 0,
            'cars': [
                <RLUtilities.Simulation.Car object at 0x00000264BF6CDA40>,
                <RLUtilities.Simulation.Car object at 0x00000264BF6818F0>
            ],
            'teammates': [],
            'opponents': [
                <RLUtilities.Simulation.Car object at 0x00000264BF6818F0>
            ],
            'my_car': <RLUtilities.Simulation.Car object at 0x00000264BF6CDA40>,
            'boost_pads': [
                <RLUtilities.GameInfo.BoostPad object at 0x00000264BF690BE0>,
                <RLUtilities.GameInfo.BoostPad object at 0x00000264BF698C50>,
                <RLUtilities.GameInfo.BoostPad object at 0x00000264BF6CD898>,
                <RLUtilities.GameInfo.BoostPad object at 0x00000264BF6CD908>,
                <RLUtilities.GameInfo.BoostPad object at 0x00000264BF6CD978>,
                <RLUtilities.GameInfo.BoostPad object at 0x00000264BF6CD9E8>
            ],
            'ball_predictions': [],
            'about_to_score': None,
            'about_to_be_scored_on': None,
            'time_of_goal': -1
        }
        """

        self.info.read_packet(packet)
