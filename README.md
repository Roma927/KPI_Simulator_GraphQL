# KPI_Simulator_GraphQL

The **KPI Simulator GraphQL** is a backend system designed to simulate KPI (Key Performance Indicator) data generation. It provides a **GraphQL API** for managing simulators, allowing users to create, update, delete, and list simulators. Built with Django and Graphene-Django, this application is a robust solution for managing simulator data.

---

## Features

- **GraphQL API**:
  - **List all simulators**: Retrieve a list of all simulators.
  - **Create a new simulator**: Add a new simulator to the database.
  - **Update a simulator**: Modify an existing simulator.
  - **Delete a simulator**: Remove a simulator from the database.
- **Django Backend**: A robust backend built with Django.
- **Simulator Model**: Includes fields for `kpi_id`, `start_date`, and `interval`.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
- **Django 4.0 or higher**
- **Graphene-Django** (for GraphQL support)
- **PostgreSQL** (or any other database supported by Django)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Roma927/KPI_Simulator_GraphQL
   cd Kpi_simulator_GraphQL
   ```


4. **Set up the database**:
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the GraphQL API**:
   - Open your browser and navigate to `http://localhost:8000/graphql/`.
   - Use the GraphiQL interface to interact with the API.

---

## GraphQL API Examples

### List All Simulators
```graphql
query {
  allSimulators {
    id
    kpiId
    startDate
    interval
  }
}
```

### Create a New Simulator
```graphql
mutation {
  createSimulator(kpiId: 123, startDate: "2024-01-01T00:00:00Z", interval: "daily") {
    simulator {
      id
      kpiId
      startDate
      interval
    }
  }
}
```

### Update a Simulator
```graphql
mutation {
  updateSimulator(id: 1, kpiId: 456, interval: "hourly") {
    simulator {
      id
      kpiId
      startDate
      interval
    }
  }
}
```

### Delete a Simulator
```graphql
mutation {
  deleteSimulator(id: 1) {
    success
    message
  }
}
```

---

## Project Structure

```
Kpi_simulator_AirFlow/
├── kpl_simulator/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│   ├── schema.py          
├── simulator/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── manage.py
├── requirements.txt
└── README.md
```
