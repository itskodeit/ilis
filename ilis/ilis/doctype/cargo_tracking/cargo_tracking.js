// Copyright (c) 2022, Ikode-IT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cargo Tracking', {
	refresh: function(frm) {
		
		// filter container by export & purpose
		frm.fields_dict['container_on_truck'].get_query = function (doc) {
            return {
                filters: [
                    ['export_reference', '=', frm.doc.export_reference],
                    ['purpose', '=', 'Container Entry']
                ]
            }
        }
	},

	setup: function(frm){
		frm.set_query("container_number", "export_container", function(doc, cdt, cdn){
			let row = locals[cdt] [cdn]
			return {
				filters: [
					['Container','purpose','!=', 'Container Entry'],
					['Container','export_reference','=', doc.export_reference],
				]
			}
		});

		frm.set_query("container_number", "containers_on_truck", function(doc, cdt, cdn){
			let row = locals[cdt] [cdn]
			return {
				filters: [
					['Container','purpose','=', 'Container Entry'],
				]
			}
		});
	},

	vessel_name: function(frm) {
		$.each(frm.doc.export_container || [], function(i, d) {
			if(!d.vessel) d.vessel = frm.doc.vessel_name;
		});
		refresh_field("export_container");
	},
	shipping_line: function(frm) {
		$.each(frm.doc.export_container || [], function(i, d) {
			if(!d.shipping_line) d.shipping_line = frm.doc.shipping_line;
		});
		refresh_field("export_container");
	},
	discharge_port: function(frm) {
		$.each(frm.doc.export_container || [], function(i, d) {
			if(!d.pod) d.pod = frm.doc.discharge_port;
		});
		refresh_field("export_container");
	},
	tracking_status: function(frm) {
		$.each(frm.doc.containers_on_truck || [], function(i, d) {
			if(!d.status) d.status = frm.doc.tracking_status;
		});
		refresh_field("containers_on_truck");
	},

});

frappe.ui.form.on("Cargo Tracking", "validate", function(frm) {
	if (frm.doc.tunduma_departure_date < frm.doc.tunduma_arrival) {
		frappe.msgprint(__("Tunduma Arrival date cannot be later than Departure"));
		frappe.validated = false;
	}
	if (frm.doc.gate_in_date < frm.doc.arrival_date) {
		frappe.msgprint(__("Arrival date cannot be later than Gate in Date"));
		frappe.validated = false;
	}
	if (frm.doc.stuffing_date < frm.doc.offloading_date) {
		frappe.msgprint(__(" Offloading date cannot be later than Stuffing  Date"));
		frappe.validated = false;
	}
	if (frm.doc.delivery_date < frm.doc.stuffing_date) {
		frappe.msgprint(__("Stuffing date cannot be later than Port Delivery  Date"));
		frappe.validated = false;
	}
	
});

frappe.ui.form.on("Container Export", {
	container_number: function(frm,cdt,cdn) {
		
		var row = locals[cdt][cdn];
		//doc = frappe.get_doc("Container", row.container_number);
		//console.log(doc);
		var doc = {}
		frappe.call({
	        method: "frappe.client.get",
	        args: {
	            doctype: "Container",
	            name: row.container_number,
        	},
	        callback(r) {
	            if(r.message) {
	            	row.type = r.message.size
	            	row.iso = r.message.iso
	            	row.size = r.message.size
	            	row.seal = r.message.seal
	                console.log(r.message.size);
	                console.log(r.message.size);
	                
	            }
	        }
    	});
    	refresh_field("size", cdn, "export_container");
    	//console.log(row.size);

		row.weight = frm.doc.after_balance
		row.document_number = frm.doc.booking_number
		row.shipper = frm.doc.exporter
		row.commodity = frm.doc.cargo
		row.origin = frm.doc.loading_place
		row.fcl = "FCL"
	}
});

frappe.ui.form.on("Container Details", {
	container_number: function(frm,cdt,cdn) {
		
		var row = locals[cdt][cdn];
		//doc = frappe.get_doc("Container", row.container_number);
		//console.log(doc);
		var doc = {}
		frappe.call({
	        method: "frappe.client.get",
	        args: {
	            doctype: "Container",
	            name: row.container_number,
        	},
	        callback(r) {
	            if(r.message) {
	            	row.container_type = r.message.type
	         		row.size = r.message.size
	            	row.seal = r.message.seal
	            	
	                console.log(r.message.size);
	                
	            }
	        }
    	});
    	refresh_field("size", cdn, "containers_on_truck");
    	//console.log(row.size);

		row.transporter = frm.doc.transporter
		row.cargo = frm.doc.cargo
		row.status = frm.doc.tracking_status
		row.shipper = frm.doc.exporter
		row.shipping_line = frm.doc.shipping_line
		row.vessel = frm.doc.vessel_name
		row.pod = frm.doc.discharge_port

	}
});