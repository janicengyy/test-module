from openerp.osv import fields, osv

class purchase_order(osv.osv):
    
    def _get_order_num(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('purchase.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.name
        return result.keys()
    def _get_order_origin(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('purchase.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.origin
        return result.keys()
    def _get_order_date(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('purchase.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.date_order
        return result.keys()
    def _get_order_curr(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('purchase.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.currency_id
        return result.keys()
    def _get_order_curr_rate(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('purchase.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.currency_id.rate
        return result.keys()
    def base_amt(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.browse(cr, uid, ids,context):
            res[record.id] = record.price_subtotal * record.rate
        return res
    def multi_unicost_qty(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.browse(cr, uid, ids,context):
            res[record.id] = record.uni_cost * record.product_qty
        return res
    
    
    
    _inherit = 'purchase.order.line'
    _columns = {
                'order_name': fields.related('order_id', 'name',type='char', string=u'Doc NO.'),
                'origin': fields.related('order_id', 'origin',type='char', string=u'Source Doc'),
                'date_order': fields.related('order_id','date_order',type='date',string=u'Order Date'),
                'currency_id': fields.related('order_id','currency_id',relation='res.currency', type='many2one',string=u'Currency'),
                'rate': fields.related('order_id','currency_id','rate',type='float',relation='res.currency',string=u'Currency Rate'),
                'base_amt':fields.function(base_amt, type='float', string=u'Base Amt'),
                'uni_cost':fields.related('product_id','standard_price',relation='product.template',type='float',string=u'Cost'),
                'cost_amt':fields.function(multi_unicost_qty, type='float',string=u'Total Cost'),
                
              
                }
purchase_order()