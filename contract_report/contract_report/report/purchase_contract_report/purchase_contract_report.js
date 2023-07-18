// Copyright (c) 2023, Tech Ventures and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Purchase Contract Report"] = {
	"filters": [
		{
			"fieldname":"job_no",
			"label": __("Job No"),
			"fieldtype": "Link",
			"options": "Master Towel Costing",
			"reqd": 1
			},
	]
};
