FROM python:3-alpine AS builder
WORKDIR /build
RUN apk add --no-cache gcc musl-dev
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
FROM python:3-alpine
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
