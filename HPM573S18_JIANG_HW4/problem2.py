import numpy as np
from enum import Enum

class Coin(Enum):
    """ the result of flip a coin  """
    HEAD = 1
    TAIL = 0

class Game(object):
    def __init__(self, name, head_prob, time_steps):
        """
        :param name: name of the player
        :param head_prob: probability that the coin is head
        :param time_steps: times of the game
        """
        self._id = name
        self._reward = -250  # assuming reward at the beginning
        self._time_steps = time_steps
        self._coins = []  # list of coins
        self._headProb=head_prob
    def simulate(self):
        """ simulate the game over the specified trial times """
        t = 0  # simulation current time
        # while the patient is alive and simulation length is not yet reached
        while t < self._time_steps:
            coinside = Coin.TAIL
            if np.random.sample() < self._headProb:
                # if the sampler less than the probability of head,
                coinside = Coin.HEAD
                # add the patient to the cohort
            self._coins.append(coinside)
            # increment time
            t += 1
        return (self._coins)

    def countwin(self):
        i = 0  # the ith element in the vector
        # while the patient is alive and simulation length is not yet reached
        while i < self._time_steps - 2:
            if self._coins[i:(i + 3)] == [Coin.HEAD, Coin.HEAD, Coin.TAIL]:
                self._reward += 100
            # increment time
            i += 1
        return (self._reward)


class Cohort:
    def __init__(self, name, pop_size, head_prob, time_steps):
        """ create a cohort of patients
        :param id: cohort ID
        :param pop_size: population size of this cohort
        :param head_prob
        """
        self._trials = []  # list of trials
        self._rewardsum = []  # list to store reward of each trial
        # populate the cohort
        for i in range(pop_size):
            # create a new patient (use id * pop_size + n as patient id)
            game = Game(pop_size + i, head_prob, time_steps)
            # add the patient to the cohort
            self._trials.append(game)

    def simulate(self):
        """ simulate the cohort of patients over the specified number of time-steps
        :param n_time_steps: number of time steps to simulate the cohort
        """
        # simulate all patients
        for game in self._trials:
            # simulate
            game.simulate()
            # record survival time
            self._rewardsum.append(game.countwin())

    def get_ave_reward(self):
        """ returns the average survival time of patients in this cohort """
        return sum(self._rewardsum) / len(self._rewardsum)

BIAS_COIN=0.4
POP_SIZE=1000
n_time_steps=20
# one player
my = Game(name="Casino2", head_prob=0.4,time_steps=n_time_steps)
# simulate the cohort
print(my.simulate())
print(my.countwin())

#1000 simulation
myCohort2 = Cohort(name="Casino2", pop_size=POP_SIZE, head_prob=BIAS_COIN, time_steps=n_time_steps)
# simulate the cohort
myCohort2.simulate()
# print the average reward
print('Average reward:', myCohort2.get_ave_reward())