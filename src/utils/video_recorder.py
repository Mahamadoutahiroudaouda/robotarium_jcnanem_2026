import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import time

class VideoRecorder:
    def __init__(self, output_dir="outputs/videos"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
    def save_animation(self, anim, filename=None, fps=30):
        if filename is None:
            filename = f"simulation_{int(time.time())}.mp4"
            
        path = os.path.join(self.output_dir, filename)
        print(f"Saving video to {path}... (This may take a while)")
        
        # Requires ffmpeg installed on system
        try:
            writer = animation.FFMpegWriter(fps=fps, metadata=dict(artist='Robotarium ANEM'), bitrate=1800)
            anim.save(path, writer=writer)
            print("Video saved successfully.")
        except Exception as e:
            print(f"Error saving video: {e}")
            print("Ensure FFMPEG is installed correctly.")
