#pip install GPUtil tabulate

import GPUtil
from tabulate import tabulate

def gpu_info():
    gpus = GPUtil.getGPUs()
    gpus_list = []

    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f'{gpu.load*100}%'
        gpu_free_memory = f'{gpu.memoryFree}MB'
        gpu_used_memory = f'{gpu.memoryUsed}MB'
        gpu_total_memoru = f'{gpu.memoryTotal}MB'
        gpu_temp = f'{gpu.temperature}'

        gpus_list.append((
            gpu_id,
            gpu_name,
            gpu_load,
            gpu_free_memory,
            gpu_used_memory,
            gpu_total_memoru,
            gpu_temp
        ))
    return str(tabulate(
            gpus_list,
            headers=(
                'id',
                'name',
                'load',
                'free memory',
                'used memory',
                'total memory',
                'temperature'
            ),
            tablefmt='pretty'
        )
    )

if __name__ == '__main__':
    print(gpu_info())

