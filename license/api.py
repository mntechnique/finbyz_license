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


def fl_si_validate(self, method):
	sales_order =  frappe.get_all('Sales Order', filters={'Customer': self.customer }, fields=['name'])

	if not sales_order:
		frappe.throw(_("Set Customer for Sales Order"))

def fl_pi_on_submit(self, method):
	import_entry = frappe.get_doc("Advance Authorisation License", self.finbyz_license)
	import_entry.append("imports", {
		"purchase_invoice" : self.name,
		"shipping_bill_no" : self.shipping_bill_no,
		"sb_date" : self.posting_date,
		"quantity" : self.quantity,
		"cif_value" : self.cif_value,
	})

	import_entry.save(ignore_permissions = True)
	frappe.db.commit()

def fl_pi_on_cancel(self, method):
	import_entry = frappe.db.get_value("Import Against AAL",
		filters={"parent":self.finbyz_license,
				"purchase_invoice":self.name}, fieldname="name")
	if import_entry:
		import_entry = frappe.get_doc("Import Against AAL", import_entry)
		import_entry.delete()
		frappe.db.commit()


def fl_pi_validate(self, method):
	purchsae_order=  frappe.get_all('Purchase Order', filters={'Supplier': self.supplier }, fields=['name'])

	if not purchsae_order:
		frappe.throw(_("Set Supplier for Purcahse Order"))
