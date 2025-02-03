import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product, OrderItem
from .forms import OrderForm

def order_form(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # 1) Create the Order
            order = form.save()

            # 2) Parse selected products from hidden input
            selected_products_json = request.POST.get('selected_products', '')
            if selected_products_json:
                try:
                    selected_products = json.loads(selected_products_json)
                    # 3) Create OrderItems
                    for sp in selected_products:
                        product_id = sp.get('id')
                        quantity = sp.get('quantity', 1)
                        if product_id and quantity:
                            # Make sure product exists
                            try:
                                product_obj = Product.objects.get(id=product_id)
                            except Product.DoesNotExist:
                                continue  # skip if not found
                            OrderItem.objects.create(
                                order=order,
                                product=product_obj,
                                quantity=quantity
                            )
                except json.JSONDecodeError:
                    pass  # or handle error

            return redirect('order_success')
        else:
            # If form invalid, re-render
            products = Product.objects.all()
            return render(request, 'orders/order_form.html', {
                'form': form,
                'products': products
            })
    else:
        form = OrderForm()
        products = Product.objects.all()
        return render(request, 'orders/order_form.html', {
            'form': form,
            'products': products
        })

def order_success(request):
    return render(request, 'orders/order_success.html')

def get_products(request):
    """ API endpoint to fetch products for AJAX selection """
    products = list(Product.objects.filter(is_active=True)
                               .values('id', 'name', 'price', 'category'))
    return JsonResponse({'products': products})
