from openerp.osv import fields, osv
from openerp.tools.translate import _
import pdb


class purchase_order(osv.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'
    _columns = {
        'mrp_id': fields.many2one('mrp.production', 'Hull Number'),
        'po_type': fields.selection([('hull', 'Hull'), ('facility', 'Facility'), ('other', 'Other')], 'Type'),
        }

purchase_order()

# class purchase_request(osv.Model):
# 	_name = 'purchase.request'
# 	_columns = {
# 		'name': fields.many2one('purcase.request', 'Request No.'),
#         'type': fields.selection([('hull', 'Hull'), ('facility', 'Facility'), ('other', 'Other')], 'Type', required=True),
#         'mrp_id': fields.many2one('mrp.production', 'Hull Number'),
#         'state':fields.selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('waiting_approval', 'Waiting for Approval'), ('approved', 'Approved'),('done', 'Done'),('reject', 'Rejected')], 'State', readonly=True, track_visibility='onchange'),
#         'requestor_id': fields.many2one('res.users', 'Requestor'),
#         'date': fields.date('Date'),
#         'note': fields.text('Note'),
#         'request_line': fields.one2many('purchase.request.line', 'request_id', 'Request Line')
# 	}

# 	 _defaults = {
#         'state': 'draft',
#         'date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
#         'requestor_id': lambda self, cr, uid, context: uid,
#         'name':"/",
#     }

# 	def request_confirm(self, cr, uid, ids, context=None):
#         for request in self.browse(cr, uid, ids, context=context):
#             if not request.product_lines:
#                 raise osv.except_osv(_('Warning!'),_('You cannot confirm an indent %s which has no line.' % (indent.name)))
#             res = {
#                'name':self.pool.get('ir.sequence').get(cr, uid, 'purchase.request'),
#                'state': 'waiting_approval'
#             }
#             self.write(cr, uid, [request.id], res, context=context)

#             # Add all authorities of the indent as followers
#             followers = []
#             if request.requestor_id and request.requestor_id.partner_id and request.requestor_id.partner_id.id:
#                 followers.append(request.requestor_id.partner_id.id)
            
#             for follower in followers:
#                 self.write(cr, uid, [request.id], {'message_follower_ids': [(4, follower)]}, context=context)

#         return True

#     def request_reject(self, cr, uid, ids, context=None):
#         self.write(cr, uid, [ids], {'state': 'reject'})

#         return True

#     def request_approve(self, cr, uid, ids, context=None):
#         self.write(cr, uid, [ids], {'state': 'approved'})
        
#         return True

#      def _create_po(self, cr, uid, ids, context=None):
#         for request in self.browse(cr, uid, ids, context=None):
#         	for line in request.request_line:
        		
#         	res = {	'type': request.type,
#         			'mrp_id': request.mrp_id

#         			}
#         return True

# 	def unlink(self, cr, uid, ids, context=None):
# 	    for request in self.browse(cr, uid, ids):
# 	        if request.state != 'draft':
# 	            raise osv.except_osv(_('Invalid Action!'), _('You cannot delete this indent'))
# 	    return super(purchase_request, self).unlink(cr, uid, ids, context=context)

# purchase_request()

# class purchase_request_line(osv.Model):
# 	_name = 'purchase.request.line'
# 	_columns = {
# 		'request_id': fields.many2one('purchase.request', ondelete='cascade', required=True),
# 		'product_id': fields.many2one('product.product', 'Product', required=True),
# 		'qty': fields.float('Qty', digits_compute= dp.get_precision('Product UoS'), required=True),
# 		'supplier_id': fields.many2one('res.partner', domain=['supplier': True]),
# 		'po_id': fields.many2one('purchase.order', 'PO Reference')
# 	}
	
# purchase_request()