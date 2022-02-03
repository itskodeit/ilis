// Copyright (c) 2022, Ikode-IT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Abble', {
	// refresh: function(frm) {

	// }

	setup: function(frm){
		frm.set_query("container_number", "containers_on_truck", function(doc, cdt, cdn){
			let row = locals[cdt] [cdn]
			return {
				filters: [
					['Container','status','=', 'Available'],
				]
			}
		});

		frm.set_query("container_number", "export_container", function(doc, cdt, cdn){
			let row = locals[cdt] [cdn]
			return {
				filters: [
					['Container','status','=', 'Available'],
				]
			}
		});
	}
});
