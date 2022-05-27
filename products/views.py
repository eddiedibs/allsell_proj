from django.shortcuts import render, get_object_or_404
from products.models import ProductModel
from django.views.generic import DetailView, ListView, TemplateView, FormView
from django.views.generic.base import View
from cart.forms import AddToCartForm, AddressForm


class ProdDetailView(FormView):
    model = ProductModel
    template_name = 'product.html'
    context_object_name = 'products'

    form_class = AddToCartForm

    def get_object(self):
        return get_object_or_404(ProductModel, slug=self.kwargs["slug"])

    def get_success_url(self):
        return reverse("cart:summary")

    def get_form_kwargs(self):
        kwargs = super(ProdDetailView, self).get_form_kwargs()
        kwargs["product_id"] = self.get_object().id
        return kwargs

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        product = self.get_object()

        item_filter = order.items.filter(
            product=product,
            colour=form.cleaned_data['colour'],
            size=form.cleaned_data['size'],
        )

        if item_filter.exists():
            item = item_filter.first()
            item.quantity += int(form.cleaned_data['quantity'])
            item.save()

        else:
            new_item = form.save(commit=False)
            new_item.product = product
            new_item.order = order
            new_item.save()

        return super(ProdDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProdDetailView, self).get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context




class ProdSellView(TemplateView):
    template_name = 'choosewhattosell.html'


