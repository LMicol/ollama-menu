#!/bin/bash

# vars
SERVICE_NAME="ollama_systray_controller"
PYTHON_PROGRAM="$(realpath main.py)"

# create systemd service file
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"

echo "[Unit]
Description=Ollama systray controller

[Service]
ExecStart=/usr/bin/python3 $PYTHON_PROGRAM
Restart=always
AmbientCapabilities=CAP_SYS_ADMIN

[Install]
WantedBy=default.target" | sudo tee $SERVICE_FILE > /dev/null

# reload systemd to recognize the new service
sudo systemctl daemon-reload

# enable and start the service
sudo systemctl enable $SERVICE_NAME.service
sudo systemctl start $SERVICE_NAME.service