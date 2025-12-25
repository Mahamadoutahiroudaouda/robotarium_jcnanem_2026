import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.utils.config import GLOBAL_CONFIG
from src.utils.drone import Drone
from src.animations.transition_manager import TransitionManager
from src.formations.base_formations import place_drones_on_ground, sphere, cube
from src.formations.letter_formations import get_text_coords
from src.formations.cultural_formations import niger_map, agadez_cross
from src.projects.project_03_vagues import ocean_waves
from src.projects.project_04_feux_artifice import fireworks_explosion
from src.projects.project_06_faune import giraffe_shape
from src.projects.project_07_calligraphy import arabic_salaam
from src.projects.project_09_architecture import hausa_architecture
from src.projects.project_10_scientific import scientific_atom
from src.projects.project_01_anem_lumiere import anem_lumiere_sequence
from src.projects.project_02_monuments import monuments_sequence
from src.projects.project_08_parade import grande_parade_sequence

class SwarmSimulation:
    def __init__(self):
        self.drone_count = GLOBAL_CONFIG.drone_count
        self.drones = [Drone(i) for i in range(self.drone_count)]
        
        # Initialize with ground formation
        initial_coords = place_drones_on_ground(self.drone_count)
        for i, d in enumerate(self.drones):
            if i < len(initial_coords):
                d.position = initial_coords[i]
                d.target_position = initial_coords[i]
        
        self.tm = TransitionManager(self.drones)
        
        # Setup Figure
        self.fig = plt.figure(figsize=(12, 10))
        self.fig.patch.set_facecolor('black')
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_facecolor('black')
        
        # Grid settings
        self.ax.grid(False)
        self.ax.set_axis_off()
        
        # Initial scatter plot
        self.scatters = None
        
        # Scenario / Timeline
        self.scenario_step = 0
        self.wait_frames = 0
        
    def init_plot(self):
        # We need to return an iterable of artists
        xs = [d.position[0] for d in self.drones]
        ys = [d.position[1] for d in self.drones]
        zs = [d.position[2] for d in self.drones]
        
        # Using a single scatter collection is faster
        self.scatters = self.ax.scatter(xs, ys, zs, c='white', s=10)
        
        # Set limits
        limit = 50
        self.ax.set_xlim(-limit, limit)
        self.ax.set_ylim(-limit, limit)
        self.ax.set_zlim(0, 80)
        return self.scatters,

    def update(self, frame):
        # Update logic (Simulation physics/transition)
        is_moving = self.tm.update()
        
        # Scenario Logic
        if not is_moving:
            if self.wait_frames > 0:
                self.wait_frames -= 1
            else:
                self.next_scenario_step()
        
        # Update Plot
        xs = [d.position[0] for d in self.drones]
        ys = [d.position[1] for d in self.drones]
        zs = [d.position[2] for d in self.drones]
        
        self.scatters._offsets3d = (xs, ys, zs)
        return self.scatters,

    def next_scenario_step(self):
        # Define the sequence of formations here for the demo
        steps = [
            ("P1_FLAG_RAIN", lambda: anem_lumiere_sequence(self.drone_count, step=0)),
            ("P1_ANEM", lambda: anem_lumiere_sequence(self.drone_count, step=1)),
            ("P1_JCN2026", lambda: anem_lumiere_sequence(self.drone_count, step=2)),
            ("P1_FES", lambda: anem_lumiere_sequence(self.drone_count, step=3)),
            ("P1_NIGER_TEXT", lambda: anem_lumiere_sequence(self.drone_count, step=4)),
            ("P1_FLAG_WAVE", lambda: anem_lumiere_sequence(self.drone_count, step=5)),
            ("P1_MAP", lambda: anem_lumiere_sequence(self.drone_count, step=6)),
            ("P1_FINALE", lambda: anem_lumiere_sequence(self.drone_count, step=7)),
            
            ("P2_MOSQUE", lambda: monuments_sequence(self.drone_count, step=0)),
            ("P2_CROSS", lambda: monuments_sequence(self.drone_count, step=1)),
            
            ("WAVES", lambda: ocean_waves(self.drone_count, t=0)),
            ("FIBONACCI", lambda: fibonacci_spiral(self.drone_count)),
            ("FIREWORKS", lambda: fireworks_explosion(self.drone_count)),
            ("FAUNA", lambda: giraffe_shape(self.drone_count, scale=2)),
            ("CALLIGRAPHY", lambda: arabic_salaam(self.drone_count, scale=3)),
            ("ARCHITECTURE", lambda: hausa_architecture(self.drone_count, scale=2)),
            ("SCIENCE", lambda: scientific_atom(self.drone_count, scale=8)),
            
            ("P8_STORM", lambda: grande_parade_sequence(self.drone_count, step=0)),
            ("P8_MAP", lambda: grande_parade_sequence(self.drone_count, step=1)),
            ("P8_HEART", lambda: grande_parade_sequence(self.drone_count, step=2)),
            
            ("TEXT_MERCI", lambda: get_text_coords("MERCI")),
            ("LAND", lambda: place_drones_on_ground(self.drone_count))
        ]
        
        if self.scenario_step < len(steps):
            name, func = steps[self.scenario_step]
            print(f"Starting formation: {name}")
            
            result = func()
            target_colors = None
            
            if isinstance(result, tuple):
                target = result[0]
                target_colors = result[1]
            else:
                target = result
                
            # Update colors if provided
            if target_colors is not None:
                # Matplotlib scatter set_color expects simple list or array
                # We need to ensure it matches drone count
                if len(target_colors) == self.drone_count:
                    self.scatters.set_color(target_colors)
                elif len(target_colors) < self.drone_count:
                    # Fill rest with white or hidden
                    full_colors = list(target_colors)
                    full_colors.extend(['white'] * (self.drone_count - len(target_colors)))
                    self.scatters.set_color(full_colors)
            
            self.tm.set_formation(target, duration_seconds=3)
            
            # Specific pause times per spec
            wait = 60 # Default 2s
            if "TEXT" in name or "P1_" in name:
                wait = 120 # 4s pause for text reading
            
            self.wait_frames = wait 
            self.scenario_step += 1
        else:
            # Loop or stop
            print("Simulation sequence finished.")
            self.wait_frames = 100

    def run(self):
        ani = animation.FuncAnimation(self.fig, self.update, init_func=self.init_plot, 
                                      frames=2000, interval=1000/30, blit=False)
        plt.show()

if __name__ == "__main__":
    sim = SwarmSimulation()
    sim.run()
