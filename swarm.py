import numpy as np

class swarm:
    _SWARM_SIZE = 50

    def __init__(self, dimension: int):
        def normalize(x: np.ndarray):
            return x / np.sqrt(x.dot(x))

        self.particles = np.random.random(size=(self._SWARM_SIZE, dimension))
        self.directions = np.apply_along_axis(normalize, 1, np.random.random(size=(self._SWARM_SIZE, dimension))) # direction supposed to be normalized
        self.personal_bests = self.particles.copy()