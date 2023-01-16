frappe.listview_settings['Ticket'] = {
	colwidths: {"subject": 6},
	add_fields: ['status'],
	onload: function(listview) {
		frappe.route_options = {
			"status": "Open"
		};

		var method = "atlantis.atlantis.doctype.ticket.ticket.set_multiple_status";

		listview.page.add_action_item(__("Set as Open"), function() {
			listview.call_for_selected_items(method, {"status": "Open"});
		});
	},
	get_indicator: function (doc) {
        if(doc.status === "Open"){
            return [__("Open"), "orange", "status,=,Open"];
        }
        else if(doc.status === "In Follow Up"){
            return [__("In Follow Up"), "red", "status,=,In Follow Up"];
        }
        else if(doc.status === "Resolved"){
            return [__("Resolved"), "green", "status,=,Resolved"];
        }
    }
}
