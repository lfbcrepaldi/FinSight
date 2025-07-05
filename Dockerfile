FROM python:3.13-slim

# install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# define working directory
WORKDIR /app

# copy requirements file
COPY requirements.txt .

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application
COPY . .

# Expose the default Streamlit port
EXPOSE 8501

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# define entrypoint
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501"]
