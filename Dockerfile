# app/Dockerfile

# 如果有新增套件
# docker build --no-cache -t streamlit-fd:0.1 .

# 如果只是更新程式碼
# docker build -t streamlit-fd:0.5 .
# 
# docker run -p 9501:9501 --rm --name streamlit-FD -v .\:/app/workspace streamlit-fd:0.5 bash

FROM python:3.9-slim

WORKDIR /app

EXPOSE 9501

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install -r requirements.txt

# 將您的程式碼複製到容器內
COPY . .

HEALTHCHECK CMD curl --fail http://localhost:9501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Fraud-Detection.py", "--server.port=9501", "--server.address=0.0.0.0"]