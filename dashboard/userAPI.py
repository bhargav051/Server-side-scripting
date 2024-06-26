import frappe
from frappe import _

@frappe.whitelist()
def getUser():
    data = frappe.get_all('User', fields=['*'])
    return data

@frappe.whitelist()
def createUser():
    data = frappe.local.form_dict
    try:
        doc = frappe.get_doc({
            "doctype": 'User',
            **data
        })
        doc.insert()
        frappe.db.commit()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500