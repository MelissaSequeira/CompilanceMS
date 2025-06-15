
# Compliance Support System (CMS)

A mini project submitted as part of the Bachelor of Engineering in Information Technology at Fr. Conceicao Rodrigues Institute of Technology.

## 🚀 Overview

The **Compliance Support System (CMS)** is a web-based platform built to support the compliance management needs of finance businesses. It enables firms to track, assess, and manage their regulatory responsibilities effectively using a streamlined and user-friendly dashboard.

## 👥 Team Members

- **Anushka Uttam Sarkar** (5022153)  
- **Melissa Rozario Sequeira** (5022157)  
- **Mereena Sarah Varghese** (5022165)  
- **Sukhada Vedang Wadodkar** (5022166)  

**Guide:** Prof. Sharlene Rebeiro

---

## 📌 Features

### 🔐 Authentication
- User **login** and **registration** support
- Session-based security to maintain user context

### 📊 Dashboard
- Displays **Risk Statistics** using a bar graph
- Displays **Task Completion Summary** using a pie chart
- Shows all compliance-related tasks and their statuses

### 📝 Task Management
- Add compliance tasks with activity name, duration, and risk percentage
- Update or remove existing tasks
- Mark tasks as "Done" or "Undone"

### ✅ Checklist
- Tracks progress of activities
- Visual interface to mark task status and edit entries

### 📣 Complaints Management
- Submit compliance-related complaints
- View and delete previous complaints

---

## 🛠️ Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Frontend   | HTML, CSS         |
| Backend    | Python, Flask     |
| Database   | SQLite            |
| Data Visuals | Matplotlib       |

---

## 🧠 System Flow

1. **User Registration/Login**  
2. Redirected to **Dashboard**  
3. Users can:
   - Add Tasks
   - View Risk Graphs
   - Use Checklist
   - Submit/View Complaints
4. Logout redirects to login screen.

---

## 📁 File Structure

```
├── templates/
│   ├── index.html
│   ├── login.html
│   └── registration.html
├── static/
│   ├── style.css
│   └── loandreg.css
├── pywork.py
├── README.md
```

---

## 🖥️ GUI Screenshots

- Login Page  
- Registration Page  
- Dashboard (Risk Graph + Pie Chart)  
- Add Task Form  
- Checklist Interface  
- Complaint Registration & Viewer

> Refer to the GUI section in the report for visuals.

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/compliance-support-system.git
   cd compliance-support-system
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install flask flask_sqlalchemy matplotlib
   ```

4. Run the app:
   ```bash
   python pywork.py
   ```

5. Visit `http://localhost:5000` in your browser.

---

## 📌 Conclusion

The Compliance Support System offers a tailored solution for finance companies to manage compliance proactively. By providing real-time insights, task management, and complaint tracking, it simplifies adherence to regulations while supporting business growth and accountability.

---

## 📫 Contact

📧 Email: melissasequeira572@gmail.com


