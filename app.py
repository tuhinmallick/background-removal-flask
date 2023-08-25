from flask import Flask, request, send_file, jsonify, Response
from portrait_utils import process_portrait_image
import cv2
import numpy as np
from io import BytesIO
import logging

app = Flask(__name__)

# 1. Configuration Management
class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

app.config.from_object(DevelopmentConfig())  # Use ProductionConfig in production

# 2. Logging Setup
logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)

@app.route('/remove-background', methods=['POST'])
def remove_bg_endpoint():
    try:
        image_file = request.files.get('image')
        if not image_file:
            return jsonify({"error": "Image not provided"}), 400

        input_img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        processed_image = process_portrait_image(input_img)
        _, img_encoded = cv2.imencode('.jpg', processed_image)
        response = Response(BytesIO(img_encoded.tobytes()), content_type='image/jpeg')
        response.headers['Content-Disposition'] = 'attachment; filename=processed_image.jpg'
        return response

    
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred while processing the image"}), 500

# 3. Exception Handling
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed"}), 405

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# 4. Restructuring
def create_app():
    return app

if __name__ == '__main__':
    app.run(port=5002)

