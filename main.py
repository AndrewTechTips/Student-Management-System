import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.styles import DARK_THEME

app = QApplication(sys.argv)
app.setStyleSheet(DARK_THEME)

main_window = MainWindow()
main_window.show()
main_window.load_data()

sys.exit(app.exec())
