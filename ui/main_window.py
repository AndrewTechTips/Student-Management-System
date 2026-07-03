from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QToolBar,
    QStatusBar,
    QHeaderView,
    QWidget,
    QVBoxLayout,
    QAbstractItemView,
    QLineEdit,
)

from database import DataBaseConnection
from .dialogs import InsertDialog, EditDialog, DeleteDialog, AboutDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(900, 600)

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction(QIcon("assets/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ("Id", "Name", "Course", "Mobile", "Email", "Group")
        )

        # Make the table read-only from the interface
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        # Hide unnecessary index column
        self.table.verticalHeader().setVisible(False)

        self.table.setShowGrid(False)
        self.table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.table.verticalHeader().setDefaultSectionSize(45)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # Id
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  # Name
        header.setSectionResizeMode(
            2, QHeaderView.ResizeMode.ResizeToContents
        )  # Course
        header.setSectionResizeMode(
            3, QHeaderView.ResizeMode.ResizeToContents
        )  # Mobile num
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)  # Email
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.addWidget(self.table)
        self.setCentralWidget(container)

        # Create toolbar and add toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        toolbar.addAction(add_student_action)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search by Name, Email, Course or Group...")
        self.search_bar.setFixedWidth(350)

        # Add clear btn
        self.search_bar.setClearButtonEnabled(True)

        self.search_bar.textChanged.connect(self.load_data)
        toolbar.addWidget(self.search_bar)

        # Create status bar and add status bar elements
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        self.search_bar.clearFocus()
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def load_data(self, search_keyword=""):
        connection = DataBaseConnection().connect()
        cursor = connection.cursor()

        if search_keyword:
            query = """
            SELECT * FROM students
                WHERE name LIKE %s OR email LIKE %s OR student_group LIKE %s OR course LIKE %s
            """
            like_pattern = f"%{search_keyword}%"
            cursor.execute(
                query, (like_pattern, like_pattern, like_pattern, like_pattern)
            )
        else:
            cursor.execute("SELECT * FROM students")

        result = cursor.fetchall()
        self.table.setRowCount(0)
        self.table.clearSelection()

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):

                item = QTableWidgetItem(str(data))
                item.setToolTip(str(data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                self.table.setItem(row_number, column_number, item)

        connection.close()

    def insert(self):
        dialog = InsertDialog(self)
        dialog.exec()

    def edit(self):
        dialog = EditDialog(self)
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog(self)
        dialog.exec()

    def about(self):
        dialog = AboutDialog(self)
        dialog.exec()
