# Feature Store Implementation using FastAPI and SQLite

## Overview
This project implements a **lightweight Feature Store service** using **Python 3.9**, **FastAPI**, **SQLite**, and **Pandas**.  
The service supports registering raw data, computing versioned features, and serving feature vectors via REST APIs.

It demonstrates core Feature Store concepts such as **data ingestion**, **feature computation**, **versioning**, and **API-based feature serving**.

---

## Tech Stack
- Python 3.9  
- FastAPI  
- SQLite  
- Pandas  
- SQLAlchemy  
- Uvicorn  

---

## Features
- Register raw data per entity  
- Compute features with basic consistency checks  
- Automatic feature versioning  
- Serve feature vectors via REST APIs  
- SQLite-backed persistence  
- Auto-generated API documentation (Swagger / OpenAPI)  

---

## Project Structure
feature_store_python39/
│
├── app/
│ ├── init.py
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ └── feature_engineering.py
│
├── ingest_sample.py
├── requirements.txt
└── README.md


---

## Setup & Installation

### Clone the repository
```bash
git clone https://github.com/IpshitaKarmakar/feature-store.git
cd feature-store

Install dependencies
pip install -r requirements.txt


No virtual environment is required. Dependencies are managed via requirements.txt.

Running the Application

Start the FastAPI server from the project root directory:

python -m uvicorn app.main:app --reload


The application will be available at:

http://127.0.0.1:8000

API Documentation
FastAPI automatically generates interactive API documentation:

Swagger UI

http://127.0.0.1:8000/docs


OpenAPI JSON

http://127.0.0.1:8000/openapi.json

Usage Workflow
Step 1: Register Raw Data

POST /register_raw

{
  "entity_id": "demo_user",
  "value": 10
}


Repeat this request to add multiple raw values for the same entity.

Step 2: Compute Features

POST /compute_features/{entity_id}

Example:

/compute_features/demo_user


Response:

{
  "message": "Features computed",
  "version": 1
}

Step 3: Retrieve Feature Vector

GET /get_features/{entity_id}

Example response:

[
  {
    "entity_id": "demo_user",
    "feature_name": "mean_value",
    "feature_value": 20.4,
    "version": 1
  },
  {
    "entity_id": "demo_user",
    "feature_name": "sum_value",
    "feature_value": 102,
    "version": 1
  }
]

Feature Versioning

Each feature computation creates a new version

Enables reproducibility and tracking of feature changes

Multiple versions can exist for the same entity

Validation & Testing

APIs tested using Swagger UI

Verified with multiple entities and raw inputs

Proper error handling for missing raw data

Notes

SQLite database (feature_store.db) is created automatically at runtime

No external services are required

API documentation is generated dynamically by FastAPI

Author

Ipshita Karmakar
B.Tech (CSE) | Machine Learning & Backend Development
