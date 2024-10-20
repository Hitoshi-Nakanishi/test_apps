Build and Run Training Container

Build the training image:
```bash
docker build -t mnist-training -f Dockerfile.training .
```

Run the container to train the model: You can persist the trained model using Docker volumes or by copying it to a specific directory:
```bash
docker run --rm -v $(pwd)/model:/app/model mnist-training
```


Build the inference image:
```bash
docker build -t mnist-inference -f Dockerfile.inference .
```

Run the inference container: You can run the web app, mounting the trained model into the container:
```bash
docker run -p 5000:5000 mnist-inference
```