# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Export(Document):
	def before_save(self):

		for item in self.export_container:
			doc = frappe.get_doc("Container", item.container_number)
			doc.update({"status": "Not-Available"}, )
			doc.save()

		for item in self.containers_on_truck:
			doc = frappe.get_doc("Container", item.container_number)
			doc.update({"status": "Not-Available"}, )
			doc.save()
		# if self.booking_number:
		# 	doc = frappe.get_doc("Container Release", self.booking_number)
		# 	doc.export_reference = self.name
		# 	if self.stuffing_date:
		# 	 	doc.stuffing_date = self.stuffing_date
		# 	doc.save()

	def validate(self):
		if self.booking_number:
			doc = frappe.get_doc("Container Release", self.booking_number)
			doc.export_reference = self.name
			if self.stuffing_date:
			 	doc.stuffing_date = self.stuffing_date
			doc.save()
