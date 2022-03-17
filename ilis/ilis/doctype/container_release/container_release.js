// Copyright (c) 2022, Ikode-IT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Container Release', {
	refresh: function(frm) {
		console.log(frm);
		/*frm.add_custom_button(__("Get Container Booking"), function() {
            show_container_dialog(frm);
        });*/
		
		// filter export by booking number
		frm.fields_dict['export_reference'].get_query = function (doc) {
            return {
                filters: [
                    ['booking_number', '=', frm.doc.booking_number]
                ]
            }
        }
	},

	release_date: function(frm) {
		$.each(frm.doc.container_collected || [], function(i, d) {
			if(!d.release_date) d.release_date = frm.doc.release_date;
		});
		refresh_field("container_collected");

		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		console.log("here");
		frm.set_value("demmurage_count", frappe.datetime.get_day_diff( 
			frappe.datetime.add_days(frm.doc.release_date, parseInt(frm.doc.free_days)), to_date));
		refresh_field(frm.doc.demmurage_count);
	},

	free_days: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		
		frm.set_value("demmurage_count", frappe.datetime.get_day_diff( 
			frappe.datetime.add_days(frm.doc.release_date, parseInt(frm.doc.free_days)), to_date));
		refresh_field(frm.doc.demmurage_count);
	},

	cfs_arrival_date: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("cfs_storage_days", frappe.datetime.get_day_diff( 
				frappe.datetime.add_days(frm.doc.cfs_arrival_date, parseInt(frm.doc.free_days_empty)), to_date));
		refresh_field(frm.doc.cfs_storage_days);
	},
	free_days_empty: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("cfs_storage_days", frappe.datetime.get_day_diff( 
				frappe.datetime.add_days(frm.doc.cfs_arrival_date, parseInt(frm.doc.free_days_empty)), to_date));
		refresh_field(frm.doc.cfs_storage_days);
	},

	stuffing_date: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("stuffed_counter", 
			frappe.datetime.get_day_diff( frappe.datetime.add_days(frm.doc.stuffing_date, frm.doc.free_days_stuffed), to_date));
		refresh_field(frm.doc.stuffed_counter);
	},
	free_days_stuffed: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("stuffed_counter", 
			frappe.datetime.get_day_diff( frappe.datetime.add_days(frm.doc.stuffing_date, frm.doc.free_days_stuffed), to_date));
		refresh_field(frm.doc.stuffed_counter);
	},


});

frappe.ui.form.on("Container Collected", {
	container_number: function(frm,cdt,cdn) {
		var row = locals[cdt][cdn];
		if (frm.doc.release_date) {
			row.release_date = frm.doc.release_date;
			refresh_field("release_date", cdn, "container_collected");
		} else {
			frm.script_manager.copy_from_first_row("container_collected", row, ["release_date"]);
		}
	},
	release_date: function(frm, cdt, cdn) {
		if(!frm.doc.release_date) {
			erpnext.utils.copy_value_in_all_rows(frm.doc, cdt, cdn, "container_collected", "release_date");
		}
	}
});

/*function show_container_dialog(frm) {
   frappe.prompt([
      {'fieldname': 'booking_reference', 'fieldtype': 'Link', 'label': 'Container Booking', 'reqd': 1, 'options': 'Container Booking'},
    
   ],
   function(booking_number){
      console.log(booking_number.booking_reference);
      //get_container_booking(booking_number.booking_reference);
   },
   'Get Containers Booking',
  )
}*/

/*function get_container_booking(booking_number) {
  frappe.call({
    "method": "frappe.client.get",
    "args": {
        "doctype": "Container Booking",
        "name": booking_number
    },
    "callback": function(response) {
         // add items to your child table
         var sinv = response.message;
         console.log(sinv.booking_no);
         console.log(sinv.depot);
         console.log(sinv.no_of_containers);
             //var child = cur_frm.add_child('export_container');
             cur_frm.set_value('booking_number', sinv.booking_no);
             cur_frm.refresh_field('booking_number');

             cur_frm.set_value('depot', sinv.depot);
             cur_frm.refresh_field('depot');

             cur_frm.set_value('no_of_containers', sinv.no_of_containers);
             cur_frm.refresh_field('no_of_containers');

			cur_frm.set_value('booking_reference', sinv.name);
            cur_frm.refresh_field('booking_reference');

        	cur_frm.set_value('shipping_line', sinv.shipping_line);
            cur_frm.refresh_field('shipping_line');
     }
   });
 }*/