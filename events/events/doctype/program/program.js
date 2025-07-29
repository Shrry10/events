// Copyright (c) 2025, Shreyas Parida and contributors
// For license information, please see license.txt

frappe.ui.form.on("Program", {
	refresh(frm) {
        frappe.call("frappe.geo.country_info.get_country_timezone_info").then(({ message }) => {
            frm.fields_dict.time_zone.set_data(message.all_timezones);
        });
	},
});
