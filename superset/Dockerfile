# Use the official Apache Superset image
FROM apache/superset:latest

# Install Redis, PostgreSQL client, and Python (if not already included) and other dependencies
USER root
RUN apt-get update && \
    apt-get install -y python3 postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Copy the Superset configuration
COPY ./superset_config.py /app/pythonpath/superset_config.py

# Generate a SECRET_KEY and append it to the configuration file before running upgrade
RUN echo "SECRET_KEY = '$(python3 -c "import os; print(os.urandom(24).hex())")'" >> /app/pythonpath/superset_config.py

# Install Python packages for Google Sheets integration
RUN pip install gspread oauth2client


# Copy the entrypoint script and make it executable
COPY entrypoint.sh /entrypoint.sh
COPY start.sh /start.sh
RUN chmod +x /entrypoint.sh
RUN chmod +x /start.sh

# Install headless Chrome browser
RUN apt-get update && apt-get install -y wget gnupg && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Set the web driver type to Chrome
ENV WEBDRIVER_TYPE=chrome

# Switch back to superset user and initialize Superset
USER superset

# Expose the port Superset is running on
EXPOSE 8088

# Start Superset using the custom start script
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start.sh"]

