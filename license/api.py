import frappe
from frappe import _

def fl_si_on_submit(self, method):
	export_entry = frappe.get_doc("Advance Authorisation License", self.finbyz_license)
	export_entry.append("exports", {
		"sales_invoice" : self.name,
		"shipping_bill_no" : self.shipping_bill_no,
		"sb_date" : self.posting_date,
		"quantity" : self.quantity,    
		"fob_value" : self.fob_value,  
	})

	export_entry.save(ignore_permissions = True)
	frappe.db.commit()

def fl_si_on_cancel(self, method):
	export_entry = frappe.db.get_value("Export Against AAL", 
		filters={"parent":self.finbyz_license,
				"sales_invoice":self.name}, fieldname="name")
	if export_entry:
		export_entry = frappe.get_doc("Export Against AAL", export_entry)
		export_entry.delete()
		frappe.db.commit()

# def fl_pi_on_submit(self, method):
# 	export_entry = frappe.new_doc("Import Against AAL", )
# 	export_entry.parent = self.finbyz_license
# 	export_entry.save(ignore_permissions = True)
# 	frappe.db.commit()

# def fl_pi_on_submit(self, method):
# 	export_entry = frappe.new_doc("Import Against AAL", )
# 	export_entry.parent = self.finbyz_license
# 	export_entry.save(ignore_permissions = True)
# 	frappe.db.commit()