import math

from ZenBot.elements.vectors import Vector3


def rotator_to_matrix(our_object):
    """
    Some black voodoo magic shit.
    """
    r = our_object.rotation.data
    CR = math.cos(r[2])
    SR = math.sin(r[2])
    CP = math.cos(r[0])
    SP = math.sin(r[0])
    CY = math.cos(r[1])
    SY = math.sin(r[1])

    matrix = []
    matrix.append(Vector3([CP * CY, CP * SY, SP]))
    matrix.append(Vector3([CY * SP * SR - CR * SY, SY * SP * SR + CR * CY, -CP * SR]))
    matrix.append(Vector3([-CR * CY * SP - SR * SY, -CR * SY * SP + SR * CY, CP * CR]))
    return matrix


def to_local(origin, target):
    """
    Takes two GameObjects
    and returns the local coordinates.
    """
    x = (target.location - origin.location) * origin.matrix[0]
    y = (target.location - origin.location) * origin.matrix[1]
    z = (target.location - origin.location) * origin.matrix[2]
    return (x, y, z)


def velocity2D(target):
    """
    Return the difference in velocity
    between two objects.
    :param target:
    :return:
    """
    return math.sqrt(target.velocity.x ** 2 + target.velocity.y ** 2)


def distance2D(target, origin):
    """
    Takes either a GameObject or a
    Vector3 and returns the distance
    between the two.
    """

    if isinstance(target, Vector3):
        difference = target - origin
    else:
        difference = target.location - origin.location
    return math.sqrt(difference.x ** 2 + difference.x ** 2)
