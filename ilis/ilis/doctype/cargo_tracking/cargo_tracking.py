# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class CargoTracking(Document):
	pass
	# def on_submit(self):
	# 	update_export_container(self)


# @frappe.whitelist(allow_guest=True)
# def update_export_container(doc):
# 	export_doc = frappe.get_doc("Export", doc.export_reference)
# 	for value in doc.export_container:
# 		export_doc.export_container.append({
# 			"container_number": value.container_number,
# 			"iso": value.iso,
# 			"size": value.size,
# 			"type": value.type,
# 			"weight": value.weight,
# 			"vessel": value.vessel,
# 			"shipping_line": value.shipping_line,
# 			"document_number": value.document_number,
# 			"shipper": value.shipper,
# 			"commodity": value.commodity,
# 			"pod": value.pod,
# 			"origin": value.origin,
# 			"seal": value.seal,
# 			"fcl": value.fcl,
# 			})
# 		export_doc.save()