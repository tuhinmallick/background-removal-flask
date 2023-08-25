from flask import Blueprint, request, jsonify, Response
import cv2
import numpy as np
from app.api.services.image_processing import processor

background_removal = Blueprint('background_removal', __name__)

@background_removal.route('/remove-background', methods=['POST'])
def remove_bg_endpoint():
    try:
        image_file = request.files.get('image')
        if not image_file:
            return jsonify({"error": "Image not provided"}), 400

        # Convert the uploaded image file to an OpenCV image
        input_img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        # Use the processor to get the processed image
        processed_image = processor.process_portrait_image(input_img)

        # Convert the processed image back to JPEG format for response
        _, img_encoded = cv2.imencode('.jpg', processed_image)
        response = Response(img_encoded.tobytes(), content_type='image/jpeg')

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
