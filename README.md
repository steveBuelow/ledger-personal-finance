# Ledger - Personal Finance App

**Ledger** is a full-stack personal finance application that replaces spreadsheet-based budget tracking with a persistent system built on Flask and PostgreSQL. It provides spending trend analytics, financial insights, and net worth tracking through monthly asset and liability reporting.

🔗 **[Live Demo](https://ledger-personal-finance-p626.onrender.com)**

![Ledger Dashboard Overview](docs/assets/dashboard-placeholder.png)
> *Placeholder: Add a high-resolution screenshot of your main dashboard showing the stats and charts.*

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

![Expense Tracking View](docs/assets/expenses-placeholder.png)
> *Placeholder: Add a screenshot of the Expense table and the "Add Expense" modal.*

### Net Worth & Asset Management
A persistent tracking system for long-term financial health.
* Monthly logging of liquid assets, investments, and physical assets.
* Liability tracking for loans and credit utilization.
* Automated net worth calculation from monthly logs.

![Net Worth View](docs/assets/networth-placeholder.png)
> *Placeholder: Add a screenshot of the Net Worth trend chart and history table.*

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

| Layer | Technologies |
| --- | --- |
| **Frontend** | HTML5, Vanilla JavaScript (ES6+), CSS3 |
| **Backend** | Python, Flask, Gunicorn |
| **Database** | PostgreSQL, Psycopg2, Supabase |
| **Security** | Werkzeug Security (PBKDF2), Secure Sessions |
| **Deployment** | Render, Git/GitHub |

## Architecture
```text
Frontend (Vanilla JS / Dynamic UI)
        ↓ REST API
Flask Backend (app.py / routes.py)
        ↓
Business Logic & Aggregation Layer (models.py)
        ↓
PostgreSQL Database