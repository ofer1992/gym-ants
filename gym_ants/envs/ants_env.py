import gym
from gym import error, spaces, utils
from gym.utils import seeding

class AntsEnv(gym.Env):
    """The main OpenAI Gym class. It encapsulates an environment with
    arbitrary behind-the-scenes dynamics. An environment can be
    partially or fully observed.

    The main API methods that users of this class need to know are:

        step
        reset
        render
        close
        seed

    And set the following attributes:

        action_space: The Space object corresponding to valid actions
        observation_space: The Space object corresponding to valid observations
        reward_range: A tuple corresponding to the min and max possible rewards

    Note: a default reward range set to [-inf,+inf] already exists. Set it if you want a narrower range.

    The methods are accessed publicly as "step", "reset", etc.. The
    non-underscored versions are wrapper methods to which we may add
    functionality over time.
    """

    metadata = {'render.modes': ['human']}
    # reward_range

    action_space = ['n', 'e', 's', 'w']
    observation_space = None

    def __init__(self):
        pass

    def step(self, action):
        """Run one timestep of the environment's dynamics. When end of
               episode is reached, you are responsible for calling `reset()`
               to reset this environment's state.

               Accepts an action and returns a tuple (observation, reward, done, info).

               Args:
                   action (object): an action provided by the environment

               Returns:
                   observation (object): agent's observation of the current environment
                   reward (float) : amount of reward returned after previous action
                   done (boolean): whether the episode has ended, in which case further step() calls will return undefined results
                   info (dict): contains auxiliary diagnostic information (helpful for debugging, and sometimes learning)
               """
        pass

    def reset(self):
        """Resets the state of the environment and returns an initial observation.

        Returns: observation (object): the initial observation of the
            space.
        """
        pass

    def render(self, mode='human', close=False):
        """Renders the environment.

        The set of supported modes varies per environment. (And some
        environments do not support rendering at all.) By convention,
        if mode is:

        - human: render to the current display or terminal and
          return nothing. Usually for human consumption.
        - rgb_array: Return an numpy.ndarray with shape (x, y, 3),
          representing RGB values for an x-by-y pixel image, suitable
          for turning into a video.
        - ansi: Return a string (str) or StringIO.StringIO containing a
          terminal-style text representation. The text can include newlines
          and ANSI escape sequences (e.g. for colors).

        Note:
            Make sure that your class's metadata 'render.modes' key includes
              the list of supported modes. It's recommended to call super()
              in implementations to use the functionality of this method.

        Args:
            mode (str): the mode to render with
            close (bool): close all open renderings

        Example:

        class MyEnv(Env):
            metadata = {'render.modes': ['human', 'rgb_array']}

            def render(self, mode='human'):
                if mode == 'rgb_array':
                    return np.array(...) # return RGB frame suitable for video
                elif mode is 'human':
                    ... # pop up a window and render
                else:
                    super(MyEnv, self).render(mode=mode) # just raise an exception
        """
        pass

    def _set_observation_space(self):
        pass