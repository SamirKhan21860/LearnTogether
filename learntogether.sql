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

-- .save and .read: Save and load SQL commands from a file.

-- .save filename: Save the current SQLite3 session to a file.
-- .read filename: Read and execute SQL commands from a file.
-- Example: .save my_session.sql
-- .read another_file.sql