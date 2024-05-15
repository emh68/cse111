from pytest import approx
import pytest

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, \
    pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, convert_kilopascals_to_psi


def test_water_column_height():
    assert water_column_height(tower_height=0, tank_height=0) == approx(0)
    assert water_column_height(tower_height=0, tank_height=10) == approx(7.5)
    assert water_column_height(tower_height=25, tank_height=0) == approx(25)
    assert water_column_height(tower_height=48.3, tank_height=12.8) == approx(57.9)


def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(height=0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(height=30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(height=50) == approx(489.450, abs=0.001)


def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(pipe_diameter=0.048692, pipe_length=0,
                                   friction_factor=0.018, fluid_velocity=1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(pipe_diameter=0.048692, pipe_length=200,
                                   friction_factor=0, fluid_velocity=1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(pipe_diameter=0.048692, pipe_length=200,
                                   friction_factor=0.018, fluid_velocity=0) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(pipe_diameter=0.048692, pipe_length=200,
                                   friction_factor=0.018, fluid_velocity=1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(pipe_diameter=0.048692, pipe_length=200,
                                   friction_factor=0.018, fluid_velocity=1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(pipe_diameter=0.28687, pipe_length=1000,
                                   friction_factor=0.013, fluid_velocity=1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(pipe_diameter=0.28687, pipe_length=1800.75,
                                   friction_factor=0.013, fluid_velocity=1.65) == approx(-110.884, abs=0.001)


def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(fluid_velocity=0, quantity_fittings=3) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(fluid_velocity=1.65, quantity_fittings=0) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(fluid_velocity=1.65, quantity_fittings=2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(fluid_velocity=1.75, quantity_fittings=2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(fluid_velocity=1.75, quantity_fittings=5) == approx(-0.306, abs=0.001)


def test_reynolds_number():
    assert reynolds_number(hydraulic_diameter=0.048692, fluid_velocity=0) == approx(0, abs=1)
    assert reynolds_number(hydraulic_diameter=0.048692, fluid_velocity=1.65) == approx(80069, abs=1)
    assert reynolds_number(hydraulic_diameter=0.048692, fluid_velocity=1.75) == approx(84922, abs=1)
    assert reynolds_number(hydraulic_diameter=0.28687, fluid_velocity=1.65) == approx(471729, abs=1)
    assert reynolds_number(hydraulic_diameter=0.28687, fluid_velocity=1.75) == approx(500318, abs=1)


def test_pressure_lost_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(larger_diameter=0.28687, fluid_velocity=0, reynolds_number=1,
                                             smaller_diameter=0.048692) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe_reduction(larger_diameter=0.28687, fluid_velocity=1.65, reynolds_number=471729,
                                             smaller_diameter=0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(larger_diameter=0.28687, fluid_velocity=1.75, reynolds_number=500318,
                                             smaller_diameter=0.048692) == approx(-184.182, abs=0.001)


def test_convert_kilopascals_to_psi():
    assert convert_kilopascals_to_psi(pressure=158.7) == approx(23.017, abs=0.001)
    assert convert_kilopascals_to_psi(pressure=156.4) == approx(22.683, abs=0.001)
    assert convert_kilopascals_to_psi(pressure=185.2) == approx(26.860, abs=0.001)
    assert convert_kilopascals_to_psi(pressure=859.2) == approx(124.616, abs=0.001)
    assert convert_kilopascals_to_psi(pressure=97.1) == approx(14.083, abs=0.001)



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.

pytest.main(["-v", "--tb=line", "-rN", __file__])
