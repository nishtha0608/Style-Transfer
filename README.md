# Style-Transfer
# Neural Style Transfer

## Project Overview
This project implements **Neural Style Transfer (NST)** using a **Flask web application**. NST is a deep learning technique that applies the artistic style of one image to another while preserving the content of the original image. The application allows users to upload a content image and a style image, process them using a **pre-trained TensorFlow Hub model**, and generate a stylized image.

## Features
- Upload a content image and a style image
- Apply neural style transfer using Google's **Magenta Arbitrary Image Stylization model**
- View and download the stylized output image
- Simple and interactive web interface

## Technologies Used
- **Flask**: Backend web framework for handling requests and responses
- **TensorFlow & TensorFlow Hub**: For loading the pre-trained NST model
- **Matplotlib & NumPy**: Image processing and visualization
- **HTML, CSS & JavaScript**: Frontend for user interaction
- **Docker**: Containerization for deployment

## Prerequisites
Ensure you have the following installed before running the project:
- Python 3.9+
- pip (Python package manager)
- Docker (optional for containerized execution)

## Installation & Setup
### Running Without Docker
1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/neural-style-transfer.git
   cd neural-style-transfer
   ```
2. **Create a virtual environment (Optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask application**
   ```sh
   python app.py
   ```
5. **Access the application**
   Open a browser and visit:
   ```sh
   http://localhost:5000
   ```

### Running with Docker
1. **Build the Docker image**
   ```sh
   docker build -t neural-style-transfer .
   ```
2. **Run the container**
   ```sh
   docker run --rm -it -p 5001:5000 -e FLASK_DEBUG=1 -v "$(pwd)":/app neural-style-transfer
   ```
3. **Access the application**
   Open a browser and visit:
   ```sh
   http://localhost:5001
   ```

## Project Structure
```
├── app.py                 # Flask backend application
├── templates/
│   ├── index.html         # Frontend UI
├── uploads/               # Stores uploaded & processed images
├── Dockerfile             # Docker container configuration
├── requirements.txt       # Required Python dependencies
├── README.md              # Project documentation
```

## API Endpoints
- `GET /` - Serves the main webpage
- `POST /upload` - Handles content and style image uploads, performs NST, and returns image URLs
- `GET /uploads/<filename>` - Serves uploaded and generated images

## Troubleshooting
- If TensorFlow-related errors occur, ensure your system supports **TensorFlow 2.x**
- If using Docker, ensure that you have correctly mapped port **5001 to 5000**

## License
This project is open-source and available under the **MIT License**.

## Author
Developed by **[Your Name]**

