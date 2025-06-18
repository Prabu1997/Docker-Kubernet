                                            🩺 Diagnose Log Uploader

This project provides a Python script (app.py) to upload a local file (such as a log file) to an AWS S3 bucket. It's containerized using Docker for easy and portable execution.

📜 What It Does
Prompts the user for:

    S3 bucket name

    Local file path

    Desired filename for the S3 object

    Uploads the file to the specified S3 bucket with a timestamp prefix

    Displays the current working directory

    Handles and logs errors gracefully

1. Build the Docker image

bash
Copy
Edit
docker build -t diagnose-uploader .

2. Run the Docker container

bash
Copy
Edit
docker run -i diagnose-uploader

You’ll be prompted for the bucket name, file path, and filename during execution.

