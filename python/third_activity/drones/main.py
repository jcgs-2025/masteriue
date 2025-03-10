from drones.models.quadcopter import Quadcopter
from drones.models.commands import Forward, Backward, Turn_left, Take_off, Land, Turn_right
import concurrent.futures

def execute_drone_commands(drone):
    """
    Execute the commands of a drone.
    
    Args:
        drone (Quadcopter): The drone to execute the commands.
        
    Returns:
        Quadcopter: The drone with the commands executed.
    
    Raises:
        Exception: If the drone is not a Quadcopter.
    """
    drone.follow_commands()
    return drone

def detect_collisions(drones):
    positions = {}
    for drone in drones:
        for pos in drone.positions:
            if pos in positions:
                positions[pos].append(drone.id)
            else:
                positions[pos] = [drone.id]
    
    collisions = {pos: ids for pos, ids in positions.items() if len(ids) > 1}
    return collisions

def main():
    drones = [
        Quadcopter("Phantom", 0, 0, [Take_off(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Backward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Backward(5), Land()]),
        Quadcopter("Mavic", 0, 0, [Take_off(), Forward(10), Turn_right(), Forward(10), Turn_right(), Forward(10), Turn_right(), Forward(10), Land()]),
        Quadcopter("Spark", 0, 0, [Take_off(), Forward(15), Turn_left(), Forward(15), Turn_left(), Forward(15), Turn_left(), Forward(15), Land()])
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(execute_drone_commands, drone) for drone in drones]
        for future in concurrent.futures.as_completed(futures):
            completed_drone = future.result()
            print(f"{completed_drone.id} has completed its commands.")

    collisions = detect_collisions(drones)
    if collisions:
        print("Be careful! Collisions detected at the following positions:")
        for pos, ids in collisions.items():
            print(f"Position {pos}: {', '.join(ids)}")
    else:
        print("No collisions detected.")

if __name__ == "__main__":
    main()