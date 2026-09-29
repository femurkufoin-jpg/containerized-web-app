FROM python:3.13-slim

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/health')"

CMD ["python", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000"]