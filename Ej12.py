Algoritmo abrir_cuenta_con_descubierto_autorizado:
# Inicializar una cuenta mediante un saldo_inicial' y un # descubierto_MAX' durante una `duración_max'.

Entrada:
saldo_inicial : REAL
descubierto_MAX : REAL
duracion_max : FECHA

Precondición:
saldo_inicial > 0
descubierto_MAX ≥ 0
duracion_max ≥ 0

Realización:
Si saldo_inicial <= 0 o descubierto_MAX < 0 o duracion_max <= 0 entonces
Mostrar mensaje de error y detener el algoritmo
Sino
# Crear una nueva cuenta con los valores iniciales
c <- NUEVA CUENTA
c.saldo <- saldo_inicial
c.descubierto_maximo <- descubierto_MAX
c.fecha_descubierto <- 0
c.duracion_maxima_descubierto <- duracion_max


Postcondición:
La cuenta "c" ha sido inicializada con los siguientes valores:
- c.saldo = saldo_inicial
- c.descubierto_maximo = descubierto_MAX
- c.fecha_descubierto = 0
- c.duracion_maxima_descubierto = duracion_max

Fin de abrir_cuenta_con_descubierto_autorizado