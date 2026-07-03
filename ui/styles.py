DARK_THEME = """
/* Main window background */
QMainWindow {
    background-color: #0f0f16;
}

QDialog, QMessageBox {
    background-color: #161622;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
}

/* Table base style */
QTableWidget {
    background-color: rgba(255, 255, 255, 0.03);
    alternate-background-color: rgba(255, 255, 255, 0.015);
    color: #f8f8f2;
    gridline-color: transparent; 
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 12px;
    padding: 10px;
    font-size: 14px;
    selection-background-color: rgba(139, 92, 246, 0.2); 
    selection-color: #ffffff;
}

QTableWidget::item:hover {
    background-color: rgba(139, 92, 246, 0.08); /* Un glow violet foarte subtil la trecerea mouse-ului */
}


/* Table header */
QHeaderView::section {
    background-color: transparent;
    color: #a78bfa;
    padding: 12px;
    border: none;
    border-bottom: 2px solid rgba(139, 92, 246, 0.3);
    font-weight: bold;
    font-size: 13px;
}

QHeaderView {
    background-color: transparent;
}

/* Table rows */
QTableWidget::item {
    padding: 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.03);
}

/* Inputs and dropdowns */
QLineEdit, QComboBox {
    background-color: rgba(255, 255, 255, 0.05);
    color: #ffffff;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 13px;
}

QLineEdit:focus, QComboBox:focus {
    border: 1px solid #8b5cf6;
    background-color: rgba(255, 255, 255, 0.08);
}

/* ComboBox dropdown */
QComboBox::drop-down {
    border: none;
    padding-right: 10px;
}

/* Buttons */
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #8b5cf6, stop:1 #6d28d9);
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 13px;
}

QPushButton:hover {
    background-color: #a78bfa;
}

QPushButton:pressed {
    background-color: #4c1d95;
}

/* Labels */
QLabel {
    color: #e2e8f0;
    font-size: 14px;
}

/* Menu bar */
QMenuBar {
    background-color: #0f0f16;
    color: #94a3b8;
    padding: 5px;
    font-size: 13px;
}

QMenuBar::item {
    background-color: transparent;
    padding: 6px 12px;
    border-radius: 4px;
}

QMenuBar::item:selected {
    background-color: rgba(255, 255, 255, 0.05);
    color: #ffffff;
}

/* Toolbar */
QToolBar {
    background-color: rgba(255, 255, 255, 0.02);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    padding: 8px;
    spacing: 10px;
}

/* Status bar */
QStatusBar {
    background-color: #0f0f16;
    color: #64748b;
    font-size: 12px;
}

/* Scrollbar */
QScrollBar:vertical {
    border: none;
    background: transparent;
    width: 8px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: rgba(255, 255, 255, 0.1);
    min-height: 20px;
    border-radius: 4px;
}

QScrollBar::handle:vertical:hover {
    background: rgba(139, 92, 246, 0.4);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    border: none;
    background: transparent;
}

QPushButton#editButton {
    background: transparent;
    background-color: rgba(139, 92, 246, 0.1);
    color: #a78bfa;
    border: 1px solid rgba(139, 92, 246, 0.3);
    padding: 6px 14px;
}

QPushButton#editButton:hover {
    background-color: rgba(139, 92, 246, 0.2);
    border: 1px solid rgba(139, 92, 246, 0.5);
    color: #ffffff;
}

QPushButton#deleteButton {
    background: transparent;
    background-color: rgba(239, 68, 68, 0.1);
    color: #f87171;
    border: 1px solid rgba(239, 68, 68, 0.3);
    padding: 6px 14px;
}

QPushButton#deleteButton:hover {
    background-color: rgba(239, 68, 68, 0.2);
    border: 1px solid rgba(239, 68, 68, 0.5);
    color: #ffffff;
}

QPushButton#deleteButton:pressed {
    background-color: rgba(239, 68, 68, 0.3);
}

"""
