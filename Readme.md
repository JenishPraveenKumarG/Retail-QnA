# AtliQ Tees: Talk to a Database with the power of LLM

## Overview
AtliQ Tees is an LLM-based application that connects to an SQL server, converts user queries into SQL queries, and retrieves information from the database. This project leverages LangChain and Streamlit to provide a seamless conversational interface for querying the database.

## How to Run This Project

### 1. Clone the Repository
```bash
  git clone https://github.com/codebasics/langchain.git
```

### 2. Install Dependencies
```bash
  pip install -r requirements.txt
```

### 3. Set Up API Key
Acquire an API key from [aistudio.google.com](https://aistudio.google.com/app/apikey) and add it to a `.env` file:
```bash
  GOOGLE_API_KEY="your_api_key_here"
```

### 4. Database Setup
Run the SQL script in MySQL Workbench to create the database:
```sql
  database/db_creation_atliq_t_shirts.sql
```

### 5. Run the Streamlit Application
```bash
  streamlit run app.py
```

### 6. Access the Web App
Once the app is running, a web page will open in your browser where you can input queries, and the application will generate and execute SQL queries to retrieve data.

## Project Structure

```
📂 AtliQ Tees
│── app.py              # Main Streamlit application script
│── llm_helper.py       # Contains LangChain logic to process queries
│── requirements.txt    # List of required Python packages
│── few_shots.py        # Contains few-shot prompts for LLM training
│── .env                # Configuration file for storing API key
│── database/
│   ├── db_creation_atliq_t_shirts.sql  # SQL script to set up the database
```

## Features
- Converts natural language queries into SQL queries.
- Retrieves and displays data from the SQL database.
- Uses LangChain for LLM-based text processing.
- Simple web interface using Streamlit.



