from django import template
register=template.Library()
@register.filter(name='cart_quantity')
def cart_quantity(detail,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==detail.id:
            return cart.get(id)
    return 0

