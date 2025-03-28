"""Este módulo contiene la implementación de una calculadora RMC."""

class CalculadoraMCM:
    """Clase que implementa una calculadora básica para operaciones RMC."""
    def __init__(self):
        pass

    def calcular_mcd(self, a, b):
        """Calcula el Máximo Común Divisor (MCD) usando el algoritmo de Euclides."""
        while b:
            a, b = b, a % b
        return a

    def calcular_mcm(self, a, b):
        """Calcula el Mínimo Común Múltiplo (MCM) utilizando el MCD."""
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Ambos valores deben ser enteros.")
        if a <= 0 or b <= 0:
            raise ValueError("Ambos valores deben ser enteros positivos.")
        return abs(a * b) // self.calcular_mcd(a, b)

if __name__ == "__main__":
    calculadora = CalculadoraMCM()

    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        resultado = calculadora.calcular_mcm(num1, num2)
        print(f"El Mínimo Común Múltiplo de {num1} y {num2} es: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")

    # Prueba simple
    assert calculadora.calcular_mcm(12, 18) == 36, "Error en el cálculo del MCM."
