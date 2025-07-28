from django.shortcuts import render
from .models import Item


def item_list(request):
    items = Item.objects.select_related('category').all()
    selected_ids = request.POST.getlist('items') if request.method == 'POST' else []
    selected_items = Item.objects.filter(id__in=selected_ids)
    total_weight = sum(item.weight for item in selected_items)
    context = {
        'items': items,
        'selected_items': selected_items,
        'total_weight': total_weight,
    }
    return render(request, 'zaino/item_list.html', context)
