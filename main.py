import sys
import os

# Add src to python path relative to this file
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.main.demo_all_projects import SwarmSimulation

if __name__ == "__main__":
    print("Launching Robotarium Swarm Simulation...")
    sim = SwarmSimulation()
    sim.run()
