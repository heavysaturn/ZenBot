from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from bot.elements.gameobjects import GameObject
from bot.states.ballchase import BallChase
from bot.Utilities.math import rotator_to_matrix, to_local


class ZenBot(BaseAgent):

    def _get_vector(self, target: str, vector_type, index=None):

        # First set the target, i.e. the game ball
        if index is not None:
            target = getattr(self.game, target)[index]
        else:
            target = getattr(self.game, target)

        # Now find the correct vector
        vector = getattr(target.physics, vector_type)

        if vector_type == "rotation":
            return (
                vector.pitch,
                vector.yaw,
                vector.roll
            )

        else:
            return (
                vector.x,
                vector.y,
                vector.z
            )

    def initialize_agent(self):
        self.me = GameObject()
        self.opponent = GameObject()
        self.ball = GameObject()
        self.controller_state = SimpleControllerState()
        self.state = BallChase(self)

    def get_output(self, game: GameTickPacket) -> SimpleControllerState:

        self.preprocess(game)
        return self.state.execute()


    def preprocess(self, game):

        # Store the gametick data
        self.game = game

        # Get vectors for the bot
        self.me.location.data = self._get_vector("game_cars", "location", self.index)
        self.me.velocity.data = self._get_vector("game_cars", "velocity", self.index)
        self.me.rotation.data = self._get_vector("game_cars", "rotation", self.index)
        self.me.rvelocity.data = self._get_vector("game_cars", "angular_velocity", self.index)
        self.me.matrix = rotator_to_matrix(self.me)

        # Get vectors for the ball
        self.ball.location.data = self._get_vector("game_ball", "location")
        self.ball.velocity.data = self._get_vector("game_ball", "velocity")
        self.ball.rotation.data = self._get_vector("game_ball", "rotation")
        self.ball.rvelocity.data = self._get_vector("game_ball", "angular_velocity")
        self.ball.matrix = rotator_to_matrix(self.ball)

        self.ball.local_location.data = to_local(self.ball, self.me)

