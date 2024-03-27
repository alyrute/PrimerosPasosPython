
try:
    print(10/0)

except TypeError as e:

    print("Error en el sistema - TYPO"  ,  e)

except ZeroDivisionError as ex:
    print("Error en "  ,  ex)
finally:
    print("Proceso terminado")


        