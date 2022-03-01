# -*- coding: utf-8 -*-
# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
from ilis.check_container import validate


class ContainerRelease(Document):
	pass
	# def before_save(self):
	# 	if self.containers_released:
	# 		for c in self.containers_released:
	# 			validate(c.container_number)
