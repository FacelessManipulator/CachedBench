#coding=utf-8

from  __future__ import print_function
import numpy as np
import numpy.random as nrd
from uniform import UniformPattern

class RWProperyPattern():
	WRITE = 1
	READ = 0

	def __init__(self, base, write_ratio):
		self.base = base
		if write_ratio < 0:
			print("Warning! write_ratio ge 0. Asssuming write_ratio is 0.")
			write_ratio = 0
		self.write_ratio = write_ratio
		self.created = []

	def __str__(self):
		return "write ratio: {0}".format(self.write_ratio_expect)

	def __repr__(self):
		return str(self)

	def clean_state(self):
		self.created = []

	def generate(self):
		# generate a uniform choose seq.
		return self.generate_property(self.base, with_base=True)

	def generate_property(self, base, with_base=False):
		# generate the rw state seq.
		rw = nrd.choice([self.WRITE, self.READ], size=base.access_max, 
				p=[self.write_ratio, 1-self.write_ratio])
		for pair in zip(base.generate_base(fresh=False), rw):
			if pair[0] not in self.created:
				self.created.append(pair[0])
				if with_base:
					yield (pair[0], self.WRITE)
				else:
					yield self.WRITE
			else:
				if with_base:
					yield pair
				else:
					yield pair[1]

def generate(obj_num, access_max, write_ratio, times=1):
	b = UniformPattern(obj_num, access_max)
	p = RWProperyPattern(b, write_ratio)
	if times >= 0:
		b.clean_state()
		for i in range(times):
			for j in p.generate():
				yield j
	else:
		while True:
			b.clean_state()
			for i in p.generate():
				yield i

if __name__ == '__main__':
	import matplotlib.pyplot as plt
	y1 = generate(100, 1000, 0.7)
	ny = np.array(list(y1))
	plt.hist(ny[:,0], bins=10)
	plt.show()
	
