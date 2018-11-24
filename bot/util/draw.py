from RLUtilities.LinearAlgebra import vec3


def draw_waypoint(location, color_rgba, agent):
    """
    Draws a waypoint at the requested location.
    :param location: Where to draw the waypoint
    :param color_rgba: The RGBA values for the waypoint color
    :param agent: The agent who should render it.
    :return:
    """
    r = 200
    agent.renderer.begin_rendering()
    color = agent.renderer.create_color(*color_rgba)

    agent.renderer.draw_line_3d(
        location - r * vec3(1, 0, 0),
        location + r * vec3(1, 0, 0),
        color
    )

    agent.renderer.draw_line_3d(
        location - r * vec3(0, 1, 0),
        location + r * vec3(0, 1, 0),
        color
    )

    agent.renderer.draw_line_3d(
        location - (r / 2) * vec3(0, 0, 1),
        location + (r / 2) * vec3(0, 0, 1),
        color
    )
    agent.renderer.end_rendering()
