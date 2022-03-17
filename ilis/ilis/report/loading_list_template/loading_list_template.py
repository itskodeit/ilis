# Copyright (c) 2013, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate, today, date_diff, add_days


def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_column()
	data=[]

	report_items = get_data(filters)
	for d in report_items:
		row = {}
		row['container_number'] = d.container_number
		row['iso'] = d.iso
		row['size'] = d.size
		row['type'] = d.type
		row['weight'] = d.weight
		row['vessel'] = d.vessel

		row['shipping_line'] = d.shipping_line	
		row['document_number'] = d.document_number	
		row['shipper'] = d.shipper

		row['commodity'] = d.commodity
		row['pod'] = d.pod
		row['origin'] = d.origin
		row['seal'] = d.seal
		row['fcl'] = d.fcl



		data.append(row)

	return columns, data


def get_column():
	return [
		{
			"fieldname":"container_number",
			"label": "CNT No",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"iso",
			"label": "ISO",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"fieldname":"size",
			"label": "Size",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"fieldname":"type",
			"label": "Type",
			"fieldtype": "Data",
			"width": 100,
		},
				{
			"fieldname":"weight",
			"label": "Gross Weight",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"vessel",
			"label": "Vessel Reference",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"fieldname":"shipping_line",
			"label": "Line",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"fieldname":"document_number",
			"label": "Document Number",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"shipper",
			"label": "Shipper",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"commodity",
			"label": "Commodity",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"pod",
			"label": "POD",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"fieldname":"origin",
			"label": "Origin",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"fieldname":"seal",
			"label": "Seal",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"fieldname":"fcl",
			"label": "FCL",
			"fieldtype": "Data",
			"width": 150,
		},

	]


def get_data(filters):
	where_filter = {"from_date": filters.from_date, "to_date": filters.to_date}
	where = ""

	data = frappe.db.sql("""select tce.container_number,tce.type, tce.size, tce.iso,
		tce.weight, tce.vessel, tce.shipping_line, tce.document_number, tce.shipper,

		tce.commodity, tce.pod, tce.fcl, tce.seal, tce.origin
		

		from `tabContainer Export` tce
		LEFT JOIN 
			`tabExport` ta ON tce.parent = ta.name
		where ta.loading_date BETWEEN %(from_date)s AND %(to_date)s
		order by ta.loading_date
		"""+ where, where_filter, as_dict=1)
	return data
