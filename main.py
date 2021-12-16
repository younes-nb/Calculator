import sys
from PyQt6.QtWidgets import QApplication
from Controller.MainController import MainController

def main():
    app = QApplication(sys.argv)
    window = MainController()
    window.view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
