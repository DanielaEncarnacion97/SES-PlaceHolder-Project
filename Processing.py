from scraper import get_walmart, get_target
class Item:
    def __init__(self, name, cost, supplier):
        self.name = name
        self.cost = cost
        self.supplier = supplier
        self.isCheaper = None
    def setIsCheaper(self, isCheaper):
        self.isCheaper = isCheaper
    def getName(self):
        return self.name
    def getCost(self):
        return self.cost
    def getSupplier(self):
        return self.supplier
    def getIsCheaper(self):
        return self.isCheaper

def find_min_relevant(options, item, supplier):
    for (name,cost) in options:
        if item in name:
            return Item(name, cost, supplier)
    return Item("Error: no relevant items", double., supplier)

def is_target_cheaper(result, target_item, walmart_item)
    target_item.setIsCheaper(result)
    walmart_item.setIsCheaper(not(result))

og_item_list = []
target_item_list = []
walmart_item_list = []
for item in og_item_list:
    walmart_options = get_walmart(item, "Walmart")
    target_options = get_target(item, "Target")
    walmart_item = find_min_relevant(walmart_options, item)
    target_item = find_min_relevant(target_options, item)
    if walmart_item.getCost() > target_item.getCost():
        is_target_cheaper(True, target_item, walmart_item)
    else:
        is_target_cheaper(False, target_item, walmart_item)
    target_item_list.append(target_item)
    walmart_item_list.append(walmart_item)