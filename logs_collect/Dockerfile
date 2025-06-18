FROM python-baseline

RUN apt get install python && pip install boto3

# Set working directory
WORKDIR /app

# Copy your script into the container
COPY app.py .

CMD [ "python3" ,  "app.py" ]