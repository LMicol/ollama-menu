import sys
import subprocess
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMainWindow

class TrayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create the system tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("assets/icon.png"))
        
        # Create a menu for the tray icon
        tray_menu = QMenu(self)

        # Restart Ollama action
        action_restart = QAction("Restart Ollama", self)
        action_restart.triggered.connect(self.ollama_restart)
        action_restart.setIcon(QIcon("assets/restart.png"))
        tray_menu.addAction(action_restart)

        # Stop Ollama action
        action_stop = QAction("Stop Ollama", self)
        action_stop.triggered.connect(self.ollama_stop)
        action_stop.setIcon(QIcon("assets/stop.png"))
        tray_menu.addAction(action_stop)

        # Quit action
        action_quit = QAction("Quit", self)
        action_quit.triggered.connect(self.quit_application)
        tray_menu.addAction(action_quit)
        
        # Set the menu for the tray icon
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.setVisible(True)
    
    def quit_application(self):
        QApplication.quit()

    def ollama_restart(self):
        subprocess.run(['sudo', 'systemctl', 'restart', 'ollama'])

    def ollama_stop(self):
        subprocess.run(['sudo', 'systemctl', 'stop', 'ollama'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TrayApp()
    sys.exit(app.exec_())
