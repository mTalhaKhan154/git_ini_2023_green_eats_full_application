from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from MyApi.serializers import ImageRequestSerializer
from MyApi.models import getData
from PIL import Image
from django.conf import settings
import os
from tensorflow.keras.models import load_model
import numpy as np
import numpy as np

#removing the tensor flows suggestion to rebuild tensorflow.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Function to process the image
def load_image(image_path):
    image = Image.open(image_path)
    return image
def preprocess_image(image):
    # Resize the image
    image = image.resize((224, 224))

    # Convert the image to a NumPy array
    image = np.array(image)

    # Normalize the pixel values
    image = image / 255

    return image


#Related to API
class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = getData.objects.all().order_by('date_created')
    serializer_class = ImageRequestSerializer




# Create your views here.


# Api view to handle api and prediction
#loading the modal and labels.txt
# Loding the model using tensorflow
model = load_model(settings.MODEL_FILE_PATH)
# Compiling the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# loadign the labels
labels = []
# Open the labels file
with open(settings.LABELS_TXT, 'r') as f:
    # Iterate over each line in the file
    for line in f:
        # Strip the newline character and append the label to the list
        labels.append(line.strip())
def modelPredict():
    # Load the image
    image = load_image(settings.TEST_IMAGE)
    # Preprocess the image
    image = preprocess_image(image)
    # Reshape the image
    image = image.reshape(1,*image.shape)
    # Make a prediction
    prediction = model.predict(image)
    # Getting the max index
    food_index = prediction.argmax()
    print(food_index)
    food_name = labels[food_index]
    return food_name,food_index
def api(request):
  return HttpResponse(modelPredict())