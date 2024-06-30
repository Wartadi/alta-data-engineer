class OngkosKirim:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
    
    def calculate_cost(self):
        volume = self.length * self.width * self.height
        base_cost = 5000
        
        if volume > 50 or self.weight > 1:
            return base_cost + ((volume // 50) + (self.weight - 1)) * base_cost
        return base_cost

def main():
    length = 5
    width = 2
    height = 4
    weight = 1
    
    calculator = OngkosKirim(length, width, height, weight)
    cost = calculator.calculate_cost()
    
    print("====== Medium 2 ======")
    print("Harga:", f"Rp {cost}")

main()
