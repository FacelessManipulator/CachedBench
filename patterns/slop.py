#coding=utf-8

from  __future__ import print_function
import numpy as np
import numpy.random as nrd
from base import BasePattern

class SlopBasePattern(BasePattern):
	def __init__(self, obj_num, access_max, slop, groups=10):
		super().__init__(obj_num, access_max)
		if slop < 0:
			print("Warning! write_ratio ge 0. Asssuming slop is 0.9")
			slop = 0.9
		self.slop = slop
		self.groups = groups

	def __str__(self):
		return super().__str__() + "slop: {0}, groups: {1}".format(
			self.slop, self.groups)

	def generate_weights(self, fresh=False):
		if fresh or not self.weights:
			ival = (self.access_max/self.groups) * (1-self.slop) / (1-self.slop**self.groups)
			weights = []
			for i in range(self.groups):
				weights.extend([ival]*(self.obj_num // self.groups))
				ival *= self.slop
			if len(weights) != self.obj_num:
				weights.extend([ival]*(self.obj_num - len(weights)))
			weights = np.array(weights)
			# self.weights = list(map(lambda x:x/float(sum(weights)), weights))
			self.weights = weights / weights.sum()

def generate(obj_num, access_max, slop=0.9, groups=10, times=1):
	sb = SlopBasePattern(obj_num, access_max, slop, groups)
	if times >= 0:
		for i in range(times):
			for j in sb.generate_base(True):
				yield j
	else:
		while True:
			for i in sb.generate_base(True):
				yield i

if __name__ == '__main__':
	import matplotlib.pyplot as plt
	y = generate(10, 10000, 0.7)
	ny = np.array(list(y))
	# print(ny)
	plt.hist(ny, bins=10)
	plt.show()
	
