FROM python:3-alpine
WORKDIR /app
COPY app.py .
RUN pip install flask redis
RUN apk add --no-cache curl
ENV REDIS_HOST=redis
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8080/ || exit 1
CMD ["python", "app.py"]
