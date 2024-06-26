import frappe
from frappe import _

@frappe.whitelist()
def read_doctype():
    name = frappe.local.form_dict.get('name')
    doc = frappe.get_doc("information", name)
    return doc.as_dict()

@frappe.whitelist()
def create_doctype():
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    if not doctype:
        return {"error": "doctype is required"}, 400
    try:
        doc = frappe.get_doc({
            "doctype": doctype,
            **data
        })
        doc.insert()
        frappe.db.commit()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500
    
@frappe.whitelist()
def delete_doctype():
    doctype = frappe.local.form_dict.get('doctype')
    docname = frappe.local.form_dict.get('name')
    frappe.delete_doc(doctype,docname)
    frappe.db.commit()
    return f"{docname} deleted successfully"

@frappe.whitelist()
def update_doctype():
    data = frappe.local.form_dict
    doc = frappe.get_doc(data.doctype,data.name)
    doc.update(data)
    doc.save()
    frappe.db.commit()
    return doc


