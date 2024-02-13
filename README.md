# Monitor Program

This repository contains an bash program that triggeres a Ansible program along with related files for setting up monitoring using Python flask applicaion, Pometheus and Telegraf.


- `program/`: Contains Python script `alertCapture.py`, Bash script `execudeProgram.sh` and folder `numOfSessionOnEachNode` that will conatin a txt file with the lines:
	a numberOfSession: X. 
	b status: Y.
- `prometheusFiles/`: Placeholder for Prometheus configuration files.
- `telegrafPlugins/`: Placeholder for Telegraf plugin files.
- `Ansible`: README for ansible located at: Ansible/addServerToMonitorStack.

## Scripts

### program/execudeProgram.sh

Main Script,This Bash script provides instructions and prompts the user to input the VM name and PEM file name. It then checks SSH connection, updates the hosts file, and executes the Ansible playbook.

### program/alertCapture.py

This Python script sets up a Flask application to capture alerts, parse JSON data, and update files based on received alerts.

### telegrafPlugins/vm_metrics.py

This Python script collects various system metrics such as CPU usage, RAM usage, RAM available, and the number of active sessions.
