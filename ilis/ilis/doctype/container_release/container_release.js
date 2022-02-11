// Copyright (c) 2022, Ikode-IT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Container Release', {
	refresh: function(frm) {

	},

	release_date: function(frm) {
		$.each(frm.doc.containers_released || [], function(i, d) {
			if(!d.release_date) d.release_date = frm.doc.release_date;
		});
		refresh_field("containers_released");
	},

	cfs_arrival_date: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("cfs_storage_days", frappe.datetime.get_day_diff( to_date , frm.doc.cfs_arrival_date));
		refresh_field(frm.doc.cfs_storage_days);
	},

});

frappe.ui.form.on("Container Export", {
	container_number: function(frm,cdt,cdn) {
		var row = locals[cdt][cdn];
		if (frm.doc.release_date) {
			row.release_date = frm.doc.release_date;
			refresh_field("release_date", cdn, "containers_released");
		} else {
			frm.script_manager.copy_from_first_row("containers_released", row, ["release_date"]);
		}
	},
	release_date: function(frm, cdt, cdn) {
		if(!frm.doc.release_date) {
			erpnext.utils.copy_value_in_all_rows(frm.doc, cdt, cdn, "containers_released", "release_date");
		}
	}
});