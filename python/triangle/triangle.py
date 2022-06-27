def equilateral(sides):
    return is_valid(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    return is_valid(sides) \
        and (sides[0] == sides[1] \
        or sides[0] == sides[2] \
        or sides[1] == sides[0] \
        or sides[1] == sides[2] \
        or sides[2] == sides[0] \
        or sides[2] == sides[1])


def scalene(sides):
    return is_valid(sides) and sides[0] != sides[1] != sides[2]


def is_valid(sides):
    return sum(sides) > 0 and not is_degenerate(sides)


def is_degenerate(sides):
    return sides[0] + sides[1] < sides[2] \
        or sides[0] + sides[2] < sides[1] \
        or sides[1] + sides[0] < sides[2] \
        or sides[1] + sides[2] < sides[0] \
        or sides[2] + sides[0] < sides[1] \
        or sides[2] + sides[1] < sides[0]
