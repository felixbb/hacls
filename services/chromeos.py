#!/usr/bin/env python

from service import AcldService

SERVICE_CONFIG = """
{
	"namespace":"chromeos",
	"resources": [
		{
			"type":"project",
			"container":true,
			"anchor":true,
			"parent":null,
		},
		{
			"type":"builder",
			"container":true,
			"anchor":true,
			"parent":"project"
		},
		{
			"type":"build",
			"container":true,
			"anchor":true,
			"parent":"builder",
		},
		{
			"type":"log",
			"container":false,
			"anchor":false,
			"parent":"build"
		}
	],
	"roles": [
		{
			"name":"administrator",
			"includeAll":true
		},
		{
			"name":"logreader",
			"includeAll":false,
			"actions": [
				"logs.read"
			]
		}
	]
}
"""

class ChromeOS(AcldService):
	def __init__(self):
		pass
