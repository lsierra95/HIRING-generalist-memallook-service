# /memallook/memallook.py
# Code below handles the creation, maintenance, and visualization of a memory buffer

import math

class Memalook:
	def __init__(self):
		self.vheap = None
		self.memory = None
		self.p = None
		self.N = None
		self.tag = None
		self.id = 100

	# First operation to be invoked
	# Creates virtual heap iff no maintained vheap exists
	def new(self, p: int, N: int):
		if self.vheap:
			return "ERROR: Virtual heap already exists"

		else:
			self.vheap = {}
			self.memory = N * p
			self.p = p
			self.N = N
			self.tag = 1

		return "SUCCESS: HEAP-%d of size %d created"%(self.id, self.memory)

	# Allocates m bytes of in buffer and returns unique tag t
	# Returns error if maintained vheap doesn't exist or not enough memory
	def alloc(self, M: int):
		if self.vheap == None:
			return "ERROR: Allocation Failed, vheap doesn't exist"
		# check if we have enough pages or total memory
		if M > self.memory or self.memory < self.p:
			return "ERROR: Allocation Failed, not enough memory"

		self.vheap[self.tag] = M
		self.memory -= M
		t = self.tag
		self.tag += 1

		return "SUCCESS, Tag %d"%(t)

	# Deallocates block with tag t
	# Returns error if t doesn't exist
	def dealloc(self, T: int):
		if self.vheap == None:
			return "ERROR: Failed, vheap doesn't exist"
		# handles user trying to deallocate a previousy deallocated tag
		if T not in self.vheap or self.vheap[T] < 0:
			return "ERROR: Failed, uknown tag"

		self.memory -= self.vheap[T]
		# change vheap[T] to -vheap[T] to keep track of |M| bytes that were prev allocated
		self.vheap[T] *= -1
		return "SUCCESS: Deallocated Tag %d"%(T)

	# Visualizes heap and lists allocated tags
	def show(self):
		if not self.vheap:
			return "ERROR: Failed, vheap doesn't exist"
		h = ""
		allocs = ["<Allocations by tag>"]
		blocks = 0

		for T in self.vheap:
			if self.vheap[T] > 0:
				allocs.append("%d: %d bytes"%(T, self.vheap[T]))

			b = math.ceil(abs(self.vheap[T]) / self.p)
			h += str(T) * b if self.vheap[T] > 0 else "*" * b
			blocks += b 

		h += "*" * (self.N - blocks)
		sq = int(math.sqrt(self.N))

		return ([h[i:i+sq] for i in range(0, self.N, sq)], allocs)

	# Resets any maintained vheap
	def reset(self):
		if self.vheap:
			self.vheap = None
			self.id += 1
			return "SUCCESS: Reset complete"

		return "ERROR: Failed, vheap doesn't exist"

	# Degragments memory buffer
	def defrag(self):
		if self.vheap:
			self.vheap = {T: v for T, v in self.vheap.items() if v > 0}
			return "SUCCESS: Defragmented vheap"

		return "ERROR: Failed, vheap doesn't exist"





