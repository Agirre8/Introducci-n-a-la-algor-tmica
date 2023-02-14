Entrada:
#Coste sin IVA
c_sin_iva: REAL
#Porcentaje de impuesto sobre la venta
porcentaje_iva: REAL

Resultado:
#Precio final con IVA incluido
precio_con_iva: REAL

Precondición:
c_sin_iva ≥ 0
0 < porcentaje_iva < 1

Realización:
precio_con_iva <-- c_sin_iva + (c_sin_iva x porcentaje_iva)

Poscondición:
precio_con_iva = c_sin_iva + (c_sin_iva x porcentaje_iva)

Fin del cálculo

Algoritmo: Interés generado

Entrada:
#Capital inicial
capital_inicial: REAL
#Tiempo en años
tiempo_en_anos: REAL
#Tasa de interés anual
tasa_interes_anual: REAL

Resultado:
#Interés generado
interes_generado: REAL

Precondición:
capital_inicial ≥ 0
tiempo_en_anos > 0
tasa_interes_anual > 0

Realización:
interes_generado <-- capital_inicial x tiempo_en_anos x tasa_interes_anual

Poscondición:
interes_generado = capital_inicial x tiempo_en_anos x tasa_interes_anual