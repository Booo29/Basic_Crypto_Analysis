#Use image as base python
FROM python:3.7-slim

#Set working directory
WORKDIR /app

#Copy the current directory contents into the container at /app
COPY crypto_analysis.py /app/crypto_analysis.py

#Install any needed packages specified in requirements.txt
RUN pip install requests

# Install cron
RUN apt-get update && apt-get -y install cron

# Copy the cron file to the cron.d directory
COPY crontab /etc/cron.d/crypto-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crypto-cron

# Apply cron job
RUN crontab /etc/cron.d/crypto-cron

#Run the script
CMD ["cron", "-f"]