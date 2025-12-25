import time
import psutil

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()
        self.frame_times = []
        
    def start_frame(self):
        self.frame_start = time.time()
        
    def end_frame(self):
        dt = time.time() - self.frame_start
        self.frame_times.append(dt)
        if len(self.frame_times) > 100:
            self.frame_times.pop(0)
            
    def get_fps(self):
        if not self.frame_times:
            return 0
        avg_dt = sum(self.frame_times) / len(self.frame_times)
        return 1.0 / avg_dt if avg_dt > 0 else 0
        
    def get_system_usage(self):
        return {
            'cpu': psutil.cpu_percent(),
            'memory': psutil.virtual_memory().percent
        }
    
    def report(self):
        print(f"FPS: {self.get_fps():.2f} | CPU: {self.get_system_usage()['cpu']}%")
