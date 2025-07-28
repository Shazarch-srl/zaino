from django.shortcuts import render
from .models import Category, Item


def item_list(request):
    categories = Category.objects.prefetch_related('items__brand').all()
    selected_ids = request.POST.getlist('items') if request.method == 'POST' else []
    selected_items = Item.objects.filter(id__in=selected_ids).select_related('brand', 'category')
    total_weight = sum(item.weight for item in selected_items)
    context = {
        'categories': categories,
        'selected_items': selected_items,
        'total_weight': total_weight,
    }
    return render(request, 'zaino/item_list.html', context)
