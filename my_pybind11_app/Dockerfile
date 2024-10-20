FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install Flask pybind11
COPY --from=builder /app/example.cpython-*-x86_64-linux-gnu.so ./
EXPOSE 5000
CMD ["python", "app.py"]
