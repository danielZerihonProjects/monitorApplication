# Ansible Playbook README

## Description

This Ansible playbook automates It performs the following tasks:

- Installs required packages and dependencies per OS.
- install telegraf plugins.
- install required packages.
- install and starts the Telegraf service.
- Adds the server to Prometheus for monitoring.
- Executes a test suite to validate the program's functionality.

## Playbook Structure

The playbook consists of the following files:

- `main.yml`: Entry point of the playbook. It includes other YAML files based on certain conditions.
- `install.yml`: Installs necessary packages and dependencies.
- `startTelegrafService.yml`: Starts the Telegraf service and checks its status.
- `addServerToPrometheus.yml`: Adds the server to Prometheus for monitoring.
- `testSuite.yml`: Executes a test suite to validate the program's functionality.
