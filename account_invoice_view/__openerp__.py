{
    "name" : "Account Invoices View",
    "version" : "1.0",
    "category" : "Generic Modules Control",
    'depends' : ['account','base','base_setup','product','sale','sale_order_dates'],
    'description': """
Functions:
==================================================
* Display more details of Customer and Supplier Invoices with adding column items in list view.

    """,
    
    "data" : ["account_invoice_view.xml"],
    "installable": True,
    "active": True
}
