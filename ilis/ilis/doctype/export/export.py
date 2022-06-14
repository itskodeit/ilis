# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class Export(Document):
	def before_save(self):
		self.validate_bl()
		
		# for item in self.export_container:
		# 	doc = frappe.get_doc("Container", item.container_number)
		# 	doc.update({"status": "Not-Available"}, )
		# 	doc.save()

		# for item in self.containers_on_truck:
		# 	doc = frappe.get_doc("Container", item.container_number)
		# 	doc.update({"status": "Not-Available"}, )
		# 	doc.save()
		# if self.booking_number:
		# 	doc = frappe.get_doc("Container Release", self.booking_number)
		# 	doc.export_reference = self.name
		# 	if self.stuffing_date:
		# 	 	doc.stuffing_date = self.stuffing_date
		# 	doc.save()

		# if self.arrival_date:
		# 	self.arrival_date >= self.gate_in_date

	
	# def validate(self):
	# 	if self.booking_number:
	# 		doc = frappe.get_doc("Container Release", self.booking_number)
	# 		doc.export_reference = self.name
	# 		if self.stuffing_date:
	# 		 	doc.stuffing_date = self.stuffing_date
	# 		doc.save()

	def validate_bl(self):
		if not self.validate_bl_format():
			frappe.throw(_("Incorrect Bl no format"))

	def validate_bl_format(self):
		alphabet = '0123456789A BCDEFGHIJK LMNOPQRSTU VWXYZ'
		if self.bl_number:
			for s in self.bl_number:
				if s not in alphabet:
					return False
		return True


@frappe.whitelist()
def make_cargo_tracking(source_name, target_doc=None, ignore_permissions=False):

	doclist = get_mapped_doc("Export", source_name, {
			"Export": {
				"doctype": "Cargo Tracking",
				"field_map": {
					"name": "export_reference",
					"booking_no": "booking_number",
					"bl_number": "bl_number",
					"exporter": "exporter",
					"reference_number": "reference_number",
					"consignee": "consignee",
					"shipping_line": "shipping_line",
					"vessel_name": "vessel_name",
					"discharge_port": "discharge_port",
				},
				"validation": {
					"docstatus": ["=", 0]
				},
				
			},
		}, target_doc, ignore_permissions=ignore_permissions)


	return doclist


@frappe.whitelist()
def make_container_entry(source_name, target_doc=None, ignore_permissions=False):

	doclist = get_mapped_doc("Export", source_name, {
			"Export": {
				"doctype": "Container Entry",
				"field_map": {
					"name": "export_reference",
					"booking_no": "booking_number",
				},
				"validation": {
					"docstatus": ["=", 0]
				},
				
			},
		}, target_doc, ignore_permissions=ignore_permissions)


	return doclist