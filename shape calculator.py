class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        lines = [self.width * '*' for i in range(self.height)]
        return '\n'.join(lines) + '\n'
    
    def get_amount_inside(self, second):
        return int(self.get_area() / second.get_area())
    
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def __repr__(self):
        return f"Square(side={self.width})"
        
    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)  
        

if __name__ == "__main__":
    rect = Rectangle(3, 6)
    sq = Square(5)
    
    sq.set_side(2)
    print(sq.get_picture())
    