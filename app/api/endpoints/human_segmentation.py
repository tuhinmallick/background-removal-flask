from flask import Blueprint, request, jsonify, Response
import cv2
import numpy as np
from app.api.services.image_processing import processor

human_segment = Blueprint('human_segment', __name__)

@human_segment.route('/segment-human', methods=['POST'])
def segment_human_endpoint():
    try:
        image_file = request.files.get('image')
        if not image_file:
            return jsonify({"error": "Image not provided"}), 400

        # Convert the uploaded image file to an OpenCV image
        input_img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        # Use the processor to get the segmented image
        segmented_image = processor.process_human_segmentation(input_img)

        # Convert the segmented image back to JPEG format for response
        _, img_encoded = cv2.imencode('.jpg', segmented_image)
        response = Response(img_encoded.tobytes(), content_type='image/jpeg')

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
