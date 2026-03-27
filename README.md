# 🚀 Lost & Found Portal with Chat System

## 📌 Overview

The **Lost & Found Portal** is a web-based application designed to help users report, search, and recover lost items efficiently. This platform connects people who have lost items with those who have found them, making the recovery process faster, simpler, and more reliable.

In addition to basic listing features, the system includes an integrated **chat functionality**, allowing users to communicate directly regarding specific items. This eliminates confusion and improves the chances of successful item recovery.

---

## 🎯 Features

### 🔐 User Authentication

* Secure user registration and login system
* Each user has a personalized dashboard

### 📦 Item Management

* Add lost or found items with details
* Upload item images
* Provide description, location, and date
* Categorize items for better organization

### 🔍 Search & Filter

* Search items using keywords
* Filter by category or location
* Easy-to-use interface for browsing

### 💬 Chat System

* One-to-one chat between users
* Item-based messaging (chat linked to a specific item)
* Clean and responsive chat UI
* Prevents duplicate messages using proper request handling

### 📱 Responsive Design

* Works on mobile and desktop devices
* Clean card-based UI for items

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite
* **Authentication:** Django Auth System

---

## ⚙️ Installation & Setup

1️⃣ Clone the repository

```bash
git clone https://github.com/01xnikhil/lostfound.git
cd lostfound
```

2️⃣ Create virtual environment

```bash
python -m venv venv

windows
venv\Scripts\activate
Mac/ios
Source venv\Scripts\activate
```

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5️⃣ Start server

```bash
python manage.py runserver
```

---

## 📂 Project Structure

```
lostfound/
│── chat/                    # Chat system
│── items/                   # Lost & Found items
│── users/                   # Authentication
│── templates/               # HTML files
│── static/                  # CSS, JS, Images
│── db.sqlite3
```

---

## 💡 Key Highlights

* Full-stack Django project
* Real-world problem solving application
* Chat system integrated without WebSockets (simple & stable)
* Clean UI and user-friendly experience
* Scalable for future improvements

---

## 🔮 Future Enhancements

* 🔔 Notification system
* 📲 Mobile app version
* 🤖 AI-based item matching
* 🌍 Multi-language support
* ☁️ Cloud deployment

---

## 👨‍💻 Author

**Nikhil Mishra**

* Passionate about Web Development & Problem Solving
* Learning Full Stack Development

---

## Project Screenshot

### Home page before login
<img width="1910" height="966" alt="Screenshot 2026-03-27 115547" src="https://github.com/user-attachments/assets/dc34bdd9-e9fb-469f-9c0d-19a8755f7e46" />

### Home Page after login
<img width="1915" height="960" alt="Screenshot 2026-03-27 114822" src="https://github.com/user-attachments/assets/740cbddb-ba28-4b13-8713-1890c984c985" />

### login & signup
<img width="1905" height="960" alt="Screenshot 2026-03-27 114951" src="https://github.com/user-attachments/assets/dc599702-6a9e-43fd-b640-3c84c98ef68c" />
<img width="1907" height="964" alt="Screenshot 2026-03-27 115024" src="https://github.com/user-attachments/assets/3eca21b3-4f11-4fe2-b5e6-67476ba83bfc" />

### Add/Report items
<img width="1905" height="965" alt="Screenshot 2026-03-27 114929" src="https://github.com/user-attachments/assets/8e7030f2-d743-405a-8aa6-5c5ec2897125" />

### All items
<img width="1910" height="980" alt="Screenshot 2026-03-27 114849" src="https://github.com/user-attachments/assets/ca9d980d-eb5a-4c51-99c7-635c4f168149" />

### Chat Page
<img width="1908" height="963" alt="Screenshot 2026-03-27 115055" src="https://github.com/user-attachments/assets/45674562-7204-4f3d-935d-9b1998024cd9" />

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
