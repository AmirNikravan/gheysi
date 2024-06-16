import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a button
        self.button = QPushButton("Change Color", self)
        self.button.clicked.connect(self.change_color)
        
        # Set initial style
        self.button.setStyleSheet("background-color: white;")

    def change_color(self):
        # Change background color to red when clicked
        self.button.setStyleSheet("background-color: red;")
        
        # Reset the background color after 1000 milliseconds (1 second)
        QTimer.singleShot(100, self.reset_color)

    def reset_color(self):
        # Reset background color to default (white)
        self.button.setStyleSheet("background-color: white;")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
