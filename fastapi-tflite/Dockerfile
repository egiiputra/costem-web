FROM python:3.12-slim

WORKDIR /usr/src/app

COPY pyproject.toml ./
RUN pip install --no-cache-dir -r pyproject.toml

COPY . .

CMD [ "streamlit", "run", "main.py" ]

