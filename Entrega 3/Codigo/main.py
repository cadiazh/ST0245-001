import pandas as pd
import gmplot
from Adicional import adicional
import time
import webbrowser

apikey = 'AIzaSyAEoJwf7WtJ_3zlUMAu5RSVpRtr5UE32gQ'
adicional.bienvenida()

temp = 0
df = pd.read_csv('C:\Programacion_Visual\Datos.py\calles_de_medellin_con_acoso.csv', sep=';')
inicial = '(-75.5778046, 6.2029412)'
final = '(-75.5762232, 6.266327)'
gmap3 = gmplot.GoogleMapPlotter(float(inicial[inicial.find(",") + 2:len(inicial) - 1]),
                                float(inicial[1:inicial.find(",")]), 14, apikey=apikey)
gmap3.text(float(inicial[inicial.find(",") + 2:len(inicial) - 1]), float(inicial[1:inicial.find(",")]), 'Punto Partida')

t1 = time.time()
for i in range(0, 3):
    grafo = adicional.crear_Grafo(df, i)
    temp = adicional.dijkstra(grafo, inicial, final)
    latitude_list = []
    longitude_list = []

    for j in range(len(temp)):
        valores = str(temp[j])
        longitude_list.append(float(valores[1:valores.find(",")]))
        latitude_list.append(float(valores[valores.find(",") + 2:len(valores) - 1]))
    gmap3.scatter(latitude_list, longitude_list, size=0, marker=False)

    if i == 0:
        gmap3.plot(latitude_list, longitude_list, '#000000', edge_width=15)  # Negro
    if i == 1:
        gmap3.plot(latitude_list, longitude_list, '#1900ff', edge_width=7)  # azul
    if i == 2:
        gmap3.plot(latitude_list, longitude_list, '#ff0000', edge_width=7)  # rojo

gmap3.text(latitude_list[len(latitude_list) - 1], longitude_list[len(longitude_list) - 1], 'Punto de llegada')
print((time.time() - t1) / 60)

gmap3.draw(
    "C:\Programacion_Visual\Datos.py\mapaConPuntos.html")  # en este punto se genera el html en la posición que se indique
webbrowser.open_new_tab('C:\Programacion_Visual\Datos.py\mapaConPuntos.html')
