console.log("chale chhe pan")
frappe.ui.form.on("Issue", {
	refresh: function(frm) {
        if(frm.doc.__islocal){
            frm.set_value('agent_name' , frappe.session.user)
        }   
    },
    validate:function(frm){
         let phoneno = frm.doc.caller_contact_number
         
    }
});

