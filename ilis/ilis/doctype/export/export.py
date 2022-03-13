# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class Export(Document):
	def before_save(self):
		self.validate_bl()
		
		for item in self.export_container:
			doc = frappe.get_doc("Container", item.container_number)
			doc.update({"status": "Not-Available"}, )
			doc.save()

		for item in self.containers_on_truck:
			doc = frappe.get_doc("Container", item.container_number)
			doc.update({"status": "Not-Available"}, )
			doc.save()
		if self.booking_number:
			doc = frappe.get_doc("Container Release", self.booking_number)
			doc.export_reference = self.name
			if self.stuffing_date:
			 	doc.stuffing_date = self.stuffing_date
			doc.save()

		# if self.arrival_date:
		# 	self.arrival_date >= self.gate_in_date

	
	def validate(self):
		if self.booking_number:
			doc = frappe.get_doc("Container Release", self.booking_number)
			doc.export_reference = self.name
			if self.stuffing_date:
			 	doc.stuffing_date = self.stuffing_date
			doc.save()

	def validate_bl(self):
		if len(self.bl_number) != 13:
			frappe.throw(_("Please confirm Bl no length"))
		if not self.validate_bl_format():
			frappe.throw(_("Incorrect Bl no format"))

	def validate_bl_format(self):
		alphabet = '0123456789A BCDEFGHIJK LMNOPQRSTU VWXYZ'
		numerals = "0123456789"
		total_numerals = 0
		for s in self.bl_number:
			if s not in alphabet:
				return False
			if s in numerals:
				total_numerals += 1
		if total_numerals != 9:
			return False
		return True
