def convertir_temperatura(grad_cent):
    # Convertir a Fahrenheit
    fahrenheit = (9 / 5) * grad_cent + 32

    # Convertir a Kelvin
    kelvin =  273.15 + grad_cent

    return fahrenheit, kelvin


centigrados=int(input("Ingrese grados centigrados="))

result_far, result_kelvin = convertir_temperatura(centigrados)

print(centigrados, "grados centigrados es igual a", result_far, "grados Fahrenheit")
print("kelvin", result_kelvin)
