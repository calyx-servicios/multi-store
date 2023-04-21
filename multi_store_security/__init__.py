import logging
from odoo import api, SUPERUSER_ID

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    modified_rules = {
        "account_multi_store.account_journal_store_rule": "['|',('store_id','=',False),('store_id','child_of',[user.store_id.id])]",
        "account_multi_store.account_move_store_rule": "['|',('journal_id.store_id','=',False),('journal_id.store_id','child_of',[user.store_id.id])]",
        "account_multi_store.account_payment_store_rule": "['|',('journal_id.store_id','=',False),('journal_id.store_id','child_of',[user.store_id.id])]",
        "base_multi_store.res_store_rule": "[('id','in',user.store_ids.ids)]",
        "base_multi_store.res_store_rule_manager": "[(1,'=',1)]",
        "base_multi_store.multi_company_store_rule": "['|',('company_id','=',False),('company_id', 'in', company_ids)]",
        "purchase_multi_store.purchase_order_store_rule": "['|',('picking_type_id.store_id','=',False),('picking_type_id.store_id','child_of',[user.store_id.id])]",
        "sale_multi_store.sale_order_store_rule": "['|',('warehouse_id.store_id','=',False),('warehouse_id.store_id','child_of',[user.store_id.id])]",
        "stock_multi_store.stock_warehouse_store_rule": "['|',('store_id','=',False),('store_id','child_of',[user.store_id.id])]",
        "stock_multi_store.stock_picking_type_store_rule": "['|',('warehouse_id.store_id','=',False),('warehouse_id.store_id','child_of',[user.store_id.id])]",
        "stock_multi_store.stock_picking_store_rule": "['|',('picking_type_id.warehouse_id.store_id','=',False),('picking_type_id.warehouse_id.store_id','child_of',[user.store_id.id])]",
    }
    for rule,value in modified_rules.items():
        try:
            rule = env.ref(rule,raise_if_not_found=True)
            rule.domain_force = value
        except:
            logging.warning("rule %s not found, skipping...")