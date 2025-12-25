import sys
import os
import argparse
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.main.demo_all_projects import SwarmSimulation
# We can subclass or parameterize SwarmSimulation to run only specific steps

def run_project(project_id):
    print(f"Launching Project #{project_id}")
    # Logic to filter the steps list in SwarmSimulation would go here
    # For now, just run full demo
    sim = SwarmSimulation()
    sim.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run specific Robotarium project')
    parser.add_argument('id', type=int, help='Project ID (1-10)')
    args = parser.parse_args()
    
    run_project(args.id)
