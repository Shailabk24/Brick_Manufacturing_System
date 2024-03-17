import csv
class Brick:
    def __init__(self, type, dimensions, weight, color, strength_rating, quantity, cost_per_unit):
        self.type = type
        self.dimensions = dimensions
        self.weight = weight
        self.color = color
        self.strength_rating = strength_rating
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit

    def calculate_total_weight(self):
        return self.weight * self.quantity

    def calculate_total_cost(self):
        return self.cost_per_unit * self.quantity


class RawMaterial:
    def __init__(self, type, supplier, unit, quantity, cost_per_unit):
        self.type = type
        self.supplier = supplier
        self.unit = unit
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit

    def calculate_total_cost(self):
        return self.cost_per_unit * self.quantity


class InventoryLocation:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.current_stock = []

    def add_stock(self, brick, quantity):
        if self.capacity - sum(b.quantity for b in self.current_stock) >= quantity:
            self.current_stock.append(brick)
            brick.quantity += quantity
        else:
            print(f"Insufficient capacity at {self.location}")

    def remove_stock(self, brick, quantity):
        if quantity <= brick.quantity:
            brick.quantity -= quantity
            if brick.quantity == 0:
                self.current_stock.remove(brick)
        else:
            print(f"Insufficient stock of {brick.type} at {self.location}")

# Create brick objects
brick1 = Brick("Standard", (20, 8, 5), 2, "Red", 1500, 150, 25)
brick2 = Brick("Paving", (20, 20, 5), 3.0, "Gray", 2000, 50, 30)

# Create raw material objects
clay = RawMaterial("Clay", "Supplier A", "Tons", 10, 20)
sand = RawMaterial("Sand", "Supplier B", "Tons", 5, 15)

# Create inventory location objects
warehouse = InventoryLocation("Warehouse", 1000)
drying_area = InventoryLocation("Drying Area", 500)

# Add stock to warehouse
warehouse.add_stock(brick1, 50)
warehouse.add_stock(brick2, 25)

weight_brick1 = brick1.calculate_total_weight()

print(weight_brick1)