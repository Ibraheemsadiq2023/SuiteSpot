# SuiteSpot Project Roadmap

This roadmap outlines the project structure, upcoming milestones, and feature development plan for SuiteSpot.

## 1. Project Overview

SuiteSpot is a Python-based desktop application for hotel management using Tkinter for the GUI and SQL for data storage. It supports role-based access, room & booking management, customer tracking, and reporting.

## 2. Repository Structure

```
SuiteSpot/
├── README.md
├── ROADMAP.md             # This roadmap document
├── requirements.txt
├── config.py
├── main.py
│
├── gui/
│   ├── __init__.py
│   ├── login_dialog.py
│   ├── main_window.py
│   ├── booking_dialog.py
│   ├── customer_dialog.py
│   ├── room_dialog.py
│   └── admin_dashboard.py
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── schema.sql
│
├── logic/
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   └── hotel_operations.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── resources/
│   ├── icons/
│   └── images/
│
├── logs/
│   └── suite_spot.log
│
└── tests/
    ├── __init__.py
    ├── test_auth.py
    ├── test_db.py
    ├── test_models.py
    └── test_gui.py
```

## 3. Milestones & Timeline

| Milestone                     | Description                                         | Target Date     |
|-------------------------------|-----------------------------------------------------|-----------------|
| Initial Setup                 | Repo scaffolding, README, requirements, config      | 2025-05-05      |
| Database Schema               | Define and test schema.sql, implement `db.py`       | 2025-05-10      |
| Authentication Module         | Build `auth.py`, login GUI, password hashing        | 2025-05-15      |
| Core GUI Layout               | Create main_window.py, navigation flow              | 2025-05-20      |
| Room & Customer Management    | Implement dialogs and logic for rooms & customers   | 2025-05-25      |
| Booking Workflow              | Integrate booking_dialog.py with backend operations | 2025-05-30      |
| Reporting Module              | Admin dashboard reports (occupancy, revenue)        | 2025-06-05      |
| Testing & QA                  | Write and run pytest suites for all components      | 2025-06-10      |
| Documentation & Release       | Finalize docs, tag v1.0.0, publish release          | 2025-06-15      |

**Note:** Dates are tentative and adjustable based on progress.

## 4. Feature Roadmap

- **v1.0.0**: Core features (auth, room/customer mgmt, bookings, basic reports)
- **v1.1.0**: Enhanced reporting (custom date ranges, export to CSV/PDF)
- **v1.2.0**: Multi-database support (GUI choice between SQLite/MySQL/PostgreSQL)
- **v2.0.0**: Networked mode (client-server architecture for multiple front-ends)
- **v2.1.0**: Mobile companion app (read-only reporting dashboard)

## 5. Contribution Guidelines

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute, code style, and testing requirements.
