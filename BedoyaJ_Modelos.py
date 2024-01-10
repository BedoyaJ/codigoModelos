import math

#   MODELOS DE PÉRDIDA DE TRAYECTORIA
#      -- PROPAGACIÓN DE ONDAS --

#   NOMBRE: JEANCARLO BEDOYA


cont = 0
exp_pathL = 0


while cont == 0:
    print("\n\n\n------------------------------------------------------")
    print("Elija el tipo de modelo de propagación:")
    print("(1) Modelo en Espacio Libre")
    print("(2) Modelo Okumura Hata")
    print("(3) Extensión PSC del Modelo Hata\n")

    model_per = int(input("Seleccione el modelo: "))
    print("\n ")
        
    if model_per == 1:  #PÉRDIDA DE TRAYECTORIA DE ESPACIO LIBRE
        print("======= Modelo en Espacio Libre =======\n")

        freq = int(input("Ingrese la frecuencia: "))
        dist = int(input("Ingrese la distancia: "))

        print("\nEspacio Libre                      (2)")
        print("Radio celular de área urbana       (2.7 a 3.5)")
        print("Radio celular en sombra            (3 a 5)")
        print("En construcción de línea de visión (1.6 a 1.8)")
        print("Obstruido en el edificio           (4 a 6)")
        print("Obstruido en las fábricas          (2 a 3)")

        while exp_pathL == 0:

            exp_pathL = float(input("\nIngrese el exponente de Path Loss: "))

            if exp_pathL > 6 or exp_pathL < 1.6:
                print ("\n<<<<<<<<< Exponente Incorrecto >>>>>>>>>\n")
                exp_pathL = 0
            
                

        
        L_dB = 20 * math.log10(freq) + 10 * exp_pathL *math.log10(dist) - 147.56
        print("\n******************************************************")
        print("La pérdida de trayectoria es: ", round(L_dB, 2), "dB")
        print("******************************************************")
        exp_pathL = 0


    #--------------------------------------------------------------------------
    elif model_per == 2:    #PÉRDIDA DE TRAYECTORIA OKUMURA HATA
        print("========= Modelo Okumura Hata =========\n")
        fc = int(input("Frecuencia de la portadora   (fc): "))
        d = int(input("Distancia de propagación      (d): "))
        h_t = int(input("Altura antena de transmisión (ht): "))
        h_r = int(input("Altura antena de receptora   (hr): "))

        print("\n(1) Pequeña o mediana ciudad")
        print("(2) Gran Ciudad")
        print("(3) Área suburbana")
        print("(4) Áreas abierta o rurales")

        entorno = int(input("\nSeleccione el entorno: "))

        if entorno == 1:
            A_hr = (1.1 * math.log10(fc) - 0.7) * h_r - (1.56 * math.log10(fc)-0.8)

            L_dB = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(h_t) - A_hr + (44.9 - 6.55 * math.log10(h_t)) * math.log10(d)

            print("\n******************************************************\n")
            print("El factor de corrección A(hr) es: ", round(A_hr, 2), "dB")
            print("La pérdida de trayectoria en P/M ciudad es: ", round(L_dB, 2), "dB")
            print("******************************************************")

        elif entorno == 2:
            if fc <= 300:
                A_hr = 8.29 * (math.log10(1.54 * h_r))**2 - 1.1
            else:
                A_hr = 3.2 * (math.log10(11.75 * h_r))**2 - 4.97

            L_dB = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(h_t) - A_hr + (44.9 - 6.55 * math.log10(h_t)) * math.log10(d)

            print("\n******************************************************")
            print("El factor de corrección A(hr) es: ", round(A_hr, 2), "dB")
            print("La pérdida de trayectoria en Gran ciudad es: ", round(L_dB, 2), "dB")
            print("******************************************************")

        elif entorno == 3:
            A_hr = (1.1 * math.log10(fc) - 0.7) * h_r - (1.56 * math.log10(fc)-0.8)

            L_dB = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(h_t) - A_hr + (44.9 - 6.55 * math.log10(h_t)) * math.log10(d)

            L_dB_suburban = L_dB - 2 * (math.log10(fc/28))**2 - 5.4

            print("\n******************************************************")
            print("El factor de corrección A(hr) es: ", round(A_hr, 2), "dB")
            print("La pérdida de trayectoria en Suburbano es: ", round(L_dB_suburban, 2), "dB")
            print("******************************************************")

        elif entorno == 4:
            A_hr = (1.1 * math.log10(fc) - 0.7) * h_r - (1.56 * math.log10(fc)-0.8)

            L_dB = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(h_t) - A_hr + (44.9 - 6.55 * math.log10(h_t)) * math.log10(d)

            L_dB_open = L_dB - 4.78 * (math.log10(fc))**2 - 18.733 * math.log10(fc) - 40.98

            print("\n******************************************************")
            print("El factor de corrección A(hr) es: ", round(A_hr, 2), "dB")
            print("La pérdida de trayectoria en Abierto/Rural es: ", round(L_dB_open, 2), "dB")
            print("******************************************************")

        else:
            print("\n<<<<<<<<< Entorno Inexistente >>>>>>>>>\n\n")
            




    #--------------------------------------------------------------------------
    elif model_per == 3:    #Extensión PSC del Modelo Hata
        print("==== Extensión PSC del Modelo Hata ====\n")
        fc = int(input("Frecuencia de 1500 a 2000 Mhz (fc): "))  #Frecuencias de 1500 a 2000 Mhz
        d = int(input("Distancia de propagación       (d): "))
        h_t = int(input("Altura antena de transmisión  (ht): "))
        h_r = int(input("Altura antena de receptora    (hr): "))

        print("\n(1) Ciudad mediana/Centros suburbanos (Suburban)")
        print("(2) Centros metropolitanos (Urban)")

        entorno = int(input("\nSeleccione el entorno: "))

        if entorno == 1:
            C_M = 0     #Factor de Corrección
            A_hr = (1.1 * math.log10(fc) - 0.7) * h_r - (1.56 * math.log10(fc)-0.8)

            L_dB_suburban = 46.3 + 33.9 * math.log10(fc) - 13.82 * math.log10(h_t) - A_hr + (44.9 - 6.55 * math.log10(h_t)) * math.log10(d) + C_M

            print("\n******************************************************")
            print("El factor de corrección A(hr) es: ", round(A_hr, 2), "dB")
            print("La pérdida de trayectoria en Suburbano es: ", round(L_dB_suburban, 2), "dB")
            print("******************************************************")

        else:
            C_M = 3     #Factor de Corrección
            A_hr = 3.2 * (math.log10(11.75 * h_r))**2 - 4.97

            L_dB_urban = 46.3 + 33.9 * math.log10(fc) - 13.82 * math.log10(h_t) - A_hr + (44.9 - 6.55 * math.log10(h_t)) * math.log10(d) + C_M

            print("\n******************************************************")
            print("El factor de corrección A(hr) es: ", round(A_hr, 2), "dB")
            print("La pérdida de trayectoria en Urbano es: ", round(L_dB_urban, 2), "dB")
            print("******************************************************")

    else:
        print("\n<<<<<<<<< Modelo Inexistente >>>>>>>>>\n\n")
        
        
        