# JobTrackr

JobTrackr is a web application designed to help users manage their job applications, resumes, and auto-fill job data using AI. The application integrates AI to extract skills from resumes and suggest job titles, reminders, and tracking features.

## Features

- **Job Application Management**: Users can add, track, and manage their job applications.
- **Resume Upload**: Users can upload their resumes for analysis.
- **AI Suggestions**: The application provides suggestions for job titles and skills based on the uploaded resume.
- **User Authentication**: Secure login and signup functionality using Firebase Auth or JWT.
- **Email Reminders**: Users can receive reminders about their job applications.
- **Application Timeline View**: Visual representation of application timelines.
- **Export to CSV**: Users can export their job application data.
- **Dark Mode Toggle**: Option for users to switch between light and dark themes.

## Project Structure

```
jobtrackr
├── client                # React frontend
│   ├── src
│   │   ├── components    # Reusable components
│   │   ├── pages         # Page components
│   │   ├── App.jsx       # Main application component
│   │   └── main.jsx      # Entry point for React app
├── server                # Node.js backend
│   ├── routes            # API route definitions
│   ├── controllers       # Business logic for routes
│   ├── models            # Mongoose models
│   ├── middleware        # Middleware functions
│   └── index.js         # Entry point for Node.js server
├── ai-service            # Python AI microservice
│   ├── app.py            # Entry point for AI service
│   └── utils
│       └── resume_parser.py # Utility functions for resume parsing
├── README.md             # Project documentation
└── .env                  # Environment variables
```

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url(will be provided later)>
   cd jobtrackr
   ```

2. **Frontend Setup**:
   - Navigate to the `client` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Start the development server:
     ```
     npm start
     ```

3. **Backend Setup**:
   - Navigate to the `server` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Start the server:
     ```
     node index.js
     ```

4. **AI Service Setup**:
   - Navigate to the `ai-service` directory.
   - Install dependencies (if using Flask):
     ```
     pip install Flask
     ```
   - Start the AI service:
     ```
     python app.py
     ```

## Usage

- Users can create an account and log in to manage their job applications.
- After logging in, users can upload their resumes to receive AI-generated suggestions.
- Users can track the status of their job applications and set reminders.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.