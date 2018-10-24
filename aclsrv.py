#!/usr/bin/env python

class AclSrv(object):
	def __init__(self, groups, services):
		self.groups = groups
		self.services = services

	def register_service()