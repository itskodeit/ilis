# -*- coding: utf-8 -*-
# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Container(Document):
	def before_save(self):
		self.validate_container()

	def validate_container(self):
		if len(self.container_number) != 11:
			frappe.throw(_("Please confirm container no length"))
		if not self.validate_container_format():
			frappe.throw(_("Incorrect container no format"))

	def validate_container_format(self):
		alphabet = '0123456789A BCDEFGHIJK LMNOPQRSTU VWXYZ'
		numerals = "0123456789"
		total_numerals = 0
		for s in self.container_number:
			if s not in alphabet:
				return False
			if s in numerals:
				total_numerals += 1
		if total_numerals != 7:
			return False
		return True

