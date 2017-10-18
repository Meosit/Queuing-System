class SystemCharacteristic:
    def update(self, current_state, pi1_state, pi2_state):
        raise NotImplementedError()

    @property
    def result(self):
        raise NotImplementedError()

    @property
    def name(self):
        raise NotImplementedError()


class AbsoluteThroughput(SystemCharacteristic):
    def __init__(self, tacts_count):
        self._result = 0
        self._tacts_count = tacts_count

    def update(self, current_state, pi1_state, pi2_state):
        if current_state[3] == '1' and not pi2_state:
            self._result += 1

    @property
    def result(self):
        return self._result / self._tacts_count

    @property
    def name(self):
        return 'A '


class RejectProbability(SystemCharacteristic):
    def __init__(self, tacts_count):
        self._result = 0
        self._tacts_count = tacts_count

    def update(self, current_state, pi1_state, pi2_state):
        if (current_state == '1100' and pi1_state) or \
                (current_state == '1101' and ((pi1_state and (not pi2_state)) or (pi1_state and pi2_state))) or \
                (current_state == '1111' and (((not pi1_state) and pi2_state)
                                              or (pi1_state and pi2_state)
                                              or (pi1_state and (not pi2_state)))) or \
                (current_state == '2111' and ((not pi1_state) and pi2_state)):
            self._result += 2

    @property
    def result(self):
        return self._result / self._tacts_count

    @property
    def name(self):
        return 'Pr'


class AverageQueueLength(SystemCharacteristic):
    def __init__(self, tacts_count):
        self._queue_length = 0
        self._tacts_count = tacts_count

    def update(self, current_state, pi1_state, pi2_state):
        if current_state[2] == '1':
            self._queue_length += 1

    @property
    def result(self):
        return self._queue_length / self._tacts_count

    @property
    def name(self):
        return 'Lq'


class AverageTimeInQueue(SystemCharacteristic):
    def __init__(self, tacts_count):
        self._queue_time = 1
        self._request_time = 0
        self._request_times = []
        self._queue_times = []
        self._prev_state = '2000'
        self._tacts_count = tacts_count

    def update(self, current_state, pi1_state, pi2_state):
        if self._prev_state[2] == '0' and current_state[2] == '1':
            self._queue_time = 1
        elif self._prev_state[2] == '1' and current_state[2] == '1':
            self._queue_time += 1
        elif self._prev_state[2] == '1' and current_state[2] == '0':
            self._queue_times.append(self._queue_time)

        self._request_time += 1
        if current_state[3] == '1' and not pi2_state:
            self._request_times.append(self._request_time)
            self._request_time = 0
        self._prev_state = current_state

    @property
    def result(self):
        _sum = sum(self._queue_times)
        if _sum == 0:
            return 0.0
        return _sum / len(self._request_times)

    @property
    def name(self):
        return 'Wq'
