# Data Pipeline for Premier League Matches using Apache Airflow

## Overview
This Apache Airflow-based project automates the ETL process for Premier League scheduled matches. It's designed to fetch, process, and store match data efficiently and reliably.

## Features
- **Automated Data Extraction**: Leverages a robust API to retrieve match details.
- **Efficient Data Transformation**: Utilizes Python and Pandas for data processing and transformation.
- **Seamless Data Loading**: Stores transformed data in a structured and accessible format.

## Technologies Used
- **Apache Airflow**: For orchestrating the workflow.
- **Python**: For scripting the ETL process.
- **Pandas**: Used in data transformation.
- **Requests**: For API interactions.

## Getting Started
To get this project up and running, you'll need to install Apache Airflow, set up your Python environment, and configure the necessary APIs.

### Prerequisites
- Apache Airflow
- Python 3.x
- Pandas library
- Access to football data API

### Installation
1. Clone the repository: `git clone https://github.com/your-repo.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Airflow: Follow [Airflow's installation guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html).

## Usage
1. Start the Airflow web server.
2. Navigate to the Airflow UI and trigger the DAG.
3. Monitor the pipeline's progress and results.

## Contributing
Interested in contributing? Great! Please read our [contribution guidelines](CONTRIBUTING.md) for details on how to get started.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

