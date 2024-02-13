#!/bin/bash

echo "Hi, please make sure you did: 
1. opened port 9273 on the Amazon EC2 instance security group
2. insert the pem file to the ~/.ssh folder
3. run the alertCapture.py app from the cli

Please insert your vm name (for example: ec2-54-208-138-90.compute-1.amazonaws.com)"
read -r vmHostName

echo "Please insert your pem file name stored at: ~/.ssh folder (for exapmle: rhelDaniDev.pem)"
read -r pathToPemFile

# Check SSH connection
echo "Checking SSH connection to $vmHostName..."
if ssh -q -o "BatchMode=yes" -i ~/.ssh/"$pathToPemFile" ec2-user@"$vmHostName" exit; then
    echo "SSH connection successful."
else
    echo "SSH connection failed. Exiting program."
    exit 1
fi

cd ../Ansible

# Add vmHostName to hosts if not present
if ! grep -q "$vmHostName" hosts; then
    echo "$vmHostName" >> hosts
fi

# Run Ansible playbook
ansible-playbook playbook.yml -i hosts --private-key ~/.ssh/"$pathToPemFile"

