FROM python:3-alpine
WORKDIR /app
COPY app.py .
RUN pip install flask redis
ENV REDIS_HOST=redis
EXPOSE 8080
CMD ["python","app.py"]

