#API handler for request to get items.

from api import items_api

import json
import pybase


class GetItems(pybase.PyBase):
  """Hnadler to fetch the items on the given request."""
  item_labels_ = ['name', 'brand_name', 'price', 'is_discounted','discount', 'discounted_price', 'description']

  def get(self):
    """Overrided function of base class to handle get request."""
    selected_item = []
    is_discounted = self.request.get('is_discounted')
    category = self.request.get('category')
    subcategory = self.request.get('subcategory')
    print is_discounted
    items_obj = items_api.ItemsApi()
    items = items_obj.getItems(category, subcategory, is_discounted)
    for item in items:
      selected_item.append(self.formatQueryResult(item))

    response = {
        'items': selected_item,
        'status': 'success'
        }
    self.response.out.write(json.dumps(response))

  def formatQueryResult(self, item_obj):
    """Formate the query object according to the given label."""
    item = {}
    item[self.item_labels_[0]] = item_obj.name
    item[self.item_labels_[1]] = item_obj.brand_name
    item[self.item_labels_[2]] = item_obj.price
    item[self.item_labels_[3]] = item_obj.has_discount
    item[self.item_labels_[4]] = item_obj.discount
    item[self.item_labels_[5]] = item_obj.discounted_price
    item[self.item_labels_[6]] = item_obj.description
    return item
