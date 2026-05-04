# Ledger - Personal Finance App

**Ledger** is a full-stack personal finance application that replaces spreadsheet-based budget tracking with a persistent system built on Flask and PostgreSQL. It provides spending trend analytics, financial insights, and net worth tracking through monthly asset and liability reporting.

## [Link for Deployed App](https://ledger-personal-finance-p626.onrender.com)

## Overview 
Ledger is a web application designed to provide a comprehensive, data-driven view of personal financial health. This application was built to handle 200+ budget expenses with persistent storage, secure authentication, and a modern, workflow-based interface.
This project focuses on:
* The management and visualization of persistent cloud databases
* RESTful backend design for complex data aggregation
* Stateful session handling and secure user data isolation
* Time-series data tracking for net worth and monthly reporting

---

## Key Features

### Comprehensive Expense Tracking
A centralized system for logging and categorizing daily financial transactions:
* Categorized income and expense logging
* Full CRUD lifecycle for over 200+ financial records
* Custom date-range filtering and dynamic querying

### Net Worth & Asset Management
A persistent tracking system for long-term financial health:
* Monthly logging of liquid assets, investments, and physical assets
* Liability tracking for loans and credit utilization
* Automated net worth calculation from monthly logs

### Financial Analytics Dashboard
Dynamic server-side data aggregation to visualize spending habits:
* Monthly spending trend analysis
* Category-based expense distribution
* Real-time calculations of discretionary vs. fixed spending

### Authentication & Security
Built with secure session handling to protect sensitive financial data:
* Password hashing and salting using Werkzeug (PBKDF2)
* Secure session cookies with SameSite=Lax
* Environment-based configuration for secure deployment

---

## Tech Stack

| Layer | Technologies |
| --- | --- |
| Frontend | HTML5, Vanilla JavaScript (ES6+), CSS3 |
| Backend | Python, Flask, Gunicorn |
| Database | PostgreSQL, Psycopg2 |
| Security | Werkzeug Security (PBKDF2), Secure Sessions |
| Deployment | Render, Git/GitHub |

## Architecture
```
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
``` Python
Net worth = SUM(Total Assets) - SUM(Total Liabilities)
```

### Expense Aggregation 
Server-side logic groups expenses by category and month to minimize payload size and improve frontend rendering speeds:
``` sql
SELECT category, SUM(amount)
FROM expenses
WHERE user_id = ? AND EXTRACT(MONTH FROM date) = ?
GROUP BY category;
```

---

## Development Highlights

### Advanced Database Queries 
Leveraged PostgreSQL to handle complex grouping and time-series queries, shifting the analytical workload from the client to the server for optimized performance.

### Data Visualization Readiness
Structured the RESTful API to serve clean, aggregated JSON payloads specifically designed to be easily consumed by frontend charting libraries or custom vanilla JS visualizations.

### Security-First Architecture
Implemented strict user-data isolation on the backend to ensure that financial records are completely decoupled and protected across different authenticated sessions.

---

## Project Structure
```
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
``` bash
git clone https://github.com/steveBuelow/ledger-personal-finance.git
cd ledger-personal-finance
pip install -r requirements.txt
python app.py
```

---

## About Me

I am a first-year Computer Science student at North Dakota State University focused on building production-oriented software systems, with a current core focus on Python 3 development.

Building Ledger allowed me to expand my backend engineering skills beyond standard CRUD applications, diving into data aggregation, time-series tracking, and designing APIs that handle sensitive relational data

### Resume Summary
Developed and deployed a full-stack personal finance application using Python, Flask, and PostgreSQL to track 200+ expenses and monthly asset/liability records. Engineered RESTful API endpoints with complex SQL aggregation to generate real-time spending analytics and net worth calculations, while implementing strict user-data isolation and secure authentication.
