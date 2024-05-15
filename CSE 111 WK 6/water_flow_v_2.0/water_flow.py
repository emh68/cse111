"""For this assignment I added the following items to exceed requirements: constant variables, a function to
convert kPa (kilopascals to psi) and a test function to test the convert kPa to psi function.

Getting clean water to all buildings in a city is a large and expensive task. Many cities will build an elevated
water tank, and install a pump that pushes water up to the tank where the water is stored. In the city,
when a thirsty person opens a water faucet, water runs from the tank through pipes to the faucet. Earth’s gravity
pulling on the water in the elevated tank pressurizes the water and causes it to spray from the faucet.Before a city
builds a water distribution system, an engineer must design the system and ensure water will flow to all buildings in
the city. An engineer must choose the tower height, pipe type, pipe diameter, and pipe path. Engineers use software
to help them make these choices and design a working water distribution system."""



WATER_DENSITY = 998.2
EARTH_ACCEL_OF_GRAVITY = 9.80665
WATER_DYNAMIC_VISCOSITY = 0.0010016


def water_column_height(tower_height, tank_height):
    """Calculates and returns the height of a column of water using an equation 
    and values for the tower height and tank height"""

    height = float(tower_height + (3 * tank_height) / 4)

    return height


def pressure_gain_from_water_height(height):
    """Calculates and returns the pressure caused by Earth’s gravity pulling on
     the water stored in an elevated tank."""

    pressure_gain = float(WATER_DENSITY * EARTH_ACCEL_OF_GRAVITY * height) / 1000

    return pressure_gain


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculates and returns the water pressure lost because of the friction
    between the water and the walls of a pipe that it flows through."""

    lost_pressure_from_pipe = (float
                               ((-abs(friction_factor) * pipe_length * WATER_DENSITY * fluid_velocity ** 2) /
                                (2000 * pipe_diameter)))

    return lost_pressure_from_pipe


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline. """

    lost_pressure_from_fittings = float((-abs(0.04) * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings) / 2000)

    return lost_pressure_from_fittings


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates and returns the Reynolds number for a pipe with water flowing through it. The Reynolds number is
        a unitless ratio of the inertial and viscous forces in a fluid that is useful for predicting fluid flow in
        different situations."""

    reynolds_number = WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY

    return reynolds_number


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """calculates the water pressure lost because of water moving from a pipe with a large diameter into a
        pipe with a smaller diameter."""

    k = float(0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter) ** 4 - 1)

    lost_pressure_from_pipe_reduction = float((-abs(k) * WATER_DENSITY * fluid_velocity ** 2) / 2000)

    return lost_pressure_from_pipe_reduction


def convert_kilopascals_to_psi(pressure):
    """Converts pressure from kilopascal units to psi (pounds per square inch)"""

    pressure_in_psi = pressure * 0.1450377377

    return pressure_in_psi


PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65  # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018  # (unitless)
HOUSEHOLD_VELOCITY = 1.75  # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    pressure = convert_kilopascals_to_psi(pressure)
    print()
    print(f"Pressure at house: {pressure:.1f} psi")


if __name__ == "__main__":
    main()
