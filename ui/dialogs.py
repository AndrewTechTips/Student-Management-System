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
        self.setFixedHeight(400)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Full Name")
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics", "Computer Science"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add mobile widget
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("+1234567890")
        layout.addWidget(self.mobile)

        # Add email widget
        self.email = QLineEdit()
        self.email.setPlaceholderText("name@example.com")
        layout.addWidget(self.email)

        # Add student group widget
        self.student_group = QLineEdit()
        self.student_group.setPlaceholderText("Group (e.g., Gr 1, Math Prep)")
        layout.addWidget(self.student_group)

        # Add a submit button
        button = QPushButton("Save Record")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text().strip()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text().strip()
        email = self.email.text().strip()
        group = self.student_group.text().strip()

        # Name validation
        if not name or len(name) < 3:
            QMessageBox.warning(
                self,
                "Invalid Input",
                "Name needs at least 3 characters.",
            )
            return

        # Mobile num validation
        if not re.fullmatch(r"\+?\d{7,15}", mobile):
            QMessageBox.warning(
                self,
                "Invalid Input",
                "Please enter a valid phone number.",
            )
            return

        # Email validation
        if not re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            QMessageBox.warning(self, "Invalid Input", "Please provide a valid email.")
            return

        # Group validation
        if not group:
            QMessageBox.warning(self, "Invalid Input", "Group cannot be empty.")
            return

        connection = DataBaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (name, course, mobile, email, student_group) VALUES (%s, %s, %s, %s, %s)",
            (name, course, mobile, email, group),
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
        self.setFixedHeight(400)

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
        courses = ["Biology", "Math", "Astronomy", "Physics", "Computer Science"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        # Add mobile widget
        mobile = self.parent().table.item(index, 3).text()
        self.mobile = QLineEdit(mobile)
        layout.addWidget(self.mobile)

        # Add email widget
        email_item = self.parent().table.item(index, 4)
        self.email = QLineEdit(email_item.text() if email_item else "")
        layout.addWidget(self.email)

        # Add group widget
        group_item = self.parent().table.item(index, 5)
        self.student_group = QLineEdit(group_item.text() if group_item else "")
        layout.addWidget(self.student_group)

        # Add a submit button
        button = QPushButton("Update Record")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        name = self.student_name.text().strip()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text().strip()
        email = self.email.text().strip()
        group = self.student_group.text().strip()

        if not name or len(name) < 3:
            QMessageBox.warning(
                self,
                "Invalid Input",
                "Name needs at least 3 characters.",
            )
            return

            # Mobile num validation
        if not re.fullmatch(r"\+?\d{7,15}", mobile):
            QMessageBox.warning(
                self,
                "Invalid Input",
                "Please enter a valid phone number.",
            )
            return

            # Email validation
        if not re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            QMessageBox.warning(self, "Invalid Input", "Please provide a valid email.")
            return

            # Group validation
        if not group:
            QMessageBox.warning(self, "Invalid Input", "Group cannot be empty.")
            return

        connection = DataBaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE students SET name = %s, course = %s, mobile = %s, email = %s, student_group = %s WHERE id = %s",
            (
                name,
                course,
                mobile,
                email,
                group,
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


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Us")
        self.setFixedWidth(380)

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title = QLabel("Student Management System")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #a78bfa;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        description = QLabel(
            "<p align='center' style='font-size: 13px; color: #e2e8f0; line-height: 1.5;'>"
            "A modern, lightweight desktop application<br>"
            "built for seamless student record management.<br><br>"
            "Developed with <b>PyQt6</b> and <b>MySQL</b> by<br>"
            "<span style='color: #8b5cf6; font-weight: bold;'>Condrea Andrei </span>."
            "</p>"
        )
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Close btn
        close_btn = QPushButton("Close")
        close_btn.setFixedWidth(120)
        close_btn.clicked.connect(self.close)

        layout.addWidget(title)
        layout.addWidget(description)

        # Add spacer
        layout.addSpacing(15)
        layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
