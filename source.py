from PIL import ImageDraw, ImageFont
from tensorflow.keras.models import load_model
import numpy as np

MODEL_NAME= "ches-x-ray.h5"
IMG_SIZE = 100
LABELS = ["PNEUMONIA", "NORMAL"]


def predict_class(image):

    # gray image
    gray_image = image.convert("L")

    # loading image data and resizing
    target_size = (IMG_SIZE, IMG_SIZE)
    resized_image = gray_image.resize(target_size)

    # unsqueezing data
    data = np.expand_dims(resized_image, axis = 0)

    # loading model
    model = load_model(MODEL_NAME)

    # predicted class
    prediction = model.predict(data)

    # normalizing
    prediction = prediction.argmax(axis = -1)

    return prediction

def write_class(image, prediction):

    # Converting to RGB
    if image.mode != 'RGB':
        image = image.convert('RGB')

    draw = ImageDraw.Draw(image)

    # some parameters
    position = (10, 10)
    text = LABELS[prediction[0]]
    color = "#3498DB"
    font_size = 30
    font = ImageFont.load_default().font_variant(size = font_size)

    # drawing
    draw.text(position, text, fill = color, font = font, width = 2, outline = "black")

    return image
