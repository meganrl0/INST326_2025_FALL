def inventory():
       """Initializes the inventory and active items bar.
       displays inventory, 
       Returns: inventory (inv), active (active)
       """
       inv = [None, None, None, None, None,
           None, None, None, None, None,
           None, None, None, None, None,
           None, None, None, None, None,
           None, None, None, None, None]
       active = [None, None, None, None, None]
       return  active, inv
print(inventory())