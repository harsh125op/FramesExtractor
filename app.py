import streamlit as st
import cv2
import os
import tempfile
import zipfile
import io
import base64
import time
from PIL import Image

def extract_frames(video_path, sampling_rate=1):
    """
    Extract frames from a video file
    
    Parameters:
    video_path (str): Path to the video file
    sampling_rate (int): Extract every nth frame
    
    Returns:
    list: List of extracted frames as numpy arrays
    """
    frames = []
    frame_count = 0
    
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Get video properties
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    
    # Create a progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Read frames
    while True:
        ret, frame = video.read()
        
        if not ret:
            break
        
        # Extract frame if it meets the sampling rate
        if frame_count % sampling_rate == 0:
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame_rgb)
            
            # Update progress
            progress = int((frame_count / total_frames) * 100)
            progress_bar.progress(progress)
            status_text.text(f"Extracting frames: {progress}%")
        
        frame_count += 1
    
    # Release video
    video.release()
    
    # Clear progress bar and status text
    progress_bar.empty()
    status_text.empty()
    
    return frames, fps

def create_zip_file(frames):
    """
    Create a zip file containing all frames
    
    Parameters:
    frames (list): List of frames as numpy arrays
    
    Returns:
    bytes: Zip file as bytes
    
    """
    # Create a BytesIO object to store the zip file
    zip_buffer = io.BytesIO()
    
    # Create a ZipFile object
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add each frame to the zip file
        for i, frame in enumerate(frames):
            img = Image.fromarray(frame)
            img_buffer = io.BytesIO()
            img.save(img_buffer, format='JPEG')
            zipf.writestr(f"frame_{i:04d}.jpg", img_buffer.getvalue())
    
    # Reset buffer position
    zip_buffer.seek(0)
    
    return zip_buffer.getvalue()

def get_download_link(zip_data, filename="frames.zip"):
    """
    Generate a download link for the zip file
    
    Parameters:
    zip_data (bytes): Zip file as bytes
    filename (str): Name of the file to download
    
    Returns:
    str: HTML link for downloading the zip file
    """
    b64 = base64.b64encode(zip_data).decode()
    href = f'<a href="data:application/zip;base64,{b64}" download="{filename}">Download ZIP file</a>'
    return href

def main():
    st.title("Video Frame Extractor")
    
    st.write("""
    Upload a video file to extract individual frames and download them as a ZIP file.
    """)
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mkv"])
    
    if uploaded_file is not None:
        # Display video info
        st.video(uploaded_file)
        
        # Options
        col1, col2 = st.columns(2)
        with col1:
            sampling_rate = st.slider("Extract every Nth frame", 1, 30, 1)
        
        # Extract frames button
        if st.button("Extract Frames"):
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
                # Write the uploaded file to the temporary file
                tmp_file.write(uploaded_file.getvalue())
                tmp_filepath = tmp_file.name
            
            try:
                # Extract frames
                with st.spinner("Extracting frames..."):
                    frames, fps = extract_frames(tmp_filepath, sampling_rate)
                
                # Show info
                st.success(f"Extracted {len(frames)} frames from the video.")
                
                # Display a sample of frames
                if len(frames) > 0:
                    st.subheader("Sample Frames")
                    cols = st.columns(3)
                    for i, col in enumerate(cols):
                        if i < len(frames):
                            # Skip to show frames from different parts of the video
                            index = min(i * (len(frames) // 3), len(frames) - 1)
                            col.image(frames[index], caption=f"Frame {index}")
                
                # Create zip file
                with st.spinner("Creating ZIP file..."):
                    zip_data = create_zip_file(frames)
                
                # Display download link
                st.markdown(get_download_link(zip_data), unsafe_allow_html=True)
                
                # Show estimated video information
                st.subheader("Video Information")
                st.write(f"FPS: {fps:.2f}")
                st.write(f"Duration: {len(frames) * sampling_rate / fps:.2f} seconds")
                st.write(f"Total original frames: {len(frames) * sampling_rate}")
                st.write(f"Extracted frames: {len(frames)}")
            
            finally:
                # Clean up the temporary file
                os.unlink(tmp_filepath)

if __name__ == "__main__":
    main()
