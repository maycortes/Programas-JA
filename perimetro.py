class Recatangulo:
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    def perimetro(self):
        perimetro=(self.alto*2)+(self.ancho*2)
        return perimetro
r1=Recatangulo(4,2)
perimetro=r1.perimetro()
print("El perimetro es:",perimetro)

