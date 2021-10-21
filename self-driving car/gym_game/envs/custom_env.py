import gym
from gym import spaces
import numpy as np
from gym_game.envs.pygame_2d import PyGame2D

class CustomEnv(gym.Env):
    #metadata = {'render.modes' : ['human']}
    def __init__(self):
        self.pygame = PyGame2D()
        self.action_space = spaces.Discrete(3) #3 inputs- right, left, accelerate
        self.observation_space = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([10, 10, 10, 10, 10]), dtype=np.int) #5 radar will be used to observe distance to walls in multiple directions - this is a simplified version of lidar

    def reset(self): #resets the game and returns the first observed data
        del self.pygame
        self.pygame = PyGame2D()
        obs = self.pygame.observe()
        return obs

    def step(self, action): #an action is performed, which is then observed and rewarded
        self.pygame.action(action)
        obs = self.pygame.observe()
        reward = self.pygame.evaluate()
        done = self.pygame.is_done()
        return obs, reward, done, {}

    def render(self, mode="human", close=False): #renders the game
        self.pygame.view()