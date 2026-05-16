# Cloud-Based DevOps Automation System

## 📌 Overview
This project demonstrates a complete beginner-friendly DevOps workflow by building a containerized Flask web application and automating its deployment using CI/CD pipelines. It integrates version control, containerization, and cloud deployment practices used in real-world software development.

---

## 🚀 Project Objective
To understand and implement a full DevOps lifecycle including:
- Application development using Flask
- Containerization using Docker
- Continuous Integration using GitHub Actions
- Cloud deployment using Render

---

## 🛠️ Technologies Used
- Python
- Flask
- Docker
- GitHub
- GitHub Actions (CI/CD)
- Render (Cloud Deployment)

---

## 📁 Project Structure
cloud-devops-project/
│
├── app.py                  # Flask web application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── .gitignore             # Ignored files for Git
├── README.md              # Project documentation
│
└── .github/
    └── workflows/
        └── main.yml        # CI/CD pipeline (GitHub Actions)

---

## ⚙️ How It Works

### 1. Application Layer
A simple Flask web app that displays:
- System status
- Current timestamp
- Host machine information

---

### 2. Containerization (Docker)
The application is containerized using Docker to ensure consistent runtime across environments.

Workflow:
Dockerfile → Docker Image → Docker Container

---

### 3. CI/CD Pipeline (GitHub Actions)
On every push to the `main` branch:
- GitHub Actions triggers automatically
- Builds Docker image
- Ensures code is production-ready

---

### 4. Deployment (Render)
The application is deployed on Render, which:
- Pulls code from GitHub
- Builds Docker image
- Hosts the application on a live URL

---

## 🔄 CI/CD Workflow
Flask App → GitHub → GitHub Actions → Docker Build → Render Deployment → Live Application

---

## 🌐 Features
- Containerized web application
- Automated CI pipeline
- Cloud deployment
- Real-time system info display
- Production-like DevOps workflow

---

## 📷 Output Example
- Web page displays:
  - Application status
  - Current system time
  - Hostname of server

---

## 🧠 Key Learnings
- Basics of DevOps lifecycle
- Docker containerization
- CI/CD automation using GitHub Actions
- Cloud deployment using Render
- Git version control workflow

---

## 📌 Future Improvements
- Add monitoring (Prometheus/Grafana)
- Add automated testing in CI pipeline
- Deploy using Kubernetes
- Add API endpoints instead of static HTML response

---

## 👨‍💻 Author
Beginner DevOps Project – Built for learning CI/CD, Docker, and cloud deployment fundamentals.

---

## 📌 Note
This project was deployed using Render during development and demonstrates a full CI/CD pipeline from code to cloud.
