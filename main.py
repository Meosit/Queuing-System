import sys

from characteristics import *
from simulator import simulate, UnitsSettings
from transitions import TRANSITIONS

START_STATE = '2000'
TACTS_COUNT = 1000000

DEFAULT_SETTINGS = UnitsSettings(pi1=0.5, pi2=0.5)


def read_probability(value_name):
    result = None
    while result is None:
        raw_input = input('{}: '.format(value_name))
        try:
            result = float(raw_input)
        except ValueError:
            print('Invalid input.')
    return result


def read_units_settings():
    values = {}
    for setting in UnitsSettings._fields:
        values[setting] = read_probability(setting)
    return UnitsSettings(**values)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        units_settings = DEFAULT_SETTINGS
    elif len(sys.argv) == 1:
        units_settings = DEFAULT_SETTINGS
    else:
        units_settings = read_units_settings()

    characteristics = [AbsoluteThroughput(TACTS_COUNT), RejectProbability(TACTS_COUNT), AverageQueueLength(TACTS_COUNT),
                       AverageTimeInQueue(TACTS_COUNT)]

    states_statistics, characteristics_results = simulate(TRANSITIONS, units_settings, TACTS_COUNT, START_STATE,
                                                          characteristics)

    print('\nProbabilities:')
    for state, count in sorted(states_statistics.items(), key=lambda x: int(x[0])):
        print('P {} = {}'.format(state, count / TACTS_COUNT))

    print('\nCharacteristics:')

    for name, result in characteristics_results.items():
        print('{} = {}'.format(name, result))


if __name__ == '__main__':
    main()
