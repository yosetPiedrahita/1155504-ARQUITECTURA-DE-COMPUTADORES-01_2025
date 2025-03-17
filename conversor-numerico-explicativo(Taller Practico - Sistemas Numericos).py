"""
Programa de Conversión Numérica Explicativo
Permite conversiones entre sistemas numéricos (decimal, binario, octal, hexadecimal)
y operaciones aritméticas en diferentes bases, mostrando el paso a paso del proceso.
"""

class ConversorNumerico:
    """Clase para realizar conversiones numéricas y operaciones aritméticas en diferentes sistemas."""
    
    def __init__(self):
        """Inicializa el conversor con los sistemas numéricos soportados y sus bases."""
        self.sistemas = {
            'decimal': 10,
            'binario': 2,
            'octal': 8,
            'hexadecimal': 16
        }
    
    def convertir(self, numero, desde_sistema, hacia_sistema, mostrar_pasos=False):
        """
        Convierte un número desde un sistema numérico hacia otro.
        
        Args:
            numero (str): El número a convertir
            desde_sistema (str): Sistema de origen ('decimal', 'binario', 'octal', 'hexadecimal')
            hacia_sistema (str): Sistema destino ('decimal', 'binario', 'octal', 'hexadecimal')
            mostrar_pasos (bool): Si es True, muestra el paso a paso de la conversión
            
        Returns:
            str: El número convertido al sistema destino o mensaje de error
        """
        # Validar sistemas
        if desde_sistema not in self.sistemas:
            return f"Error: Sistema de origen '{desde_sistema}' no válido."
        
        if hacia_sistema not in self.sistemas:
            return f"Error: Sistema destino '{hacia_sistema}' no válido."
        
        # Si los sistemas son iguales, no hay necesidad de convertir
        if desde_sistema == hacia_sistema:
            if mostrar_pasos:
                print(f"El número ya está en sistema {desde_sistema}. No se requiere conversión.")
            return numero
        
        try:
            # Convertir a decimal primero (paso intermedio)
            if desde_sistema == 'decimal':
                valor_decimal = int(numero)
                if mostrar_pasos:
                    print(f"\nPaso 1: El número {numero} ya está en sistema decimal.")
            else:
                valor_decimal = int(numero, self.sistemas[desde_sistema])
                if mostrar_pasos:
                    print(f"\nPaso 1: Convertir {numero}({desde_sistema}) a decimal:")
                    self._explicar_conversion_a_decimal(numero, desde_sistema)
                    print(f"Resultado en decimal: {valor_decimal}")
            
            # Convertir desde decimal al sistema destino
            if hacia_sistema == 'decimal':
                resultado = str(valor_decimal)
                if mostrar_pasos:
                    print(f"\nPaso 2: El número ya está en sistema decimal: {resultado}")
            else:
                if mostrar_pasos:
                    print(f"\nPaso 2: Convertir {valor_decimal}(decimal) a {hacia_sistema}:")
                    self._explicar_conversion_desde_decimal(valor_decimal, hacia_sistema)
                
                if hacia_sistema == 'binario':
                    resultado = bin(valor_decimal)[2:]  # Eliminar prefijo '0b'
                elif hacia_sistema == 'octal':
                    resultado = oct(valor_decimal)[2:]  # Eliminar prefijo '0o'
                elif hacia_sistema == 'hexadecimal':
                    resultado = hex(valor_decimal)[2:].upper()  # Eliminar prefijo '0x'
                
                if mostrar_pasos:
                    print(f"Resultado en {hacia_sistema}: {resultado}")
            
            return resultado
        except ValueError:
            return f"Error: '{numero}' no es un número válido en sistema {desde_sistema}."
    
    def _explicar_conversion_a_decimal(self, numero, desde_sistema):
        """
        Explica el proceso de conversión de un número a decimal.
        
        Args:
            numero (str): El número a convertir
            desde_sistema (str): Sistema de origen
        """
        base = self.sistemas[desde_sistema]
        digitos = numero.upper()  # Para manejar letras en hexadecimal
        
        print(f"Para convertir {numero}({desde_sistema}) a decimal:")
        print(f"Base del sistema {desde_sistema}: {base}")
        
        total = 0
        for i, digito in enumerate(reversed(digitos)):
            valor_digito = int(digito, base) if digito.isdigit() else (ord(digito) - ord('A') + 10)
            valor_posicional = valor_digito * (base ** i)
            total += valor_posicional
            print(f"Posición {i}: {digito} × {base}^{i} = {digito} × {base**i} = {valor_posicional}")
        
        print(f"Suma total: {total}")
    
    def _explicar_conversion_desde_decimal(self, decimal, hacia_sistema):
        """
        Explica el proceso de conversión desde decimal a otro sistema.
        
        Args:
            decimal (int): El número decimal a convertir
            hacia_sistema (str): Sistema destino
        """
        base = self.sistemas[hacia_sistema]
        
        print(f"Para convertir {decimal}(decimal) a {hacia_sistema}:")
        print(f"Base del sistema {hacia_sistema}: {base}")
        print("Método de división sucesiva:")
        
        numero = decimal
        restos = []
        
        while numero > 0:
            resto = numero % base
            
            # Convertir resto a representación en el sistema destino
            if resto < 10:
                resto_representacion = str(resto)
            else:
                resto_representacion = chr(resto - 10 + ord('A'))
            
            print(f"{numero} ÷ {base} = {numero // base} con resto {resto} {'(' + resto_representacion + ')' if resto > 9 else ''}")
            
            restos.append(resto_representacion)
            numero //= base
        
        resultado = ''.join(reversed(restos))
        
        print(f"Los restos en orden inverso dan: {resultado}")

    def _validar_operacion(self, num1, num2, sistema):
        """
        Método auxiliar para validar los parámetros de una operación aritmética.
        
        Args:
            num1 (str): Primer número
            num2 (str): Segundo número
            sistema (str): Sistema numérico
            
        Returns:
            tuple: (es_valido, mensaje_error) o (es_valido, (val1, val2)) si es válido
        """
        if sistema not in self.sistemas:
            return False, f"Sistema '{sistema}' no válido. Use: decimal, binario, octal o hexadecimal."
        
        try:
            val1 = int(num1, self.sistemas[sistema])
            val2 = int(num2, self.sistemas[sistema])
            return True, (val1, val2)
        except ValueError:
            return False, f"Error: Los números proporcionados no son válidos en sistema {sistema}."
    
    def suma(self, num1, num2, sistema, mostrar_pasos=False):
        """
        Suma dos números en el sistema especificado.
        
        Args:
            num1 (str): Primer número
            num2 (str): Segundo número
            sistema (str): Sistema numérico
            mostrar_pasos (bool): Si es True, muestra el paso a paso de la operación
            
        Returns:
            str: Resultado de la suma en el sistema especificado o mensaje de error
        """
        valido, resultado = self._validar_operacion(num1, num2, sistema)
        if not valido:
            return resultado
        
        val1, val2 = resultado
        suma = val1 + val2
        
        if mostrar_pasos:
            print(f"\nOperación de suma en sistema {sistema}:")
            print(f"1. Convertir operandos a decimal (si es necesario):")
            if sistema != 'decimal':
                print(f"   {num1}({sistema}) = {val1}(decimal)")
                print(f"   {num2}({sistema}) = {val2}(decimal)")
            else:
                print(f"   Los números ya están en decimal: {val1} y {val2}")
            
            print(f"\n2. Realizar la suma en decimal:")
            print(f"   {val1} + {val2} = {suma}")
            
            print(f"\n3. Convertir el resultado a sistema {sistema}:")
            if sistema != 'decimal':
                self._explicar_conversion_desde_decimal(suma, sistema)
            else:
                print(f"   El resultado ya está en decimal: {suma}")
        
        return self.convertir(str(suma), 'decimal', sistema)
    
    def resta(self, num1, num2, sistema, mostrar_pasos=False):
        """
        Resta dos números en el sistema especificado.
        
        Args:
            num1 (str): Primer número (minuendo)
            num2 (str): Segundo número (sustraendo)
            sistema (str): Sistema numérico
            mostrar_pasos (bool): Si es True, muestra el paso a paso de la operación
            
        Returns:
            str: Resultado de la resta en el sistema especificado o mensaje de error
        """
        valido, resultado = self._validar_operacion(num1, num2, sistema)
        if not valido:
            return resultado
        
        val1, val2 = resultado
        
        if val1 < val2:
            return "Error: El resultado sería negativo. El programa maneja solo números positivos."
        
        resta = val1 - val2
        
        if mostrar_pasos:
            print(f"\nOperación de resta en sistema {sistema}:")
            print(f"1. Convertir operandos a decimal (si es necesario):")
            if sistema != 'decimal':
                print(f"   {num1}({sistema}) = {val1}(decimal)")
                print(f"   {num2}({sistema}) = {val2}(decimal)")
            else:
                print(f"   Los números ya están en decimal: {val1} y {val2}")
            
            print(f"\n2. Realizar la resta en decimal:")
            print(f"   {val1} - {val2} = {resta}")
            
            print(f"\n3. Convertir el resultado a sistema {sistema}:")
            if sistema != 'decimal':
                self._explicar_conversion_desde_decimal(resta, sistema)
            else:
                print(f"   El resultado ya está en decimal: {resta}")
        
        return self.convertir(str(resta), 'decimal', sistema)
    
    def multiplicacion(self, num1, num2, sistema, mostrar_pasos=False):
        """
        Multiplica dos números en el sistema especificado.
        
        Args:
            num1 (str): Primer número
            num2 (str): Segundo número
            sistema (str): Sistema numérico
            mostrar_pasos (bool): Si es True, muestra el paso a paso de la operación
            
        Returns:
            str: Resultado de la multiplicación en el sistema especificado o mensaje de error
        """
        valido, resultado = self._validar_operacion(num1, num2, sistema)
        if not valido:
            return resultado
        
        val1, val2 = resultado
        multiplicacion = val1 * val2
        
        if mostrar_pasos:
            print(f"\nOperación de multiplicación en sistema {sistema}:")
            print(f"1. Convertir operandos a decimal (si es necesario):")
            if sistema != 'decimal':
                print(f"   {num1}({sistema}) = {val1}(decimal)")
                print(f"   {num2}({sistema}) = {val2}(decimal)")
            else:
                print(f"   Los números ya están en decimal: {val1} y {val2}")
            
            print(f"\n2. Realizar la multiplicación en decimal:")
            print(f"   {val1} × {val2} = {multiplicacion}")
            
            print(f"\n3. Convertir el resultado a sistema {sistema}:")
            if sistema != 'decimal':
                self._explicar_conversion_desde_decimal(multiplicacion, sistema)
            else:
                print(f"   El resultado ya está en decimal: {multiplicacion}")
        
        return self.convertir(str(multiplicacion), 'decimal', sistema)
    
    def division(self, num1, num2, sistema, mostrar_pasos=False):
        """
        Divide dos números en el sistema especificado.
        
        Args:
            num1 (str): Dividendo
            num2 (str): Divisor
            sistema (str): Sistema numérico
            mostrar_pasos (bool): Si es True, muestra el paso a paso de la operación
            
        Returns:
            str: Resultado de la división en el sistema especificado (parte entera) o mensaje de error
        """
        valido, resultado = self._validar_operacion(num1, num2, sistema)
        if not valido:
            return resultado
        
        val1, val2 = resultado
        
        if val2 == 0:
            return "Error: División por cero."
        
        division = val1 // val2  # División entera
        
        if mostrar_pasos:
            print(f"\nOperación de división en sistema {sistema}:")
            print(f"1. Convertir operandos a decimal (si es necesario):")
            if sistema != 'decimal':
                print(f"   {num1}({sistema}) = {val1}(decimal)")
                print(f"   {num2}({sistema}) = {val2}(decimal)")
            else:
                print(f"   Los números ya están en decimal: {val1} y {val2}")
            
            print(f"\n2. Realizar la división en decimal (parte entera):")
            print(f"   {val1} ÷ {val2} = {division}")
            
            print(f"\n3. Convertir el resultado a sistema {sistema}:")
            if sistema != 'decimal':
                self._explicar_conversion_desde_decimal(division, sistema)
            else:
                print(f"   El resultado ya está en decimal: {division}")
        
        return self.convertir(str(division), 'decimal', sistema)


