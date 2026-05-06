# Ledger - Personal Finance App

**Ledger** is a full-stack personal finance application that replaces spreadsheet-based budget tracking with a persistent system built on Flask and PostgreSQL. It provides spending trend analytics, financial insights, and net worth tracking through monthly asset and liability reporting.

🔗 **[Live Demo](https://ledger-personal-finance-p626.onrender.com)**

![Ledger Dashboard Overview](<img width="1019" height="1096" alt="ledger-dashboard" src="https://github.com/user-attachments/assets/d1252d02-e4dd-4975-a63a-db5cce889a5c" />)

## Overview 
Ledger is a web application designed to provide a comprehensive, data-driven view of personal financial health. This application was built to handle hundreds of budget expenses with persistent storage, secure authentication, and a modern, workflow-based interface.

This project focuses on:
* The management and visualization of persistent cloud databases.
* RESTful backend design for complex data aggregation.
* Stateful session handling and secure user data isolation.
* Time-series data tracking for net worth and monthly reporting.

---

## Key Features

### Comprehensive Expense Tracking
A centralized system for logging and categorizing daily financial transactions.
* Categorized income and expense logging.
* Full CRUD lifecycle for over 200+ financial records.
* Custom date-range filtering and dynamic querying.

![Expense Tracking View](<img width="1010" height="684" alt="ledger-expenses-ui" src="https://github.com/user-attachments/assets/5ef44fa0-c25a-4659-9a44-e93b929e8cf5" />)

### Net Worth & Asset Management
A persistent tracking system for long-term financial health.
* Monthly logging of liquid assets, investments, and physical assets.
* Liability tracking for loans and credit utilization.
* Automated net worth calculation from monthly logs.

![Net Worth View](<img width="1010" height="969" alt="ledger-net-worth-ui" src="https://github.com/user-attachments/assets/12699383-81a1-470d-9dd0-8f9eed632199" />)

### Financial Analytics Dashboard
Dynamic server-side data aggregation to visualize spending habits.
* Monthly spending trend analysis.
* Category-based expense distribution.
* Real-time calculations of discretionary vs. fixed spending.

### Authentication & Security
Built with secure session handling to protect sensitive financial data.
* Password hashing and salting using Werkzeug (PBKDF2).
* Secure session cookies with `SameSite=Lax`.
* Environment-based configuration for secure deployment.

---

## Tech Stack
```
| Layer | Technologies |
| --- | --- |
| **Frontend** | HTML5, Vanilla JavaScript (ES6+), CSS3 |
| **Backend** | Python, Flask, Gunicorn |
| **Database** | PostgreSQL, Psycopg2, Supabase |
| **Security** | Werkzeug Security (PBKDF2), Secure Sessions |
| **Deployment** | Render, Git/GitHub |
```

---

## Architecture
```text
Frontend (Vanilla JS / Dynamic UI)
        ↓ REST API
Flask Backend (app.py / routes.py)
        ↓
Business Logic & Aggregation Layer (models.py)
        ↓
PostgreSQL Database
```

---

## Data Model & Logic

### Net Worth Calculation

Net worth is dynamically calculated by querying the most recent monthly asset and liability logs:
```Python
Net worth = SUM(Total Assets) - SUM(Total Liabilities)
```

### Expense Aggregation
Server-side logic groups expenses by category and month to minimize payload size and improve frontend rendering speeds:
```SQL
SELECT category, SUM(amount)
FROM expenses
WHERE user_id = ? AND EXTRACT(MONTH FROM date) = ?
GROUP BY category;
Development Highlights
Advanced Database Queries: Leveraged PostgreSQL to handle complex grouping and time-series queries, shifting the analytical workload from the client to the server for optimized performance.
```

---

## Development Highlights
* **Advanced Database Queries:** Leveraged PostgreSQL to handle complex grouping and time-series queries, shifting the analytical workload from the client to the server for optimized performance.

* **Data Visualization Readiness:** Structured the RESTful API to serve clean, aggregated JSON payloads specifically designed to be easily consumed by frontend charting libraries.

* **Security-First Architecture:** Implemented strict user-data isolation on the backend to ensure that financial records are completely decoupled and protected across different authenticated sessions.

---

## Future Roadmap (Summer 2026)
* [ ] **Frontend Modernization:** Refactoring the current vanilla HTML/JS UI into a React application to handle state management more effectively as the platform scales.

* [ ] **Infrastructure Upgrade:** Migrating the database architecture to utilize AWS RDS for enterprise-grade scalability and performance.

---

## Project Structure
```Plaintext
Ledger/
│
├── static/              # CSS, UI assets, and client-side JS
├── templates/           # HTML frontend
├── app.py               # Application entry point
├── routes.py            # REST API endpoints for transactions & analytics
├── models.py            # Business logic + DB operations
├── db.py                # Database connection layer
└── requirements.txt     # Dependencies
```

---

## Installation
```Bash
git clone [https://github.com/steveBuelow/ledger-personal-finance.git](https://github.com/steveBuelow/ledger-personal-finance.git)
cd ledger-personal-finance
pip install -r requirements.txt
python app.py
```

---

## About Me
I am a Computer Science student at North Dakota State University focused on building production-oriented software systems, with a current core focus on Python 3 development.

Building Ledger allowed me to expand my backend engineering skills beyond standard CRUD applications, diving into data aggregation, time-series tracking, and designing APIs that handle sensitive relational data.

### Resume Summary

Developed and deployed a full-stack personal finance application using Python, Flask, and PostgreSQL to track 200+ expenses and monthly asset/liability records. Engineered RESTful API endpoints with complex SQL aggregation to generate real-time spending analytics and net worth calculations, while implementing strict user-data isolation and secure authentication.
