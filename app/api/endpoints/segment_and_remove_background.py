from flask import Blueprint, request, jsonify, Response
import cv2
import numpy as np
from app.api.services.image_processing import processor

segment_and_remove_background_bp = Blueprint('segment-and-remove-background', __name__)

@segment_and_remove_background_bp.route('/segment-and-remove-background', methods=['POST'])
def segment_and_remove_bg_endpoint():
    try:
        image_file = request.files.get('image')
        if not image_file:
            return jsonify({"error": "Image not provided"}), 400

        # Convert the uploaded image file to an OpenCV image
        input_img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        # Use the processor to get the segmented image
        segmented_image = processor.process_human_segmentation(input_img)

        # Now, use the segmented image to remove the background
        # Assuming the segmented image has the person in white and the background in black
        person_mask = (segmented_image < 127).astype(np.uint8)
        person_mask_resized = cv2.resize(person_mask, (input_img.shape[1], input_img.shape[0]))
        background_removed_img = np.where(person_mask_resized[:, :, np.newaxis].astype(bool), input_img, 255)
        
        # Convert the processed image back to JPEG format for response
        _, img_encoded = cv2.imencode('.jpg', background_removed_img)
        response = Response(img_encoded.tobytes(), content_type='image/jpeg')

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
