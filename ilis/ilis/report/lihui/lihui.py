# Copyright (c) 2013, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_column()
	data=[]

	report_items = get_data(filters)
	for d in report_items:
		row = {}
		
		row['transporter'] = d.transporter
		row['drivers_name'] = d.drivers_name
		row['license_number'] = d.license_number
		row['truck'] = d.truck
		row['trailer'] = d.trailer
		row['container_number'] = d.container_on_truck
		row['reference_number'] = d.reference_number
		row['package'] = d.package
		row['exporter'] = d.exporter
		row['consignee'] = d.consignee
		row['loading_place'] = d.loading_place
		row['loading_date'] = d.loading_date
		row['laoding_tons'] = d.laoding_tons
		row['offloading_weight'] = d.offloading_weight
		row['tunduma_arrival'] = d.tunduma_arrival
		row['tunduma_departure_date'] = d.tunduma_departure_date
		row['arrival_date'] = d.arrival_date
		row['offloading_date'] = d.offloading_date

		row['crn'] = d.crn
		row['crn_received'] = d.crn_received
		row['cfs'] = d.cfs
		row['tracking_status'] = d.tracking_status
		row['destination'] = d.destination


		data.append(row)

	return columns, data


def get_column():
	return [
		{
			"fieldname":"transporter",
			"label": "Transporter",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"drivers_name",
			"label": "Driver ",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"license_number",
			"label": "Driver's License",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"truck",
			"label": "Truck",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"trailer",
			"label": "Trailer",
			"fieldtype": "Data",
			'width': 150
		},
				{
			"fieldname":"container_number",
			"label": "Container",
			"fieldtype": "Link",
			"options": "Container",
			'width': 200
		},
		{
			"fieldname":"reference_number",
			"label": "Reference No",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"package",
			"label": "Package",
			"fieldtype": "float",
			"width": 120,
		},
		{
			"fieldname":"exporter",
			"label": "Shipper",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"consignee",
			"label": "Consignee",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"loading_place",
			"label": "Loading Point",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"loading_date",
			"label": "Loading Date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"laoding_tons",
			"label": "Loading Weight(T)",
			"fieldtype": "float",
			"width": 120,
		},
		{
			"fieldname":"offloading_weight",
			"label": "OffLoading Weight(T)",
			"fieldtype": "float",
			"width": 120,
		},
		{
			"fieldname":"tunduma_arrival",
			"label": "Tunduma Arrival",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"tunduma_departure_date",
			"label": "Tunduma Departure",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"arrival_date",
			"label": "Arrival CFS DAR ",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"offloading_date",
			"label": "offLoading Date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"crn",
			"label": "CRN Number",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"crn_received",
			"label": "CRN Received",
			"fieldtype": "Date",
			"width": 120,
		},		
		{
			"fieldname":"cfs",
			"label": "OffLoading Yard",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"offloading_date",
			"label": "Empty Container returned to SL Date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"tracking_status",
			"label": "Status",
			"fieldtype": "Data",
			"width": 120,
		},

		{
			"fieldname":"destination",
			"label": "Destination",
			"fieldtype": "Data",
			"width": 120,
		},
		

	
	]


def get_data(filters):
	where_filter = {"from_date": filters.from_date, "to_date": filters.to_date}
	where = ""

	data = frappe.db.sql("""select
		ta.transporter, ta.drivers_name, ta.license_number, ta.truck, ta.trailer,
		ta.container_on_truck, ta.reference_number, ta.package, ta.exporter, ta.consignee,		
		ta.loading_place, ta.loading_date, ta.laoding_tons, ta.offloading_weight,
		ta.tunduma_arrival, ta.tunduma_departure_date, ta.arrival_date, ta.offloading_date,
		ta.crn, ta.crn_received, ta.cfs, ta.tracking_status,
		te.destination

		from `tabCargo Tracking` ta
		LEFT JOIN 
			`tabExport` te ON ta.export_reference = te.name
		where ta.loading_date BETWEEN %(from_date)s AND %(to_date)s
		AND ta.docstatus !=2
		order by ta.loading_date
		"""+ where, where_filter, as_dict=1)
	return data
