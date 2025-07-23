import json

import psutil



def cpu_data() -> tuple[dict,str]: 
    """
    Collects  and returns detailed CPU  ststistics using the psutil library
    
    Returns:
        dict: A dictionary containting total CPU usage, per-core usage,
        number of logical and physical cores, and CPU frequency info.
    
    """
    total_usage = psutil.cpu_percent(interval=1)
    per_cpu_usage = psutil.cpu_percent(interval=1 , percpu=True)
    logical_processors = psutil.cpu_count(logical=True)
    core = psutil.cpu_count(logical=False)
    total_freq = psutil.cpu_freq()
    per_cpu_freq = psutil.cpu_freq(percpu=True)
    
    cpu_data = {
        "totalUsage": total_usage,
        "perCoreUsage": per_cpu_usage,
        "logicalCore": logical_processors,
        "physicalCore": core,
        "totalFreq": total_freq,
        "perCoreFreq" : per_cpu_freq
    }
    
    return cpu_data , "cpu"



def disk_data() -> tuple[dict, str]:
    """
    Collects and returns disk and RAM usage data.

    Returns:
        dict: A dictionary with usage stats for each disk partition and RAM.
    """
    ram = psutil.virtual_memory()
    partitons = psutil.disk_partitions(all=False)
    storage_data = {}
    for i,disk in enumerate(partitons):
        storage_data[f"disk{i}"] = psutil.disk_usage(disk.mountpoint)
    
    storage_data["ram"] = ram
    return storage_data, "storage"




def get_process_data():
    pass


def combine_and_dump(*args):
    combined_data ={}
    for data,label in args:
        combined_data[label] = data
    
    return json.dumps(combined_data, indent=2, default=str)






def fetch_cpu():
    return combine_and_dump(cpu_data())
def fetch_storage():
    return combine_and_dump(disk_data())
def fetch_summary():
    return combine_and_dump(cpu_data(),disk_data())