import sys
import psutil
import shutil

path = sys.argv
# CPU Funtions
def get_cpu_count():
    cpu_count = psutil.cpu_count()
    return cpu_count


def get_cpu_percent():
    percents = psutil.cpu_percent(interval=1, percpu=True)
    for i, percent in enumerate(percents):
        print(f"CPU {i}: {percent}% ")
def get_cpu_freq():
    freq = psutil.cpu_freq()
    print(f"Max:{freq.max}")

# def sensors_temperatures():
#    temps = psutil.sensors_temperatures()
#    print(temps)

stats = shutil.disk_usage(path[0])

print(stats)


