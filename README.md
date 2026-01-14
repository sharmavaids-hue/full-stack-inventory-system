# 🏭 Full-Stack Enterprise Inventory Analytics System

A robust, microservices-style Full-Stack application designed to manage, track, and visualize enterprise inventory data in real-time. This project integrates a **Java Spring Boot** backend for transactional integrity with a **Python Streamlit** frontend for interactive Business Intelligence (BI) analytics, all backed by a persistent **PostgreSQL** database running in **Docker**.

## 🚀 Key Features

* **RESTful API Architecture:** Decoupled backend handling CRUD operations via secure endpoints.
* **Interactive BI Dashboard:** Real-time analytics using **Streamlit** and **Plotly** to visualize stock levels, asset value distribution, and category metrics.
* **Bulk Data Ingestion:** Automated CSV parsing pipeline allowing users to upload mass inventory data, which is mapped and synchronized to the database.
* **Search & Filtering:** Server-side filtering logic implemented with custom Spring Data JPA queries for optimized performance.
* **Data Export:** Automated reporting allowing stakeholders to export processed data to CSV/Excel for external analysis.

## 🛠 Tech Stack

### Backend (The Core)
* **Language:** Java 17
* **Framework:** Spring Boot (Web, Data JPA)
* **Database:** PostgreSQL 15
* **Containerization:** Docker

### Frontend (The Analytics)
* **Language:** Python 3.10+
* **Framework:** Streamlit
* **Data Processing:** Pandas
* **Visualization:** Plotly Express

---

## 🏗 Architecture Overview

1.  **Frontend:** The user interacts with the Python Streamlit dashboard.
2.  **API Layer:** Python sends HTTP requests (GET/POST/DELETE) to the Java Spring Boot Controller.
3.  **Service Layer:** Java processes the request and enforces business logic.
4.  **Data Layer:** Hibernate/JPA translates Java objects into SQL queries for the PostgreSQL database.

---

## 📸 Screenshots

### 1. The Interactive Dashboard
*(Add a screenshot of your main "Overview" tab here)*

### 2. Advanced Analytics & Charts
*(Add a screenshot of your "Advanced Analytics" tab with the donut chart here)*

---

## 💻 How to Run This Project

### Prerequisites
* Java JDK 17+
* Python 3.10+
* Docker Desktop

### 1. Start the Database
```bash
docker run --name inventory-db -e POSTGRES_PASSWORD=secret -d -p 5432:5432 postgres