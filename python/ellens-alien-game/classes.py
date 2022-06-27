"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    health = 3
    total_aliens_created = 0


    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1


    def hit(self):
        ''' Decrements health by 1 point. '''
        self.health -= 1


    def is_alive(self):
        ''' Check if the alien is still alive. '''
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        ''' Teleports the alien to a new location '''
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object):
        ''' TO-DO: Detects the collision of two objects '''


def new_aliens_collection(alien_start_positions):
    ''' Creates an Alien's collection based on the given positions '''
    return [Alien(positions[0], positions[1]) for positions in alien_start_positions]
