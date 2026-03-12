# Configurable Workflow Decision System

A modular decision-processing system built using **FastAPI** that evaluates requests using configurable rules, executes workflow states, logs audit information, and exposes REST APIs for processing and querying requests.

This project was built as part of the **ScoreMe Hackathon Assignment**.

---

# System Overview

The system processes incoming requests and determines a decision (`approve`, `reject`, or `manual_review`) based on configurable rules.

Each request goes through a workflow pipeline:

1. Request received
2. Input validation
3. External credit service check
4. Rule evaluation
5. Workflow state execution
6. Audit logging
7. Result storage

---

# Architecture

```
Client
   ↓
FastAPI REST API
   ↓
Input Validation (Pydantic)
   ↓
External Service Simulation
   ↓
Rule Engine
   ↓
Workflow Engine
   ↓
Audit Logger
   ↓
State Storage (In-memory DB)
```

---

# Project Structure

```
decision-workflow-system
│
├── config
│   └── rules.json                # Configurable decision rules
│
├── database
│   └── db.py                     # In-memory request storage
│
├── tests
│   └── test_decision.py          # Automated tests
│
├── main.py                       # FastAPI application
├── rule_engine.py                # Rule evaluation logic
├── workflow.py                   # Workflow state transitions
├── audit_logger.py               # Audit logging system
├── external_service.py           # External dependency simulation
│
├── README.md
└── .gitignore
```

---

# Features

• REST API for decision processing
• Configurable rules via JSON
• Workflow state tracking
• Audit logging for every request
• Idempotent request handling (duplicate request protection)
• External service simulation with retry mechanism
• Input validation using Pydantic
• Automated tests for rule engine

---

# Installation

Clone the repository:

```
git clone https://github.com/YashDawange/decision-workflow-system.git
cd decision-workflow-system
```

Install dependencies:

```
pip install fastapi uvicorn pytest
```

---

# Running the Application

Start the FastAPI server:

```
python -m uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation (Swagger UI)

FastAPI automatically generates interactive API documentation.

Open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

This interface allows you to:

• Test the APIs directly from the browser
• Send requests to `/request` endpoint
• Retrieve request status using `/request/{request_id}`

---

# API Endpoints

## Submit Request

POST `/request`

Example Request

```
{
  "request_id": "REQ001",
  "income": 60000,
  "credit_score": 720
}
```

Example Response

```
{
  "decision": "approve",
  "history": [
    "RECEIVED",
    "VALIDATED",
    "RULE_EVALUATED",
    "APPROVE",
    "COMPLETED"
  ]
}
```

---

## Get Request Status

GET `/request/{request_id}`

Example:

```
GET /request/REQ001
```

Returns the stored decision and workflow history.

---

# Decision Rules

Rules are configurable in:

```
config/rules.json
```

Example rules:

```
[
  {
    "condition": "credit_score < 600",
    "decision": "reject"
  },
  {
    "condition": "income > 50000 and credit_score > 700",
    "decision": "approve"
  }
]
```

If no rule matches, the request is marked for:

```
manual_review
```

---

# Testing

Run automated tests using:

```
pytest
```

The test suite verifies rule engine correctness.

---

# Error Handling

The API includes input validation using Pydantic.

Example invalid request:

```
{
  "request_id": "REQ100",
  "income": "hello",
  "credit_score": "abc"
}
```

Returns:

```
422 Validation Error
```

---
