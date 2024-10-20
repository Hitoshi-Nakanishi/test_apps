#!/bin/bash

if [ "$1" == "train" ]; then
    echo "Starting training..."
    python train.py  # Adjust this command to your training script
else
    echo "Starting inference..."
    flask run --host=0.0.0.0
fi
