#!/bin/bash

# vars
APP_NAME="ollama_systray_controller"
PYTHON_PROGRAM="$(realpath main.py)"
USER_HOME=$(eval echo ~$USER)
AUTOSTART_DIR="$USER_HOME/.config/autostart"
DESKTOP_FILE="$AUTOSTART_DIR/$APP_NAME.desktop"

# Remove old systemd service if it exists
if [ -f "/etc/systemd/system/$APP_NAME.service" ]; then
    echo "Removing old systemd service..."
    sudo systemctl stop $APP_NAME.service 2>/dev/null
    sudo systemctl disable $APP_NAME.service 2>/dev/null
    sudo rm /etc/systemd/system/$APP_NAME.service
    sudo systemctl daemon-reload
fi

# Create autostart directory if it doesn't exist
mkdir -p "$AUTOSTART_DIR"

# Create desktop entry file
echo "[Desktop Entry]
Type=Application
Name=Ollama Systray Controller
Exec=/usr/bin/python3 $PYTHON_PROGRAM
Icon=application-x-executable
Comment=Ollama systray controller
Terminal=false
Categories=Utility;
X-GNOME-Autostart-enabled=true" > "$DESKTOP_FILE"

# Make it executable
chmod +x "$DESKTOP_FILE"

echo "Application installed as autostart entry: $DESKTOP_FILE"
echo "It will start automatically when you log in to your desktop"
echo "You can test it immediately by running: python3 $PYTHON_PROGRAM"