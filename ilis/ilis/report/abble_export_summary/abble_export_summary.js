// Copyright (c) 2016, Ikode-IT and contributors
// For license information, please see license.txt
/* eslint-disable */
var aday = new Date();
var to_date = aday.toISOString().split('T')[0];
aday.setDate(aday.getDate() - 7);
var from_date = aday.toISOString().split('T')[0];
var cur_report = null;


frappe.query_reports["Abble Export Summary"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": from_date,
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": to_date
		},
	],

	"formatter":function (value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);
    if (data.cfs_free_days < 10 && column.id == 'cfs_free_days' ) {
            value = "<span style='color:red!important;font-weight:bold'>" + value + "</span>";

     }
    if (data.free_days < 16 && column.id == 'free_days' ) {
            value = "<span style='color:red!important;font-weight:bold'>" + value + "</span>";

    }

    return value
	}
};
