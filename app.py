from flask import Flask, render_template
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)  # Add this line
logger = logging.getLogger(__name__)     # Add this line

@app.route('/')
def home():
    logger.info("Home page accessed")    # Add this line
    return render_template('index.html')

if __name__ == '__main__':
    logger.info("Starting Flask app...")   # Add this line
    app.run(host='0.0.0.0', port=80)
