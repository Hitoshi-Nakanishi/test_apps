# My Pybind11 App

This project demonstrates how to use `pybind11` to create Python bindings for a simple C++ library. The project is containerized using Docker for easy deployment.

## Project Structure

my_pybind11_app/
│
├── CMakeLists.txt      # CMake configuration for building the C++ extension
├── example.cpp         # C++ source file with functions to bind
├── Dockerfile           # Dockerfile for building the C++ extension
├── app.py              # Flask app
├── templates/          # HTML templates folder
│   └── index.html      # HTML template for the front end
└── docker-compose.yml   # Docker Compose configuration



## Requirements

- Docker installed on your machine.

## Build and Run Instructions

### Step 1: Build the Docker Image

To build the Docker image, navigate to the project directory and run the following command:

```bash
docker build -t my_pybind11_app .
```

### Step 2: Run the Docker Container
Once the build completes successfully, you can run the Docker container with:

```bash
docker run my_pybind11_app
```

Expected Output
You should see output similar to:

```python
The sum of 5.0 and 3.0 is: 8.0
The product of 5.0 and 3.0 is: 15.0
```
