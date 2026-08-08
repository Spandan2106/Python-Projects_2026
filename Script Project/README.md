# System Resource Monitor

A Python script that monitors CPU and memory usage and sends an email alert if they exceed configurable thresholds.

## Features

- Monitors CPU and Memory usage.
- Sends email alerts when usage exceeds defined thresholds.
- Configurable thresholds and check intervals.
- Logs monitoring activity to a file (`server_monitor.log`).

## Prerequisites

- Python 3.6+
- Git

## Setup and Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd Script Project
    ```

2.  **Create a virtual environment:**
    It's recommended to use a virtual environment to manage project dependencies.
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    Create a `.env` file in the project root by copying the example file:
    ```sh
    # For Windows
    copy .env.example .env

    # For macOS/Linux
    cp .env.example .env
    ```
    Now, open the `.env` file and update it with your specific configuration (email credentials, etc.).

    **Note on `EMAIL_PASSWORD`**: If you are using Gmail, you will need to generate an "App Password" for this script to be able to send emails on your behalf. You can find instructions on how to do this in Google's support documentation.

## Usage

Run the monitoring script from your terminal:
```sh
python resource_monitor.py
```

The script will now run in the background, checking your system resources every 5 minutes (or at the `CHECK_INTERVAL` you define) and logging its activity to `server_monitor.log`.