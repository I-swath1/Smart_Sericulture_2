
from pathlib import Path
import tensorflow as tf

# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Trained model location
MODEL_PATH = BASE_DIR / "models" / "mobilenetv2_best.keras"


def load_silkworm_model():
    """
    Load the trained MobileNetV2 model.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Trained model not found: {MODEL_PATH}"
        )

    model = tf.keras.models.load_model(
        MODEL_PATH,
        compile=False
    )

    print("Silkworm AI model loaded successfully!")

    return model
