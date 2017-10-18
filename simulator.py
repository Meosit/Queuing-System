from collections import defaultdict, namedtuple
from random import random

UnitsSettings = namedtuple('UnitsSettings', ['pi1', 'pi2'])


def simulate(transitions, units_settings, tacts_count, start_state, characteristics):
    result = defaultdict(int)
    pi1, pi2 = units_settings.pi1, units_settings.pi2

    current_state = start_state
    for _ in range(tacts_count):
        pi1_state = random() <= pi1
        pi2_state = random() <= pi2

        result[current_state] += 1

        for characteristic in characteristics:
            characteristic.update(current_state, pi1_state, pi2_state)

        current_state = next((x for x in transitions if x[0] == current_state and x[2](pi1_state, pi2_state)))[1]

    return result, {x.name: x.result for x in characteristics}
