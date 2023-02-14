Algoritmo: Calcular Remuneración de Horas Extra

Entrada:
  salario_mensual_bruto : REAL # Importe del salario mensual bruto
  horas_extra : ENTERO # Cantidad de horas extra del mes a remunerar

Precondición:
  salario_mensual_bruto > 0
  horas_extra ≥ 0

Constantes:
  CANTIDAD_HORAS_MAX_1 : ENTERO ← 8 # Umbral de cambio de precio de remuneración
  PRECIO_1 : REAL ← 1,25 # Precio de remuneración de CANTIDAD_HORAS_MAX_1 primeras horas extra
  PRECIO_2 : REAL ← 1,50 # Precio de remuneración de las otras horas extra

Variables:
  precio_hora : REAL # Precio hora de la remuneración bruta de base
  horas_extra_1 : ENTERO # Cantidad de horas extra con PRECIO_1 %
  horas_extra_2 : ENTERO # Cantidad de horas extra con PRECIO_2 %
  remuneracion_extra : REAL # Importe total de la remuneración de las horas extra

Realización:
  precio_hora ← precio_hora_bruto(salario_mensual_bruto) # Cálculo del precio hora de la remuneración bruta de base
  horas_extra_1 ← min(horas_extra, CANTIDAD_HORAS_MAX_1) # Cálculo de la cantidad de horas con PRECIO_1 %
  horas_extra_2 ← max(horas_extra - CANTIDAD_HORAS_MAX_1, 0) # Cálculo de la cantidad de horas con PRECIO_2 %
  remuneracion_extra ← precio_hora x (horas_extra_1 x PRECIO_1 + horas_extra_2 x PRECIO_2) # Cálculo de la remuneración de las horas extra

Salida:
  remuneracion_extra # Importe total de la remuneración de las horas extra

Postcondición:
  remuneracion_extra ≥ 0 # La remuneración extra no puede ser negativa