import sys
import subprocess
from PySide2.QtWidgets import (QApplication, QWidget, QSystemTrayIcon, QMenu)
from PySide2.QtGui import QIcon


class SystemTray(QSystemTrayIcon):
    def __init__(self, system_tray_icon, parent=None):
        QSystemTrayIcon.__init__(self, system_tray_icon, parent)
        self.setToolTip("System Tray")

        # Create a Menu to add the applications
        system_tray_menu = QMenu(parent)

        # Add application to the System Tray
        application_menu = system_tray_menu.addAction("CPU Usage App")
        application_menu.triggered.connect(self.open_cpu_usage_app)
        application_menu.setIcon(QIcon("icons/app_icon_image.png"))

        # Add a sepetaor in the menu
        system_tray_menu.addSeparator()

        # Add exit menu to the System Tray
        exit_menu = system_tray_menu.addAction("Exit")
        exit_menu.triggered.connect(self.exit_system_tray)
        exit_menu.setIcon(QIcon("icons/exit_icon_image.png"))

        # Set the menu to bet the context menu for the system tray
        self.setContextMenu(system_tray_menu)


    # Runs the CpuUsageVisualization app
    def open_cpu_usage_app(self):
        '''
        NOTE: Before running the system tray app:
        - Create an apps folder within the SystemTray folder
        - Clone the repository: https://github.com/PratikTayshete/CPU-Usage-using-PySide2-and-Matplotlib
        - Place the repository within the apps folder
        Place the project in the apps folder.
        '''
        subprocess.call(["python3", "apps/CpuUsageVisualization/main.py"])


    def exit_system_tray(self):
        sys.exit()




if __name__ == '__main__':
    app = QApplication()
    widget = QWidget()
    # Add a System Tray entry and pass the icon image and the widget
    system_tray_icon = SystemTray(QIcon("icons/system_tray_icon_image.png"), widget)
    system_tray_icon.show()
    sys.exit(app.exec_())