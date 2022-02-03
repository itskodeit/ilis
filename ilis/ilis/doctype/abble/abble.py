# -*- coding: utf-8 -*-
# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Abble(Document):
	def before_save(self):
		for item in self.export_container:
			doc = frappe.get_doc("Container", item.container_number)
			doc.update({"status": "Not-Available"}, )
			doc.save()

		for item in self.containers_on_truck:
			doc = frappe.get_doc("Container", item.container_number)
			doc.update({"status": "Not-Available"}, )
			doc.save()

