from ecoloco_final_version import get_distance_to_target
import pytest


def test_measure_distance():
    assert test_measure_distance(66) == {
        'frequency': 550, 'volume': 0.4, 'duration': 0.5, 'repetitions': 3, 'time_between_tones': 0.1}


pytest.main(["-v", "--tb=line", "-rN", __file__])
