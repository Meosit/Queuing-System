TRANSITIONS = [
    ['2000', '1000', lambda pi1, pi2: 1],
    ['1000', '2100', lambda pi1, pi2: 1],

    ['2100', '1100', lambda pi1, pi2: pi1],
    ['2100', '1001', lambda pi1, pi2: not pi1],

    ['1100', '2100', lambda pi1, pi2: pi1],
    ['1100', '2101', lambda pi1, pi2: not pi1],

    ['1001', '2100', lambda pi1, pi2: not pi2],
    ['1001', '2101', lambda pi1, pi2: pi2],

    ['2101', '1100', lambda pi1, pi2: pi1 and (not pi2)],
    ['2101', '1001', lambda pi1, pi2: (not pi1) and (not pi2)],
    ['2101', '1101', lambda pi1, pi2: pi1 and pi2],
    ['2101', '1011', lambda pi1, pi2: (not pi1) and pi2],

    ['1101', '2100', lambda pi1, pi2: (pi1 and (not pi2))],
    ['1101', '2101', lambda pi1, pi2: ((not pi1) and (not pi2)) or (pi1 and pi2)],
    ['1101', '2111', lambda pi1, pi2: (not pi1) and pi2],

    ['1011', '2101', lambda pi1, pi2: not pi2],
    ['1011', '2111', lambda pi1, pi2: pi2],

    ['2111', '1101', lambda pi1, pi2: pi1 and (not pi2)],
    ['2111', '1011', lambda pi1, pi2: ((not pi1) and (not pi2)) or ((not pi1) and pi2)],
    ['2111', '1111', lambda pi1, pi2: pi1 and pi2],

    ['1111', '2111', lambda pi1, pi2: ((not pi1) and pi2) or ((not pi1) and (not pi2)) or (pi1 and pi2)],
    ['1111', '2101', lambda pi1, pi2: pi1 and (not pi2)],
]
