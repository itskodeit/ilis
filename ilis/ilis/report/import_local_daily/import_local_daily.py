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
		row['bl_number'] = d.bl_number
		row['client'] = d.client
		row['reference_number'] = d.reference_number

		row['eta'] = d.eta
		row['etb'] = d.etb
		row['discharge_date'] = d.discharge_date
		row['vessel_name'] = d.vessel_name
		row['shipping_line'] = d.shipping_line
		row['cfs'] = d.cfs
		row['delivery_order'] = d.delivery_order
		row['carry_in'] = d.carry_in_date		

		
		row['apply_tbs_permit'] = d.apply_tbs_permit		
		row['verify_invoice'] = d.verify_invoice
		row['destination'] = d.destination

		



		data.append(row)

	return columns, data


def get_column():
	return [
		{
			"fieldname":"client",
			"label": "Client",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"bl_number",
			"label": "TRA Reference No",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"bl_number",
			"label": "TANSAD No",
			"fieldtype": "Data",
			'width': 150
		},
			{
			"fieldname":"destination",
			"label": "Status",
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"fieldname":"bl_number",
			"label": "Bill",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"container_number",
			"label": "Container",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"vessel_name",
			"label": "Vessel Name",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"eta",
			"label": "ETA ",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"etb",
			"label": "ETB ",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"discharge_date",
			"label": "Discharge Date ",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"carry_in",
			"label": "Clearance ",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"carry_in",
			"label": "Carry In",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"carry_in",
			"label": "Deadline",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"cfs",
			"label": "Clearance Point",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"destination",
			"label": "Destination ",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"shipping_line",
			"label": "Shipping Line",
			"fieldtype": "Data",
			"width": 120,
		},

		{
			"fieldname":"delivery_order",
			"label": "Delivery Order",
			"fieldtype": "Date",
			"width": 120,
		},

		{
			"fieldname":"apply_tbs_permit",
			"label": "TBS",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"verify_invoice",
			"label": "Verification",
			"fieldtype": "Date",
			"width": 120,
		},




	
	]


def get_data(filters):
	where_filter = {"from_date": filters.from_date, "to_date": filters.to_date}
	where = ""

	data = frappe.db.sql("""select ti.client, ti.documents_received, 
		ti.eta, ti.etb, ti.discharge_date, ti.vessel_name, ti.shipping_line,
		ti.delivery_order, ti.apply_tbs_permit, ti.bl_number, ti.verify_invoice,
		ti.destination, ti.carry_in_date, ti.cfs

		from `tabImport` ti
		where ti.documents_received BETWEEN %(from_date)s AND %(to_date)s
		order by ti.documents_received
		"""+ where, where_filter, as_dict=1)
	return data
