# Data Pipeline for Premier League Matches using Apache Airflow and Amazon Web Services (AWS)

## Overview
This Apache Airflow-based project automates the ETL process for Premier League scheduled matches. It's designed to run on an AWS EC2 instance and stores the processed data in an Amazon S3 bucket. This solution provides a scalable and efficient approach to handle sports data.

## Features
- **Automated Data Extraction**: Leverages a robust API to retrieve match details.
- **Efficient Data Transformation**: Utilizes Python and Pandas for data processing and transformation.
- **AWS EC2 Execution**: Runs the entire pipeline on an AWS EC2 instance for reliable and scalable processing.
- **S3 Data Storage**: Stores the processed data in an S3 bucket, ensuring durability and ease of access.

## Technologies Used
- Apache Airflow
- AWS EC2
- Amazon S3
- Python
- Pandas
- Requests

## Getting Started
To get this project up and running, you'll need to set up Apache Airflow on an AWS EC2 instance and configure an Amazon S3 bucket for data storage.

### Prerequisites
- AWS account with access to EC2 and S3
- Apache Airflow
- Python 3.x
- Pandas library

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

