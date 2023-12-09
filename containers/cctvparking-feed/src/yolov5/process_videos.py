import subprocess
import os

# Folder with MP4 videos
videos_folder = '/home/luigipizzolito/Documents/GitHub/CommunityManagementSystem/containers/webserver/public/videos-original'

# Output folder
output_folder = '/home/luigipizzolito/Documents/GitHub/CommunityManagementSystem/containers/webserver/public/videos-original/output'
os.makedirs(output_folder, exist_ok=True)

# List all MP4 files in the folder
all_files = [file for file in os.listdir(videos_folder) if file.endswith('.mp4')]
print(all_files)

# Run YOLOv5 detection for each video
for index, video_file in enumerate(all_files, start=1):
    video_file_path = os.path.join(videos_folder, video_file)
    print(video_file_path)
    
    # Run the YOLOv5 detection script for the video
    command = f"/home/luigipizzolito/Desktop/smart-car-parking-yolov5-main/yolov5/bin/python /home/luigipizzolito/Desktop/smart-car-parking-yolov5-main/yolov5/detect_customize.py --weights yolov5s.pt --img 640 --conf 0.60 --source {video_file_path} --class 2 --project {output_folder} --name {index}"

    # Execute the command
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Detection successful for video {index}: {video_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during detection for video {index}: {video_file}")
        print(f"Error Message: {e}")

print(f"All detections saved in the folder: {output_folder}")
