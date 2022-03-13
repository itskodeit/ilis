# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ContainerBooking(Document):
	def on_submit(self):
		if self.approval_status == "Pending":
			frappe.throw(_("Booking not Approved"))
