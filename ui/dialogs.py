import re
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QComboBox,
    QPushButton,
    QGridLayout,
    QLabel,
    QMessageBox,
)
from database import DataBaseConnection


class InsertDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add mobile widget
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # Add a submit button
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text().strip()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text().strip()

        # Name validation
        if not name or len(name) < 3:
            QMessageBox.warning(
                self,
                "Validation Error",
                "Please enter a name with at least 3 characters",
            )
            return

        # Mobile num validation
        if not re.fullmatch(r"\+?\d{7,15}", mobile):
            QMessageBox.warning(
                self,
                "Validation Error",
                "Please enter a valid phone number.",
            )
            return

        connection = DataBaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)",
            (name, course, mobile),
        )
        connection.commit()
        cursor.close()
        connection.close()

        self.parent().load_data()
        self.close()


class EditDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Get student name from selected row
        index = self.parent().table.currentRow()
        student_name = self.parent().table.item(index, 1).text()

        # Get id from selected row
        self.student_id = self.parent().table.item(index, 0).text()

        # Add student name widget
        self.student_name = QLineEdit(student_name)
        layout.addWidget(self.student_name)

        # Add combo box of courses
        course_name = self.parent().table.item(index, 2).text()
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        # Add mobile widget
        mobile = self.parent().table.item(index, 3).text()
        self.mobile = QLineEdit(mobile)
        layout.addWidget(self.mobile)

        # Add a submit button
        button = QPushButton("Update")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        name = self.student_name.text().strip()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text().strip()

        # Name validation
        if not name or len(name) < 3:
            QMessageBox.warning(
                self,
                "Validation Error",
                "Please enter a name with at least 3 characters",
            )
            return

        # Mobile num validation
        if not re.fullmatch(r"\+?\d{7, 15}", mobile):
            QMessageBox.warning(
                self,
                "Validation Error",
                "Please enter a valid phone number.",
            )
            return

        connection = DataBaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s",
            (
                name,
                course,
                mobile,
                self.student_id,
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()

        # Refresh the table
        self.parent().load_data()
        self.close()


class DeleteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Delete Student Data")

        layout = QGridLayout()
        confirmation = QLabel("Are you sure you want to delete?")
        yes_btn = QPushButton("Yes")
        no_btn = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes_btn, 1, 0)
        layout.addWidget(no_btn, 1, 1)
        self.setLayout(layout)

        yes_btn.clicked.connect(self.delete_student)
        no_btn.clicked.connect(self.close)

    def delete_student(self):
        # Get selected row index and student id
        index = self.parent().table.currentRow()
        student_id = self.parent().table.item(index, 0).text()

        connection = DataBaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE from students WHERE id = %s", (student_id,))

        connection.commit()
        cursor.close()
        connection.close()

        self.parent().load_data()
        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText("The record was deleted successfully")
        confirmation_widget.exec()


class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        layout.addWidget(self.name_input)

        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.search)
        layout.addWidget(search_btn)

        self.setLayout(layout)

    def search(self):
        name = self.name_input.text()
        connection = DataBaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE name = %s", (name,))

        items = self.parent().table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            self.parent().table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()


class AboutDialog(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        content = """
        This app was created during the course "The Python Mega Course".
        Feel free to modify and reuse this app.
        """
        self.setText(content)
