from django.test import TestCase
from django.urls import reverse


class ItemSelectionTests(TestCase):
    fixtures = ["initial_data.json"]

    def test_select_items_updates_weight(self):
        response = self.client.post(reverse("zaino:item_list"), {"items": [1, 2]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["selected_items"]), 2)
        self.assertAlmostEqual(response.context["total_weight"], 2.5 + 0.4)
        self.assertContains(response, 'class="item selected"', count=2)
