FROM python:3.10

WORKDIR /app

COPY backend/ /app

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    pandas \
    scikit-learn \
    sqlalchemy \
    psycopg2-binary \
    python-jose \
    passlib \
    python-multipart

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]