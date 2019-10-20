from django.conf.urls import url
from .views import catalog,cart,removefromcart,checkout,completeOrder,adminLogin,adminDashboard

urlpatterns = [
    # Examples:
    # url(r'^$', 'simple_store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',catalog, name='catalog'),
    url(r'^cart/$',cart, name='cart'),
    url(r'^cart/remove/$',removefromcart, name='remove'),
    url(r'^cart/checkout/$',checkout, name='checkout'),
    url(r'^cart/checkout/complete/$',completeOrder, name='complete_order'),
    url(r'^admin-login/$',adminLogin, name='admin_login'),
    url(r'^admin-panel/$',adminDashboard, name='admin'),


]
