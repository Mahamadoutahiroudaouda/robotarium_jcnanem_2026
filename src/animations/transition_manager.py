import numpy as np

class TransitionManager:
    def __init__(self, drones):
        self.drones = drones
        self.frames_total = 0
        self.current_frame = 0
        self.start_positions = []
        self.end_positions = []
        self.is_transitioning = False

    def set_formation(self, target_coords, duration_seconds=5, fps=30):
        """
        Sets a new target formation and prepares the interpolation.
        target_coords: list or array of (x,y,z) coordinates.
        """
        self.is_transitioning = True
        self.frames_total = int(duration_seconds * fps)
        self.current_frame = 0
        
        # Capture current positions
        self.start_positions = [np.copy(d.position) for d in self.drones]
        
        # Ensure we have enough target coords, or handle mismatch
        # For simplicity, assume len(target_coords) == len(drones) or we loop/truncate
        self.end_positions = []
        for i, d in enumerate(self.drones):
            if i < len(target_coords):
                self.end_positions.append(np.array(target_coords[i]))
            else:
                # If extra drones, they can go to a holding area or stay put
                self.end_positions.append(np.copy(d.position)) # Stay put

    def update(self):
        """
        Updates drone positions for the current frame of transition.
        Returns True if transition is active, False if finished.
        """
        if not self.is_transitioning:
            return False

        if self.current_frame >= self.frames_total:
            self.is_transitioning = False
            # Snap to final
            for i, d in enumerate(self.drones):
                 d.position = self.end_positions[i]
            return False

        # Ease-in-out interpolation (cosine)
        progress = self.current_frame / self.frames_total
        # Cosine interpolation formula: y = (1 - cos(pi * x)) / 2
        alpha = (1 - np.cos(progress * np.pi)) / 2

        for i, d in enumerate(self.drones):
            new_pos = self.start_positions[i] + (self.end_positions[i] - self.start_positions[i]) * alpha
            d.position = new_pos

        self.current_frame += 1
        return True
