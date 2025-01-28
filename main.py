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
        tray_menu.addAction(action_restart)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TrayApp()
    sys.exit(app.exec_())
