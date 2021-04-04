import threading
import time
from typing import Iterable, Callable, Union

import nvsmi
import psutil

# From the docs:
# Warning the first time this function is called with interval = 0.0 or None
# it will return a meaningless 0.0 value which you are supposed to ignore.
# https://github.com/testingautomated-usi/repli-ensemble-bench/tree/0d8c483b8ac9c430e59263fd1cf7a4162009a4e6
psutil.cpu_percent()
time.sleep(0.1)

exit_event = threading.Event()


class CPU:
    id = -1
    uuid = 'cpu'

    def __init__(self):
        virtual_memory = psutil.virtual_memory()
        self.mem_util: float = virtual_memory.percent
        self.mem_used: float = virtual_memory.used
        # Actually stands for cpu util
        self.gpu_util: float = psutil.cpu_percent()
        # We currently still ignore temperature
        self.temperature = 0


class DeviceState:
    index = None
    uuid = None

    def __init__(self, measurements: Iterable[Union[nvsmi.GPU, CPU]], mean_time):
        self.mean_time = mean_time
        mem_util = []
        mem_used = []
        gpu_util = []
        temp = []

        for m in measurements:
            self._set_or_check_id(m)
            mem_util.append(m.mem_util)
            mem_used.append(m.mem_used)
            gpu_util.append(m.gpu_util)
            temp.append(m.temperature)

        self.mem_util = sum(mem_util) / len(mem_util)
        self.mem_used = sum(mem_used) / len(mem_used)
        self.gpu_util = sum(gpu_util) / len(gpu_util)
        self.temp = sum(temp) / len(temp)

    def _set_or_check_id(self, m):
        if self.index:
            assert self.index == m.id
            assert self.uuid == m.uuid
        else:
            self.index = m.id
            self.uuid = m.uuid

    def __repr__(self) -> str:
        return (
            f"{self.index} - "
            f"{self.uuid} - "
            f"Util: {round(self.gpu_util, 2)}% - "
            f"Mem: {self.mem_used}MiB ({round(self.mem_util, 2)}%) - "
            f"Temp: {round(self.temp, 2)}"
        )


def run(average_window_sec: int,
        read_sleep_sec: int = 0.1):
    while not exit_event.isSet():
        measurements, mean_time = _collect_measurements(average_window_sec, read_sleep_sec)
        for gpu, gpu_measurements in measurements.items():
            for seq in range(100):
				gpu_state = DeviceState(measurements=gpu_measurements, mean_time=mean_time)
				if (gpu_state.temp > 80):
					time.sleep(15.0)
				else:
					break
            


def _collect_measurements(average_window_sec, read_sleep_sec):
    measurements = {-1: []}
    start_time = time.time()
    time_over = False
    while time_over is False:
        gpus = read_nvidia_smi()
        for gpu in gpus:
            if gpu.id not in measurements:
                measurements[gpu.id] = []
            measurements[gpu.id].append(gpu)
        measurements[-1].append(CPU())
        # time_over = time.time() >= start_time + average_window_sec
		time_over = true

        # if read_sleep_sec > 0:
        #     time.sleep(read_sleep_sec)
    # Not exact, but close enough
    mean_time = (start_time + time.time()) / 2
    return measurements, mean_time


def read_nvidia_smi() -> Iterable[nvsmi.GPU]:
    return nvsmi.get_gpus()