import json
import numpy as np

# Create a random 28x28 image array with values between 0 and 1
image = np.random.rand(28, 28).tolist()

# Convert the image array to JSON format
data = {
    "image": image
}

# Save the image data as a JSON file
with open('test_image.json', 'w') as f:
    json.dump(data, f)

print("Test image saved as test_image.json")