def mostrar_menu():
    """Función para mostrar menú principal del programa."""
    print("\n===== CONVERSOR NUMÉRICO EXPLICATIVO =====")
    print("1. Convertir entre sistemas numéricos")
    print("2. Suma en diferentes sistemas")
    print("3. Resta en diferentes sistemas")
    print("4. Multiplicación en diferentes sistemas")
    print("5. División en diferentes sistemas")
    print("6. Salir")
    return input("\nSeleccione una opción (1-6): ")


def seleccionar_sistema(mensaje="Seleccione sistema"):
    """
    Función auxiliar para seleccionar un sistema numérico.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        str: Nombre del sistema seleccionado o None si la selección es inválida
    """
    sistemas = ['decimal', 'binario', 'octal', 'hexadecimal']
    
    print("\nSistemas disponibles:")
    for i, sistema in enumerate(sistemas, 1):
        print(f"{i}. {sistema}")
    
    try:
        opcion = int(input(f"{mensaje} (1-4): "))
        if 1 <= opcion <= 4:
            return sistemas[opcion - 1]
        else:
            print("Opción no válida. Intente nuevamente.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        return None


def main():
    """Función principal del programa."""
    conversor = ConversorNumerico()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            # Conversión entre sistemas
            desde_sistema = seleccionar_sistema("Seleccione sistema de origen")
            if desde_sistema is None:
                continue
                
            hacia_sistema = seleccionar_sistema("Seleccione sistema de destino")
            if hacia_sistema is None:
                continue
                
            numero = input(f"\nIngrese número en sistema {desde_sistema}: ")
            mostrar_pasos = input("¿Mostrar paso a paso? (s/n): ").lower() == 's'
            
            resultado = conversor.convertir(numero, desde_sistema, hacia_sistema, mostrar_pasos)
            print(f"\nResultado: {numero}({desde_sistema}) = {resultado}({hacia_sistema})")
            
        elif opcion == '2':
            # Suma
            sistema = seleccionar_sistema("Seleccione sistema para la operación")
            if sistema is None:
                continue
                
            num1 = input(f"\nIngrese primer número en sistema {sistema}: ")
            num2 = input(f"Ingrese segundo número en sistema {sistema}: ")
            mostrar_pasos = input("¿Mostrar paso a paso? (s/n): ").lower() == 's'
            
            resultado = conversor.suma(num1, num2, sistema, mostrar_pasos)
            print(f"\nResultado: {num1} + {num2} = {resultado} (en sistema {sistema})")
            
        elif opcion == '3':
            # Resta
            sistema = seleccionar_sistema("Seleccione sistema para la operación")
            if sistema is None:
                continue
                
            num1 = input(f"\nIngrese minuendo en sistema {sistema}: ")
            num2 = input(f"Ingrese sustraendo en sistema {sistema}: ")
            mostrar_pasos = input("¿Mostrar paso a paso? (s/n): ").lower() == 's'
            
            resultado = conversor.resta(num1, num2, sistema, mostrar_pasos)
            print(f"\nResultado: {num1} - {num2} = {resultado} (en sistema {sistema})")
            
        elif opcion == '4':
            # Multiplicación
            sistema = seleccionar_sistema("Seleccione sistema para la operación")
            if sistema is None:
                continue
                
            num1 = input(f"\nIngrese primer factor en sistema {sistema}: ")
            num2 = input(f"Ingrese segundo factor en sistema {sistema}: ")
            mostrar_pasos = input("¿Mostrar paso a paso? (s/n): ").lower() == 's'
            
            resultado = conversor.multiplicacion(num1, num2, sistema, mostrar_pasos)
            print(f"\nResultado: {num1} × {num2} = {resultado} (en sistema {sistema})")
            
        elif opcion == '5':
            # División
            sistema = seleccionar_sistema("Seleccione sistema para la operación")
            if sistema is None:
                continue
                
            num1 = input(f"\nIngrese dividendo en sistema {sistema}: ")
            num2 = input(f"Ingrese divisor en sistema {sistema}: ")
            mostrar_pasos = input("¿Mostrar paso a paso? (s/n): ").lower() == 's'
            
            resultado = conversor.division(num1, num2, sistema, mostrar_pasos)
            print(f"\nResultado: {num1} ÷ {num2} = {resultado} (en sistema {sistema})")
            
        elif opcion == '6':
            # Salir
            print("\n¡Gracias por usar el Conversor Numérico Explicativo!")
            break
            
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida (1-6).")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()