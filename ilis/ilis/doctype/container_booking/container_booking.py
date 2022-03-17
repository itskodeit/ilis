# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class ContainerBooking(Document):
	def on_submit(self):
		if self.approval_status == "Pending":
			frappe.throw(_("Booking not Approved"))

@frappe.whitelist()
def make_container_release(source_name, target_doc=None, ignore_permissions=False):

	doclist = get_mapped_doc("Container Booking", source_name, {
			"Container Booking": {
				"doctype": "Container Release",
				"field_map": {
					"name": "booking_reference",
					"booking_no": "booking_number",
					"shipping_line": "shipping_line",
					"depot": "depot",
					"no_of_containers": "no_of_containers",
				},
				"validation": {
					"docstatus": ["=", 1]
				},
				
			},
		}, target_doc, ignore_permissions=ignore_permissions)


	return doclist
