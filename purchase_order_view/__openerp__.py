{
    "name" : "Purchase Order View",
    "version" : "1.0",
    "category" : "Generic Modules Control",
    'depends' : ['account','base','base_setup','product','sale','sale_order_dates'],
    'description': """
Functions:
==================================================
* Add menu items under Purchases to show more details of Purchase Orders in list view.
    """,
    
    "data" : ["purchase_order_tree.xml"],
    "installable": True,
    "active": True
}
