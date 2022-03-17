# -*- coding: utf-8 -*-
# Copyright (c) 2022, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from ilis.check_container import validate


class ContainerRelease(Document):
	

    def on_submit(self):
        create_container(self);
        
        
@frappe.whitelist(allow_guest=True)
def create_container(doc):
    # check if container exists

    for value in doc.container_collected:
        new_container = frappe.new_doc("Container")
        new_container.update({
            "reference_container_release": doc.doctype,
            "creation_document_no": doc.name,
            "booking_number":doc.booking_number,
            "shipping_line":doc.shipping_line,
            "release_date": doc.release_date,
            "type": value.container_type,
            "size": value.size,
            "container_number": value.container_number,
            "seal": value.seal,
            "export_reference": doc.export_reference,
            "parenttype": 'Export',
            "parent": doc.export_reference,
            "parentfield": 'container_details'
        })
        new_container.insert(ignore_permissions=True)

