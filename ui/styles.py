DARK_THEME = """
/* App background and text */
QMainWindow, QDialog, QMessageBox {
    background-color: #1e1e2e;
    color: #cdd6f4;
}

/* Main table look */
QTableWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    gridline-color: #313244;
    border: none;
    font-size: 14px;
    selection-background-color: #45475a;
}

/* Table header */
QHeaderView::section {
    background-color: #313244;
    color: #cdd6f4;
    padding: 8px;
    border: none;
    font-weight: bold;
    font-size: 14px;
}

/* Buttons */
QPushButton {
    background-color: #89b4fa;
    color: #11111b;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: bold;
    font-size: 13px;
}

QPushButton:hover {
    background-color: #b4befe;
}

QPushButton:pressed {
    background-color: #74c7ec;
}

/* Inputs and dropdowns */
QLineEdit, QComboBox {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #45475a;
    padding: 8px;
    border-radius: 6px;
    font-size: 13px;
}

/* Focus state */
QLineEdit:focus, QComboBox:focus {
    border: 1px solid #89b4fa;
}

/* Top bars and menus */
QStatusBar, QMenuBar, QToolBar {
    background-color: #11111b;
    color: #cdd6f4;
    border: none;
}

/* Menu hover */
QMenuBar::item:selected {
    background-color: #313244;
    border-radius: 4px;
}
"""
