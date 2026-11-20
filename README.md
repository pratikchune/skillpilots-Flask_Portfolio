# 🌐 Flask-Based Personal Portfolio Website

## 📌 Project Overview

The **Flask-Based Personal Portfolio Website** is a personal portfolio web application developed using Python Flask, HTML, and Internal CSS.

The main objective of this project is to create a professional online platform to showcase personal information, technical skills, academic projects, GitHub repositories, and resume details.

The website also provides a contact form through which visitors can communicate with the portfolio owner.

## 🎯 Project Objectives

- Develop a responsive and user-friendly personal portfolio website.
- Showcase technical skills and programming knowledge.
- Display academic and personal projects with descriptions.
- Provide direct links to GitHub project repositories.
- Allow visitors to view the resume online.
- Provide a contact form for communication.
- Deploy the portfolio website using a cloud hosting platform.

## ✨ Key Features

### 1. Home Section
- Displays personal introduction.
- Shows professional role and career interests.
- Provides navigation to different sections.

### 2. About Me
- Displays educational background.
- Introduces professional interests and career goals.

### 3. Technical Skills
Showcases technical skills such as:
- Python
- SQL
- Excel
- Power BI
- Pandas
- NumPy
- Matplotlib
- Flask
- HTML
- CSS

### 4. Projects Showcase
- Displays multiple academic and personal projects.
- Shows project descriptions and categories.
- Displays technologies used in each project.
- Provides individual project detail pages.

### 5. Resume Section
- Provides an option to view the resume in PDF format.

### 6. Contact Section
- Provides a contact form for visitors.
- Collects name, email, and message.
- Uses FormSubmit for email communication.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML5 | Webpage structure |
| Internal CSS3 | Website styling and responsiveness |
| Jinja2 | Dynamic HTML content rendering |
| Git | Version control |
| GitHub | Source code management |
| Render | Cloud deployment |
| FormSubmit | Contact form email handling |

## 📂 Project Structure

```text
Flask_Portfolio/
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
├── README.md
│
├── templates/
│   ├── index.html
│   └── project.html
│
└── static/
    └── files/
        └── resume.pdf
```

## ⚙️ Installation and Setup

Follow these steps to run the project on your local computer.

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Flask_Portfolio.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Flask_Portfolio
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

For Windows:

```powershell
.\venv\Scripts\activate
```

### Step 5: Install Required Libraries

```bash
python -m pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Open in Browser

Visit:

```text
http://127.0.0.1:5000/
```

The portfolio website will now run locally.

## 📦 Requirements

The project requires the following Python packages:

```text
Flask
gunicorn
```

Install them using:

```bash
python -m pip install flask gunicorn
```

## 🚀 Deployment

The application can be deployed using Render.

Deployment configuration:

- **Platform:** Render
- **Service Type:** Web Service
- **Runtime:** Python 3
- **Build Command:**

```bash
pip install -r requirements.txt
```

- **Start Command:**

```bash
gunicorn app:app
```

After successful deployment, Render provides a public URL to access the portfolio website.

## 📧 Contact Form Configuration

The contact form uses FormSubmit.

To activate it:

1. Open `templates/index.html`.
2. Find the FormSubmit action URL.
3. Replace `YOUR_EMAIL` with your email address.
4. Submit the form for the first time.
5. Complete the email activation process.

## 🔮 Future Enhancements

- Add a professional profile photograph.
- Add project screenshots and demonstrations.
- Implement a downloadable resume feature.
- Add social media and LinkedIn integration.
- Implement an admin dashboard for managing projects.
- Add a database to store contact messages.
- Improve animations and interactive UI components.

## 👨‍💻 Author

**Pratik Chune**

MCA Student | Aspiring Data Analyst | Python Developer

**Areas of Interest:**
- Data Analytics
- Python Programming
- Machine Learning
- Data Visualization
- Web Development

## 📄 License

This project is developed for educational and portfolio purposes.

---

⭐ If you find this project useful, consider giving the repository a star!
