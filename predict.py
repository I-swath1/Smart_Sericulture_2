import numpy as np
from PIL import Image
from pathlib import Path

CLASS_NAMES = [
    "Healthy",
    "grasserie",
    "Flacherie",
    "Pebrine"
]

def predict_silkworm(image_path, model):
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))

    image_array = np.array(image).astype("float32")
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array, verbose=0)

    predicted_index = int(np.argmax(predictions[0]))
    predicted_condition = CLASS_NAMES[predicted_index]

    confidence = float(predictions[0][predicted_index]) * 100

    return {
        "condition": predicted_condition,
        "confidence": round(confidence, 2)
    }