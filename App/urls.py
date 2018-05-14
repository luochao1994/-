from django.conf.urls import url

from App import views

urlpatterns =[
    url(r'^home/',views.home,name='home'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^regist',views.regist,name='regist'),
    url(r'^login/',views.login,name='login'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^mine/',views.mine,name='mine'),
    url(r'^market/',views.Market,name='market'),
    url(r'^markets/(\d+)/(\d+)/(\d+)/',views.user_market_params,name='markets'),
# 添加购物车
    url(r'^addgoods/', views.add_goods, name='addgoods'),
    url(r'^subgoods/', views.sub_goods, name='subgoods'),
    # 购物车
    url(r'^cart/', views.user_cart, name='cart'),
    # 修改购物车商品的选择
    url(r'^changeCartSelect/', views.user_change_select, name='change_select'),
    #下单
    url(r'^ordered/',views.ordered,name='ordered'),
    #付款
    url(r'^payOrder/(\d+)/',views.payOrder,name='payOrder'),
    #确认付款
    url(r'^payOrdered/(\d+)/',views.payOrdered,name='payOrdered'),
    #待付款
    url (r'orderWaitPay', views.order_wait_pay, name='ordr_Wait_pay'),
    #待收货
    url (r'^orderpayed/', views.order_wait_shouhuo, name='order_wait_shouhuo'),

]
