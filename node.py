class NodeObj():
    x_pos: float
    y_pos: float
    x_vel: float
    y_vel: float
    id: int
    singular_c_value: int
    accumulated_c_value = 0
    sensor_radius: 10
    seen = []
    validated = []

    def __init__(self, x_pos, y_pos, x_vel, y_vel, c_val id):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.singular_c_value = c_val
        self.accumulated_c_value = c_val
        self.id = id
