CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    class_name TEXT NOT NULL,
    role TEXT DEFAULT 'student',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    profile_image_url TEXT
);

-- Add this to learntogether.sql
CREATE TABLE assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    class_name TEXT,
    assignment_name TEXT,
    deadline DATETIME,
    reminder_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES students(id)
);


-- -- Table for Classes
-- CREATE TABLE classes (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     user_id INTEGER,
--     class_name TEXT,
--     schedule TEXT,
--     UNIQUE(user_id, class_name)
-- );

-- -- Table for Assignments
-- CREATE TABLE assignments (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     user_id INTEGER,
--     class_id INTEGER,
--     assignment_name TEXT,
--     deadline DATETIME,
--     UNIQUE(user_id, assignment_name)
-- );

-- .save and .read: Save and load SQL commands from a file.

-- .save filename: Save the current SQLite3 session to a file.
-- .read filename: Read and execute SQL commands from a file.
-- Example: .save my_session.sql
-- .read another_file.sql