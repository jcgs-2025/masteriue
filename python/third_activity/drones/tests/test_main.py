import pytest
from drones.drones.models.quadcopter import Quadcopter
from drones.drones.models.commands import Forward, Backward, Turn_left, Take_off, Land, Turn_right


@pytest.fixture
def drone():
    return Quadcopter("raptor", 0, 0, [
        Take_off(), Forward(5), Turn_left(), Forward(5), Turn_left(),
        Forward(5), Turn_left(), Forward(5), Turn_left(), Backward(5),
        Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(),
        Forward(5), Turn_right(), Backward(5), Land()
    ])

def test_drone_initial_position(drone):
    assert drone.x == 0
    assert drone.y == 0

def test_drone_follow_commands(drone):
    drone.follow_commands()
    assert drone.x == 0
    assert drone.y == 0

