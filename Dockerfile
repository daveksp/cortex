FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir "poetry==2.1.4"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./

RUN poetry install \
    --no-interaction \
    --no-root

COPY . .

RUN poetry install \
    --no-interaction

EXPOSE 8000

CMD ["uvicorn", "cortex.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]