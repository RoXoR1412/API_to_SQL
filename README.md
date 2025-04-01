# API_to_SQL

## Project Overview
`API_to_SQL` is a FastAPI-based project that fetches data from an API or CSV files, performs calculations or transformations, and stores the processed data into a SQL database. The project demonstrates how to integrate APIs, handle CSV files, and interact with a database using SQLModel and SQLAlchemy.

## Features
- Fetch data from external APIs.
- Load data from CSV files into a database.
- Perform calculations or transformations on the data.
- Query and display data from the database in tabular format.
- RESTful API endpoints for data operations.

## Technologies Used
- **FastAPI**: For building the RESTful API.
- **SQLModel**: For database modeling and interaction.
- **SQLite/MySQL**: As the database backend.
- **Pandas**: For reading and processing CSV files.
- **Python-dotenv**: For managing environment variables.

## Installation

### Prerequisites
- Python 3.9 or higher
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/RoXoR1412/API_to_SQL.git
   cd API_to_SQL
   ```

2. Create and activate a virtual environment:
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root directory.
   - Add the necessary environment variables, such as database connection strings.

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## Usage
- Access the API documentation at `http://127.0.0.1:8000/docs` after running the application.
- Use the provided endpoints to interact with the API for data operations.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.