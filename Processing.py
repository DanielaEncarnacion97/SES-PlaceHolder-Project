from scraper import get_walmart, get_target
def items_processor(og_item_list):
    class Item:
        def __init__(self, name, cost, supplier):
            self.name = name
            self.cost = cost
            self.supplier = supplier
            self.isCheaper = None
        def setIsCheaper(self, isCheaper):
            self.isCheaper = isCheaper
        def getCost(self):
            return self.cost
        def __dict__(self):
            return {"name": self.name, "cost": self.cost, "supplier": self.supplier, "isCheaper": self.isCheaper}

    def find_min_relevant(options, item, supplier):
        for (name,cost) in options:
            if item in name:
                return Item(name, cost, supplier)
        return Item("Error: no relevant items", sys.float_info.max, supplier)

    def is_target_cheaper(result, target_item, walmart_item)
        target_item.setIsCheaper(result)
        walmart_item.setIsCheaper(not(result))

    item_list = []
    for item in og_item_list:
        walmart_options = get_walmart(item)
        target_options = get_target(item)
        walmart_item = find_min_relevant(walmart_options, item)
        target_item = find_min_relevant(target_options, item)
        if walmart_item.getCost() > target_item.getCost():
            is_target_cheaper(True, target_item, walmart_item)
        else:
            is_target_cheaper(False, target_item, walmart_item)
        item_list.append(target_item.__dict__)
        item_list.append(walmart_item.__dict__)

     return item_list
