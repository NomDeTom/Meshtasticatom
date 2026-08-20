import copy

from numpy import sqrt

class Point:
    """
    Simple point in 3D euclidean space, all 3 coordinates floats
    """
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def euclidean_distance(self, p2) -> float:
        """Euclidean distance between this point and another."""
        x_diff = self.x - p2.x
        y_diff = self.y - p2.y
        z_diff = self.z - p2.z
        return sqrt( x_diff ** 2 + y_diff ** 2 + z_diff ** 2 )

    def update_xy(self, x: float, y: float):
        """
        A point is often 'moved' in our simulation. This is just
        an easy way to do that without using direct member access.
        """
        self.x = x
        self.y = y

    def copy(self):
        """
        return a copy of this point, so that mutations on the new point
        do not effect this point
        """
        return copy.copy(self)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
