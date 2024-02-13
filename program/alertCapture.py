from flask import Flask, request, jsonify

import json
import os
import requests

# Flask app
app = Flask(__name__)

@app.route('/newjson', methods=['POST'])
def newjson():
    alert = request.get_json()

    # Parse JSON alert from the request
    print("Received JSON alert:")
    print(alert)

    # Extract necessary information from the JSON alert
    alert_host = alert['alerts'][0]['labels']['host']
    alert_value = float(alert['alerts'][0]['annotations']['description'])

    print("alert_host")
    print(alert_host)
    print("alert_value")
    print(alert_value)


    file_path = f"/home/ec2-user/projectForTal/program/numOfSessionOnEachNode/{alert_host}.txt"

    if not os.path.exists(file_path):
        print("file NOT exists")
        # If the file doesn't exist, create it with the required content
        with open(file_path, 'w') as f:
            f.write(f"numberOfSession: {alert_value}\nstatus: 0\n")
    else:
        # If the file exists, read its current content
        print("file exist")
        with open(file_path, 'r') as f:
            content = f.read().splitlines()
            current_value = float(content[0].split(': ')[1])
            current_status = 0
            
        # Compare the current value with the received alert value
        if alert_value < current_value:
            # If the received alert value is less than the current value, update the file content
            print("file exist and modified")
            current_status = -1
            
        with open(file_path, 'w') as f:
            f.write(f"numberOfSession: {alert_value}\nstatus: {current_status}\n")


    print("Done checking")
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

