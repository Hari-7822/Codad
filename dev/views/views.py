from django.shortcuts import render

def co(request):
    return render(request, "co.j2")

from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles import finders
import os

@csrf_exempt
@require_GET
def serve_image_with_cors(request):
    image_name = 'head_img.jpg'
    # Assuming the 'static' folder is in the same directory as the script
    image_path = os.path.join(os.path.dirname(__file__), 'static', 'images', image_name)

    # Open the image file
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Create an HttpResponse with the image data
    response = HttpResponse(image_data, content_type='image/jpeg')

    # Add CORS headers to allow cross-origin requests from all origins
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'

    return response

