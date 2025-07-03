FROM python:3.12-alpine

# Set timezone to Asia/Kuala_Lumpur
RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/Asia/Kuala_Lumpur /etc/localtime && \
    echo "Asia/Kuala_Lumpur" > /etc/timezone

# Install required Python packages
RUN pip install --no-cache-dir schedule pytz aprslib

# Copy the bot script
WORKDIR /app
COPY aprs_bot.py /app/aprs_bot.py

# Run the script
CMD ["python", "/app/aprs_bot.py"]
