-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS school;
USE school;

-- Create the students table with all required columns
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    course VARCHAR(100) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    student_group VARCHAR(50) NOT NULL
);

-- (Optional) Insert a few demo records so the app isn't empty on first run
INSERT INTO students (name, course, mobile, email, student_group) VALUES
('Silviu Hagi', 'Computer Science', '0722112233', 'silviu.hagi@student.com', 'CS Group 2'),
('Emma Watson', 'Biology', '0744123123', 'emma.watson@university.edu', 'Bio Gr 1'),
('Mateo Garcia', 'Math', '0755987654', 'mateo.garcia@gmail.com', 'Math Gr 1');