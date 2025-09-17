###############################
# Fecha: 16/09/2025
# Descripción: Este codigo realiza el análisis de 
#     14 variables estadisticas por medio de funciones
####

# Fecha: 16/09/2025
# Análisis estadístico básico de una lista

import statistics as stats
from collections import Counter


datos = [40, 52, 98, 72, 34, 23, 55, 34, 25, 28]
datos = [15, 28, 35, 42, 55, 63, 28, 74, 81, 55, 39, 20]
datos = [10, 22, 34, 45, 56, 67, 78, 89, 43, 32, 21, 56, 45, 67, 34, 10]
datos = [90, 85, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 20, 35, 50, 65]




# Medidas
media = stats.mean(datos)
mediana = stats.median(datos)
modas = stats.multimode(datos)            # lista
desv_std = stats.stdev(datos)             # muestral
desv_pop = stats.pstdev(datos)            # poblacional (opcional)
geom = stats.geometric_mean(datos)
harm = stats.harmonic_mean(datos)

# Rango e IQR
rango = max(datos) - min(datos)
q1, q2, q3 = stats.quantiles(datos, n=4, method="exclusive")
iqr = q3 - q1
siqr = iqr / 2  # "desviación cuartílica" (semi-interquartílica)

# Frecuencia de la(s) moda(s)
conteo = Counter(datos)
freq_moda = max(conteo.values())
modas_str = ", ".join(str(m) for m in modas)

# Coeficiente de variación (muestral): stdev / mean
cv = (desv_std / media) * 100 if media != 0 else float("nan")

print(f"Datos de análisis:             {datos}")

# Salida
print("          Calcular           |    Valor    |  Análisis")
print("-" * 58)
print(f"1. Nombre de la variable:     {'inventar':>12}")
print(f"2. Fuentes:                    {'inventar':>12}")
print(f"3. Tabla de datos:                ...")
print(f"4. Media aritmética            {media:10.3f}")
# La moda puede ser múltiple, por eso no usamos : .3f
print(f"5. Moda                        {modas_str:>10}   (freq={freq_moda})")
print(f"6. Mediana                     {mediana:10.3f}")
print(f"7. Media geométrica            {geom:10.3f}")
print(f"8. Media armónica              {harm:10.3f}")
print(f"9. Rango                       {rango:10.3f}")

# print(f"10. Cuartiles (Q1, Q2, Q3)     ({q1:.3f}, {q2:.3f}, {q3:.3f})")
# print(f"11. IQR (Q3 - Q1)              {iqr:10.3f}")
print(f"10. Desv. cuartílica           {siqr:10.3f}","*puede variar dependiendo de cómo se calculen los cuartiles")
print(f"11. Desv. estándar (muestral)  {desv_std:10.3f}")
print(f"12. Coef. de variación (%)     {cv:10.3f}")
print(f"13. Suma de datos              {sum(datos):10.3f}")
print(f"14. Número de datos            {len(datos):10d}")

