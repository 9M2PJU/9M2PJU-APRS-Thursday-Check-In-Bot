FROM python:3.12-alpine

# Set timezone to Asia/Kuala_Lumpur
RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/Asia/Kuala_Lumpur /etc/localtime && \
    echo "Asia/Kuala_Lumpur" > /etc/timezone

# Install cron and Python dependencies
RUN apk add --no-cache curl bash busybox-suid && \
    pip install --no-cache-dir pytz aprslib

# Create app directory
WORKDIR /app
COPY aprs_bot.py /app/aprs_bot.py

# Create cron job for Thursday 9PM MYT (13:00 UTC)
RUN echo "0 13 * * 4 python /app/aprs_bot.py >> /var/log/cron.log 2>&1" > /etc/crontabs/root

# Touch log file
RUN touch /var/log/cron.log

# Start cron in foreground
CMD ["/usr/sbin/crond", "-f", "-L", "/var/log/cron.log"]
