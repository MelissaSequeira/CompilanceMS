
# Compliance Support System (CMS)

The **Compliance Support System (CMS)** is a web-based platform built to support the compliance management needs of finance businesses. It enables firms to track, assess, and manage their regulatory responsibilities effectively using a streamlined and user-friendly dashboard.

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
- ![image](https://github.com/user-attachments/assets/d3c1399c-dbe4-4924-92c4-4364f00b7685)

- Registration Page
- ![image](https://github.com/user-attachments/assets/35f0c25e-8c3a-4e79-8f10-f62530149b67)
  
- Home Page
- ![image](https://github.com/user-attachments/assets/50ec4828-e11e-42be-bead-dc85cd4d97da)

- Dashboard (Risk Graph + Pie Chart)
- ![image](https://github.com/user-attachments/assets/ac81ff36-7623-4ffb-bf70-2eeaf3ee497b)

- Add Task Form
- ![image](https://github.com/user-attachments/assets/355be1cd-6b07-4944-bead-aca7d0146f49)

- Checklist Interface
- ![image](https://github.com/user-attachments/assets/42c50a64-0ef6-44a5-9ddd-9feec6492480)

- Complaint Registration & Viewer
- ![image](https://github.com/user-attachments/assets/88c5d8b2-d9fa-40da-807a-f8597aa6eda9)
- ![image](https://github.com/user-attachments/assets/bdaf7153-777f-489e-996a-b74aeb25b565)

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

5. Visit [`(https://compilancems.onrender.com)`](https://compilancems.onrender.com) in your browser.

---

## 📌 Conclusion

The Compliance Support System offers a tailored solution for finance companies to manage compliance proactively. By providing real-time insights, task management, and complaint tracking, it simplifies adherence to regulations while supporting business growth and accountability.

---

## 📫 Contact

📧 Email: melissasequeira572@gmail.com


