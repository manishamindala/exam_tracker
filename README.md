# 🎓 Study Sphere - Exam Tracker & Smart Alarms

Study Sphere is a full-stack Flask application designed to help students manage their exam schedules and stay on top of their study sessions with integrated alarms and a visual calendar.

---

## 🚀 Live Demo
You can access the live application here:  
👉 **[https://study-sphere-0izv.onrender.com](https://study-sphere-0izv.onrender.com)**

---

## ✨ Features
* **User Authentication**: Secure Login and Sign-up system using `Flask-Login` and `Bcrypt` password hashing.
* **Exam Dashboard**: Add, track, and delete upcoming exams with an automatic "days left" countdown.
* **Mission Alarms**: Create custom study alarms with audio notifications to stay focused.
* **Calendar View**: A visual grid to see your upcoming exam deadlines at a glance.
* **Responsive Design**: A modern, clean UI built with **Bootstrap 5** for desktop and mobile compatibility.

---

## 🛠️ Tech Stack
* **Backend**: Python (Flask)
* **Database**: SQLAlchemy (SQLite for development / PostgreSQL ready)
* **Frontend**: HTML5, CSS3, JavaScript (Bootstrap 5)
* **Deployment**: Render & GitHub Actions

---

## 📦 Installation & Local Setup

If you want to run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/manishamindala/exam_tracker.git](https://github.com/manishamindala/exam_tracker.git)
   cd exam_tracker
Create a virtual environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
python app.py
The app will be available at http://127.0.0.1:5000.

🔑 Default Credentials (for testing)
The application automatically seeds an admin account for easy testing:

Email: admin@test.com

Password: admin123

📄 License
This project is open-source and available under the MIT License.


### 💡 Quick steps to finish:
1. Open **VS Code**.
2. Create a file named **`README.md`** (if you haven't already).
3. **Paste** the code above.
4. **Save, commit, and push**:
   ```powershell
   git add README.md
   git commit -m "Complete project documentation"
   git push origin main
