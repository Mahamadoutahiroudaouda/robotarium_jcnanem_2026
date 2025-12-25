import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.main.demo_all_projects import SwarmSimulation

# Placeholder for keyboard/gamepad control
class RealTimeController(SwarmSimulation):
    def run(self):
        print("Real-time control mode enabled.")
        print("Press '1'-'9' to trigger formations (Not implemented in this demo).")
        super().run()

if __name__ == "__main__":
    sim = RealTimeController()
    sim.run()
