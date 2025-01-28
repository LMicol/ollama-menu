import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMainWindow
from PyQt5.QtGui import QIcon

class TrayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create the system tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("assets/icon.png"))
        
        # Create a menu for the tray icon
        tray_menu = QMenu(self)
        
        # Quit action
        action_quit = QAction("Quit", self)
        action_quit.triggered.connect(self.quit_application)
        tray_menu.addAction(action_quit)
        
        # Set the menu for the tray icon
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.setVisible(True)
    
    def quit_application(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TrayApp()
    sys.exit(app.exec_())
