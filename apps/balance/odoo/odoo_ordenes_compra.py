import xmlrpc.client

url = "https://odoo.bluepacificoils.com/"
db = "bpo.production"
username = "UAdmin"
password = "12345"

#****************************Balanza****************************

def get_entidad_origen_y_material(orden_compra):
    """
    Parametro: orden de compra
    Obtiene: entidad origen y material
    """
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    entidades_materiales = models.execute_kw(
        db, uid, password,
        'purchase.order', 'search_read',
        [[
            ('name', '=', orden_compra )
        ]],
        {'fields': [
            'name',
            'partner_id',
            'company_id',
            'product_id'
        ]}
    )

    return entidades_materiales