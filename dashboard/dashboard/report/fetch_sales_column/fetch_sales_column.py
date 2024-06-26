import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data

def get_columns():
    return [
        _("Customer Name") + ":Data: 150",
        _("Sales Order Name") + ":Link/Sales Order: 250",
        _("Delivery Date") + ":Date: 200",
        _("Item Code") + ":Link/Item: 200",
        _("Item Name") + ":Data: 150",
        _("Item Qty") + ":Float: 100"
    ]

def get_data(filters):
    data = []

    sales_orders = frappe.db.sql("""
        SELECT
            so.customer_name,
            so.name as sales_order_name,
            soi.delivery_date,
            soi.item_code,
            soi.item_name,
            soi.qty
        FROM
            `tabSales Order` so
        JOIN
            `tabSales Order Item` soi ON so.name = soi.parent
     
        ORDER BY
            so.name ASC
    """, as_dict=1)

    for so in sales_orders:
        data.append([
            so.customer_name,
            so.sales_order_name,
            so.delivery_date,
            so.item_code,
            so.item_name,
            so.qty
        ])

    return data