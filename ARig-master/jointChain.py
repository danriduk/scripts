'''
joint chain class
'''

import maya.cmds as mc
from . import checks, utils



class jntChain():
	def __init__(
		self,
		prefix='c',
		name='joint',
		suffix='jnt',
		posList=[(0,0,0)]
		):	

		self.prefix = prefix
		self.name = name
		self.suffix = suffix
		self.posList = posList

		self.jnts = []

	def build(self):
		# create joints from pos list
		for p in reversed(self.posList):
			# clear selection to create joints in root
			mc.select(cl=1)

			# get unique name
			fullName = checks.uniqueName(self.prefix, self.name, self.suffix)
			print fullName
			jnt = mc.joint(name=fullName, p=p)
			self.jnts.append(jnt)

		utils.iterParenting(self.jnts)

	def displayAxis(self, jnts=[]):
		# toggle display axis
		for jnt in jnts:
			attr = mc.getAttr('{0}.displayLocalAxis'.format(jnt))
			mc.setAttr('{0}.displayLocalAxis'.format(jnt), not attr)
