import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QPushButton,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QVBoxLayout,
    QComboBox,
    QToolBar,
    QStatusBar,
    QGridLayout,
    QLabel,
    QMessageBox,
)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
