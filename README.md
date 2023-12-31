# LearnTogether

#### Video Demo: [Your Video URL Here]

#### Description:

LearnTogether is an innovative web application designed to enhance students' interest and engagement in learning and studies. The platform provides a centralized space for students to access various features, making their educational journey more enjoyable and interactive.

## Features:

### 1. Announcements
Stay informed about important updates and announcements from teachers or administrators. The Announcements section ensures that students are aware of any critical information related to their courses.

### 2. Class Timing
Organize your schedule effectively with the Class Timing feature. Get details about class timings, subjects, and other relevant information, helping you manage your time efficiently.

### 3. Assignments
Access and submit assignments through a user-friendly interface. The Assignments section streamlines the process of sharing practical details and important tasks, making it easier for students to stay on top of their coursework.

### 4. Study Materials
Explore a curated collection of study materials, categorized by subjects and age groups. The Study Materials feature is designed to provide additional learning resources, fostering a self-study and e-learning environment.

### 5. Scholarship Opportunities
Discover scholarship and job opportunities through the Scholarship Opportunities section. This feature helps students explore potential career paths and educational support outside the regular curriculum.

### 6. Exams
Stay prepared for upcoming exams with the Exam Schedules feature. Access detailed information about exam names, dates, times, and rooms, ensuring you are ready for your assessments.

## Project Structure:

- **app.py**: The main Flask application file that handles routes, database connections, and other server-side logic.
- **helpers.py**: Contains functions for querying data from the database, such as fetching study materials, announcements, and exam schedules.
- **index.html**: The main HTML template that structures the home page, including the navigation bar and content sections.
- **announcements.html, classTiming.html, assignments.html, studyMaterials.html, exams.html**: Individual HTML templates for specific sections, displaying relevant data and providing a consistent user experience.

## Usage:

1. Clone the repository: `git clone https://github.com/SamirKhan21860/LearnTogether.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python app.py`
4. Access the application in your web browser at `http://localhost:5000`

## Additional Information:

LearnTogether is built using technologies such as Flask, Python, Jinja, and Tailwind CSS. The application aims to create a collaborative and engaging learning environment for students, promoting effective communication and resource sharing.

Feel free to explore the various features and contribute to the continuous improvement of LearnTogether. Happy learning!