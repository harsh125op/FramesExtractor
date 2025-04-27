# Video Frame Extractor

A web application that allows users to upload video files, extract individual frames, and download them as a ZIP file.

![Video Frame Extractor Screenshot](https://via.placeholder.com/800x450)

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User-friendly Interface**: Simple drag-and-drop upload for video files
- **Format Support**: Compatible with MP4, AVI, MOV, and MKV video formats
- **Customizable Extraction**: Control frame extraction density with sampling rate options
- **Live Preview**: See sample frames before downloading
- **Efficient Download**: All frames packaged in a single ZIP file
- **Progress Tracking**: Real-time progress bar during extraction
- **Video Information**: Displays FPS, duration, and frame statistics

## Demo

[View Live Demo](#) *(Add your deployment link when available)*

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/harsh125op/FramesExtractor.git
   cd FramesExtractor
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Upload a video file using the file uploader

4. Adjust the sampling rate slider if needed

5. Click "Extract Frames" and wait for the process to complete

6. Download the ZIP file containing all extracted frames

## How It Works

The application follows these steps to extract frames:

1. **Video Upload**: The user uploads a video file through the Streamlit interface
2. **Frame Extraction**: OpenCV processes the video to extract frames based on the selected sampling rate
3. **Image Processing**: Frames are converted from BGR to RGB format
4. **ZIP Creation**: All frames are compiled into a single ZIP file
5. **Download**: The user can download the ZIP file containing all extracted frames

## Technologies

- **Streamlit**: Web application framework
- **OpenCV**: Computer vision and video processing
- **Pillow**: Image processing
- **Python**: Core programming language
- **BytesIO & Base64**: For handling file operations in memory

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Created by [Your Name](https://github.com/harsh125op) - feel free to connect on [LinkedIn](https://linkedin.com/in/yourprofile)!
