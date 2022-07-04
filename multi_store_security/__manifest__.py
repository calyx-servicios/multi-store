# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Multi Store Security",
    "summary": """
        This module modifies all multi-store
        access rules 
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["ParadisoCristian"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.1.0.0",
    "depends": [
        "stock_multi_store_users",
        "purchase_multi_store",
        "sale_multi_store",
    ],
    'data': [
        'security/account_invoice_inter_company_currency_security.xml',
    ],
}
