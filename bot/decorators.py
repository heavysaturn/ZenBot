from functools import wraps


def render(func):
    """
    A decorator that starts and stops
    the agent renderer. Mostly used
    in the utils.Draw class
    """
    @wraps(func)
    def with_rendering(*args, **kwargs):
        self = args[0]
        self.agent.renderer.begin_rendering()
        self._init_colors(self.agent.renderer)
        func(*args, **kwargs)
        self.agent.renderer.end_rendering()
    return with_rendering

