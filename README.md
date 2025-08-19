🏆 Online Judge Platform

An Online Judge system built with Django that allows users to practice coding problems, compile & run code in multiple languages, receive AI-powered suggestions, and track their progress. Admins can manage problems easily through the Django Admin Panel.

✨ Features
👤 User Side

🔐 Authentication – Secure login & signup required to access problems and profiles.

📚 Problem Set – Explore coding problems with detailed descriptions, constraints, and examples.

💻 Code Editor –

Supports multiple languages (C++, Python, Java, etc.).

Run code with custom inputs.

Submit solutions to get verdicts (Accepted, Wrong Answer, Runtime Error, etc.).

🤖 AI Suggestions – Receive hints for incorrect solutions or optimization tips for accepted ones.

📊 User Profile – Track number of problems solved and progress history.

🛠️ Admin Side

🔑 Django Admin Panel (superuser only).

✍️ Create & Manage Problems – Add problem statements, constraints, and test cases.

⚙️ Full Control – Only authorized admins can manage the problem database.

🚀 Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript (integrated with Django templates)

Database: SQLite (default, can switch to PostgreSQL/MySQL)

Compiler Integration: Custom code execution environment (Docker/Sandboxed)

AI Suggestions: Integrated with an AI model for hints & optimizations

📸 Walkthrough
https://www.loom.com/share/e613f2506a934bdd88b08d88e0a9b014?sid=fe132661-5843-4508-b199-0b97826d6798

⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/online-judge.git
cd online-judge

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Create Superuser (for Admin Panel)
python manage.py createsuperuser

6. Run Server
python manage.py runserver


Project will be live at http://127.0.0.1:8000/

🔑 Usage

Go to homepage → Sign up / login.

Explore problem list and start solving.

Submit code to see verdicts.

Visit profile to track progress.

Superusers: /admin for managing problems.

📌 Future Improvements

📊 Add leaderboard & ranking system.

📂 Add discussion forum for problem-solving.

🔒 Improve code execution sandbox for security.

