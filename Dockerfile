FROM python:3.11-slim AS builder

WORKDIR /app

COPY src/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --target=/app -r /app/requirements.txt

COPY src/main /app

FROM gcr.io/distroless/python3-debian12:nonroot

COPY --from=builder /app /app

WORKDIR /app

ENV PYTHONPATH /app

CMD ["/app/app.py"]
