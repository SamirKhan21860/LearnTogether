-- Students
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    class_name TEXT NOT NULL,
    role TEXT DEFAULT 'student',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    profile_image_url TEXT
);

-- Complaints and Requests
CREATE TABLE complaints_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    submission_type TEXT NOT NULL,
    category TEXT NOT NULL,
    subject TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students (id)
);
-- -- Announcements
CREATE TABLE announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author TEXT
);

-- -- Upcoming Events
-- CREATE TABLE upcoming_events (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     event_name TEXT NOT NULL,
--     event_date DATE NOT NULL,
--     location TEXT,
--     description TEXT
-- );

-- -- Assignment Reminders
CREATE TABLE assignment_reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    description TEXT NOT NULL,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES students(id)
);

-- -- Exam Schedules
-- CREATE TABLE exam_schedules (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     exam_name TEXT NOT NULL,
--     exam_date DATE NOT NULL,
--     exam_time TIME NOT NULL,
--     exam_room TEXT
-- );

-- -- Important School Updates
-- CREATE TABLE school_updates (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     update_title TEXT NOT NULL,
--     update_content TEXT NOT NULL,
--     posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- -- Scholarship Opportunities
-- CREATE TABLE scholarship_opportunities (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     scholarship_title TEXT NOT NULL,
--     deadline DATE NOT NULL,
--     requirements TEXT NOT NULL
-- );

-- -- Internship/Job Opportunities
-- CREATE TABLE job_opportunities (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     opportunity_title TEXT NOT NULL,
--     company_name TEXT NOT NULL,
--     description TEXT NOT NULL,
--     posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );



-- .save and .read: Save and load SQL commands from a file.

-- .save filename: Save the current SQLite3 session to a file.
-- .read filename: Read and execute SQL commands from a file.
-- Example: .save my_session.sql
-- .read another_file.sql