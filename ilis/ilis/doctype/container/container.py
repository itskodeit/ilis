# -*- coding: utf-8 -*-
# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class Container(Document):
	pass

# @frappe.whitelist
# def validate_container(number):
# 	if len(number) != 11:
# 		frappe.msgprint("Container No length not valid:")