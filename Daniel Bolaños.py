import random

def simular_monty_hall_con_hits(num_simulaciones):
    hits_cambiar = 0  # Contador de aciertos cambiando de puerta
    hits_no_cambiar = 0  # Contador de aciertos sin cambiar de puerta
    
    for _ in range(num_simulaciones):
        # Asignar el premio a una puerta aleatoria
        premio = random.randint(0, 2)
        
        # El jugador elige una puerta al azar
        eleccion_jugador = random.randint(0, 2)
        
        # El anfitrión abre una puerta que no tiene el premio ni es la elección del jugador
        puertas = [0, 1, 2]
        puertas.remove(eleccion_jugador)
        
        if premio in puertas:
            puertas.remove(premio)
        puerta_abierta = random.choice(puertas)  # El anfitrión abre una puerta sin premio
        
        # Caso 1: El jugador decide NO cambiar de puerta
        if eleccion_jugador == premio:
            hits_no_cambiar += 1  # Acierto si el jugador no cambia de puerta
        
        # Caso 2: El jugador decide cambiar de puerta
        puertas_restantes = [0, 1, 2]
        puertas_restantes.remove(eleccion_jugador)
        puertas_restantes.remove(puerta_abierta)
        eleccion_jugador_cambiada = puertas_restantes[0]  # El jugador cambia a la puerta restante
        
        if eleccion_jugador_cambiada == premio:
            hits_cambiar += 1  # Acierto si el jugador cambia de puerta

    # Retornar los aciertos y las probabilidades
    return hits_no_cambiar, hits_cambiar, hits_no_cambiar / num_simulaciones, hits_cambiar / num_simulaciones

# Parámetros
num_simulaciones = 10000

# Ejecutar la simulación
hits_no_cambiar, hits_cambiar, prob_no_cambiar, prob_cambiar = simular_monty_hall_con_hits(num_simulaciones)

# Mostrar resultados
print(f"Aciertos sin cambiar de puerta: {hits_no_cambiar} de {num_simulaciones} (Probabilidad: {prob_no_cambiar:.3f})")
print(f"Aciertos cambiando de puerta: {hits_cambiar} de {num_simulaciones} (Probabilidad: {prob_cambiar:.3f})")

