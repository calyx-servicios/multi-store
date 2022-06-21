from odoo import models, api
from odoo.models import BaseModel

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        user = self.env.user
        # if superadmin, do not apply
        if not self.env.is_superuser():
            args += ['|', 
                ('store_id', '=', False), 
                ('store_id', 'child_of', user.store_ids.ids)
            ]
        return BaseModel._search(self, args, offset, limit, order, count=count, access_rights_uid=access_rights_uid)
