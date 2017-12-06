#coding=utf-8

from  __future__ import print_function
import numpy as np
import numpy.random as nrd
from base import BasePattern

class UniformPattern(BasePattern):
	def __init__(self, obj_num, access_max):
		super().__init__(obj_num, access_max)
		
	def __str__(self):
		return super().__str__() + "write ratio: {0}".format(
			self.write_ratio_expect)

	def __repr__(self):
		return str(self)

	def generate_weights(self, fresh=False):
		if fresh or self.weights is None:
			weights = np.ones(self.obj_num)
			self.weights = weights / weights.sum()


def generate(obj_num, access_max, times=1):
	sb = UniformPattern(obj_num, access_max)
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
	y = generate(10, 1000)
	ny = np.array(list(y))
	# print(ny)
	plt.hist(ny, bins=10)
	plt.show()
	
