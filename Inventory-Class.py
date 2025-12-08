class inventory:
    """Instantiates an object of the inventory class."""
    player_inv = [None, None, None, None, None,
           None, None, None, None, None,
           None, None, None, None, None,
           None, None, None, None, None,
           None, None, None, None, None]
    player_active = [None, None, None, None, None]
    def __init__(self, inv, active):
        self.inv = inv
        self.active = active
    def add_item(self, item):
        """adds item to the inventory.
        Args: item (str) the stackable item.
        Side Effects, changes a None value in the inventory to item."""
        for i in self.active:
            if self.active[i] != None:
                i += 1
            else:
                self.active[i] = item
        if i == 4:
            i = 0
            for i in self.inv:
                if self.inv[i] != None:
                    i += 1
                else:
                    self.inv[i] = item
    def subtract_item(self, item):
        """Subtracts item to the inventory.
        Args: item (str) the stackable item.
        Returns item (str)
        Side Effects, changes a item value in the inventory to None."""
        for i in self.active:
            if self.active[i] == None:
                i += 1
            else:
                self.active[i] = item
        if i == 4:
            i = 0
            for i in self.inv:
                if self.inv[i] == None:
                    i += 1
                else:
                    ret = self.inv[i]
                    self.inv[i] = None
                    return ret
    def stack_item(self, item, n):
        """Takes duplicate items and stacks the together.
        Args: item (str) the stackable item, n (int) the amount of copies of the
        item are being stacked on to the original.
        Side Effects, increases the number of duplicate items in a stack
        represented by ("item name", xn)"""
        for i in self.active and self.inv:
            if self.active[i] == item:
                self.active[i] = item + " x" + n
            elif self.inv[i] == item:
                self.inv[i] = item + " x" + n
                
class item:
    """creates an object of the item class."""
    def __init__(self, name, description, actions, stackable=False):
        """Instantiates an item object.
        Attributes: name(str) the name of the object, description (str) a
        description of the item, its function and its lore, actions (list)
        of things that the item can be used for and the effects of such actions,
        stackable(bool) whether or not multiple copies of the item can occupy
        one inventory slot with the default value being False."""
        self.name = name
        self.description = description
        self.actions = actions
        self.stackable = stackable
    def use_item(self, action):
        """Accesses item's actions attributes to enact a use of that item.
        Args: action(list) a action that the item can be used for and its
        effects (example: consumables like healing potions can be consumed to
        restore health which deleats that instance of the item from the
        inventory).
        Returns: the effect(s) of that item's action."""
        if action in self.actions:
            return action[1]
