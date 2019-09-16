import matplotlib
# import tkinter
matplotlib.use("Agg")
from pybrain.rl.learners.valuebased import ActionValueNetwork, ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q, SARSA, NFQ
from pybrain.rl.experiments import EpisodicExperiment, Experiment
from game_environment import GameEnvironment
from game_task import GameTask
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader
from numpy import mean
from pybrain.optimization import CMAES
from pybrain.tools.shortcuts import buildNetwork
from pybrain.rl.agents import OptimizationAgent
from pybrain.utilities import fListToString
import pylab
import tkinter

if __name__ == "__main__":

	environment = GameEnvironment()

	task = GameTask(environment)
	modules = [
		# ActionValueNetwork(103, 40),
		# ActionValueNetwork(103, 40),
		ActionValueNetwork(103, 40)
	]

	
	# module = ActionValueTable(103, 40)
	# network = buildNetwork(task.outdim, 5, task.indim)

	
	cmd = input("(l)oad network or (n)ew? > ")

	if cmd != "n" :
		for module in modules :
			network = NetworkReader.readFrom("best_net.xml")
			

	# learner = CMAES(storeAllEvaluations = True)
	# learner = SARSA()
	learner = NFQ()
	
	# agent = OptimizationAgent(network, learner)
	while True :
		bestModule = None
		maxFitness = -100
		for module in modules :
			agent = LearningAgent(module, learner)
			experiment = EpisodicExperiment(task, agent)
			reward = [sum(x) for x in experiment.doEpisodes(10)]
			print("Avg: {}  Reward: {}etc..".format(mean(reward), reward))
			agent.learn()
			if mean(reward) > maxFitness :
				maxFitness = mean(reward)
				bestModule = module
			agent.reset()
		NetworkWriter.writeToFile(bestModule.network, "best_net.xml")

	# experiment = Experiment(task, agent)

	# while (True) :
	# print(experiment.doInteractions(100))
	# experiment.doEpisodes(1000)
	# score = environment.getScore()
		# n, fit = learner._bestFound()
		# ns.append(n)
		# print(n)
		# pylab.pcolor(module.params.reshape(103, 40).max(1).reshape(9,9))
		# pylab.pcolor(ns)
		# pylab.draw()
	# print('Episodes learned from:', len(learner._allEvaluations))
	# print('Best fitness found:', fit)
	# print('with this network:')
	# print(n)
	# print('containing these parameters:')
	# print(fListToString(n.params, 4))

# from matplotlib import pyplot as plt

# def plotPerformance(values, fig):
	# plt.figure(fig.number)
	# plt.clf()
	# plt.plot(values, 'o-')
	# plt.gcf().canvas.draw()
	# # Without the next line, the pyplot plot won't actually show up.
	# plt.pause(0.001)
	# plt.ion()
	# reward_fig = plt.figure()
	# score_fid = plt.figure()
	# module.initialize(1.)
	# learner.explorer.epsilon = 0.4
	# rewards.append()
	# while(score < 10) :
	# experiment.doEpisodes(100)
	# f = open('hanabi_net', 'w')
	# help(module.network.copy())
	# pickle.dump(module.network, f)
	# f.close()
	# plotPerformance(rewards, reward_fig)
	


