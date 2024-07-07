import cv2
import os

def extract_frames(video_path):
    # Get the video title (filename without extension)
    video_title = os.path.splitext(os.path.basename(video_path))[0]
    
    # Define the output folder on the desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'))
    output_folder = os.path.join(desktop_path, video_title)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames in video: {total_frames}")

    frame_index = 0
    while cap.isOpened():
        # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame as an image file
        frame_filename = os.path.join(output_folder, f"frame_{frame_index:04d}.png")
        cv2.imwrite(frame_filename, frame)
        
        frame_index += 1
        print(f"Extracted frame {frame_index}/{total_frames}")

    # Release the video capture object
    cap.release()
    print(f"Finished extracting frames to {output_folder}")

# Example usage
video_path = 'path_to_your_video_file.mp4'
extract_frames(video_path)
