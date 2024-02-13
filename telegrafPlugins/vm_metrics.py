import os
import json
import psutil
import shutil

metrics = {'cpu_used' : 0, 'ram_used': 0, 'ram_available': 0}

cpu_used=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),1))
ram_used=psutil.virtual_memory().percent
ram_available=round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,1)
numberOfSessions=str(round(float(os.popen('''who | wc -l''').readline()),1))


metrics['cpu_used'] = float(cpu_used)
metrics['ram_used'] = float(ram_used)
metrics['ram_available'] = float(ram_available)
metrics['numberOfSessions'] = float(numberOfSessions)

print (json.dumps(metrics))
