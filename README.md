# Portfolio Tracker

A simple, extendable web application to manage and track financial assets in your portfolio. Built with FastAPI and SQLModel, it provides core CRUD operations and is designed to evolve with features like authentication, analytics, and performance optimizations using Rust microservices.

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Setup & Installation](#setup--installation)
* [Usage](#usage)
* [API Endpoints](#api-endpoints)
* [Project Structure](#project-structure)
* [Roadmap & Future Enhancements](#roadmap--future-enhancements)
* [Contributing](#contributing)
* [License](#license)

## Features

**Core**

* Add and list assets (symbol, quantity, average price)
* Input validation with Pydantic
* SQLite database (switchable to PostgreSQL via `DATABASE_URL`)

**Upcoming**

* User authentication and permissions
* Portfolio valuation endpoints (current market value, profit/loss)
* Background tasks for fetching live prices
* Data visualization dashboard
* Dockerization and CI/CD pipeline
* Rust microservice for performance-critical calculations
* Unit and integration tests
* Deployment to cloud (e.g., Fly.io, Render)

## Tech Stack

* **Backend:** FastAPI, SQLModel, Uvicorn
* **Database:** SQLite (development), PostgreSQL (production)
* **Env Management:** python-dotenv
* **HTTP Requests:** requests (for external price data)

## Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/zlizzle/portfolio-tracker.git
   cd portfolio-tracker
   ```
2. **Create & activate virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment**

   * Copy the template:

     ```bash
     cp .env.example .env
     ```
   * Edit `.env` and set your variables (e.g., `DATABASE_URL=sqlite:///./portfolio.db`).
5. **Run the app**

   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

* Open your browser at `http://127.0.0.1:8000` to view the root docs.
* Use Swagger UI at `http://127.0.0.1:8000/docs` for interactive API exploration.

## API Endpoints

| Method | Path       | Description               |
| ------ | ---------- | ------------------------- |
| POST   | `/assets/` | Create a new asset record |
| GET    | `/assets/` | Retrieve a list of assets |

Request/response schemas are defined in `app/schemas.py`.

## Project Structure

```
portfolio-tracker/
├── app/
│   ├── main.py            # FastAPI app & router setup
│   ├── database.py        # DB engine configuration
│   ├── models.py          # SQLModel ORM models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # Database interaction functions
│   └── routers/
│       └── portfolio.py   # Asset-related route handlers
├── .env.example           # Template for environment variables
├── .gitignore             # Ignored files and folders
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
└── README.md              # Project overview and instructions
```

## Roadmap & Future Enhancements

1. **Authentication:** Add JWT-based login and user management
2. **Portfolio Valuation:** Endpoints for current value, gains/losses
3. **Background Tasks:** Periodic fetching of asset prices
4. **Data Visualization:** Integrate a frontend dashboard
5. **Rust Integration:** Offload heavy calculations to a Rust microservice
6. **Testing:** Add unit tests with pytest and CI integration
7. **Deployment:** Containerize with Docker, deploy via Fly.io or Render

## Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
