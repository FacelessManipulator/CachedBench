#coding=utf-8

from  __future__ import print_function
import numpy as np
import numpy.random as nrd
from abc import ABCMeta, abstractmethod

class BasePattern(metaclass=ABCMeta):
	def __init__(self, obj_num, access_max):
		self.total_access = 0
		if obj_num <= 0 or access_max <= 0:
			raise Exception("Error! obj_num and access_max should gt 0.")
		self.obj_num = obj_num
		self.access_max = access_max
		self.data = None
		self.weights = None

	def __str__(self):
		return ("total access: {0}, object num: {1}, " +\
			"access max: {2} ").format(self.total_access, 
			self.obj_num, self.access_max
			)

	def __repr__(self):
		return str(self)

	def clean_state(self):
		self.data = None
		self.weights = None

	@abstractmethod
	def generate_weights(self, fresh=False):
		if fresh or self.weights is None:
			weights = np.ones(self.obj_num)
			self.weights = weights / weights.sum()

	def generate(self):
		self.generate_weights()
		return nrd.choice(range(self.obj_num), p=self.weights, size=self.access_max)

	def generate_base(self, fresh=False):
		if fresh or not self.data:
			self.data = self.generate()
		return self.data

def generate(obj_num, access_max=1000, times=1):
	bp = BasePattern(obj_num, access_max)
	if times >= 0:
		for it in range(times):
			for num in bp.generate():
				yield num
	else:
		while True:
			for num in bp.generate():
				yield num


if __name__ == '__main__':
	# import matplotlib.pyplot as plt
	# y = generate(100, 1000, 10)
	# plt.hist(list(y))
	# plt.show()
	print("can not ")
