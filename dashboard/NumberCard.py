import frappe

@frappe.whitelist()
def Total_Sales_Order():
    return frappe.db.count('Sales Order',{'docstatus':1})

@frappe.whitelist()
def salesGreaterThanVal():
    query = """
        SELECT COUNT(DISTINCT PARENT)
        FROM `tabSales Order Item`
        WHERE amount > 100
    """

    count = frappe.db.sql(query,as_dict=False)[0][0]

    return count