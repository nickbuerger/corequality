#!/usr/bin/env python3

import psutil
from multiprocessing import Process, Manager
from time import sleep

testtime=30
interval=0.2
logical=False

def cpufreq(core):
    frequency = psutil.cpu_freq(percpu=True)[core]
    return frequency.current

def maxfreq(core,return_dict):
    frequencies = []
    for i in range(int(testtime/interval)):
        frequencies.append(cpufreq(core))
        sleep(interval)
    return_dict[core] = int(max(frequencies))

def runstress(core,pid):
    process = psutil.Process()
    process.cpu_affinity([core])
    while psutil.pid_exists(pid):
        1*1

if __name__ == '__main__':
    corecount = psutil.cpu_count(logical)
    manager = Manager()
    return_dict = manager.dict()
    print(f"Running {testtime}s of CPU stress on each core to find maximum frequency.")
    for core in range(corecount):
        tprocess = Process(target=maxfreq, args=(core,return_dict,))
        tprocess.start()
        sprocess = Process(target=runstress, args=(core,tprocess.pid,))
        sprocess.start()
        tprocess.join()
        sprocess.join()
        print(f"Core{core}: {return_dict[core]} MHz")
