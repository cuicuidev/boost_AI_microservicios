# Despliegue de modelos de IA en la nube

### Teoría
---
- Explicar las dos perspectivas en la arquitectura de software: monolitos y microservicios.
    - Ventajas y desventajas de los monolitos.
    - Cómo los microservicios solucionan los problemas de los monolitos.
    - Retos que traen los microservicios.
- Aprovechar la explicación para dar un tour por AWS.
    - Enseñar cómo registrarse.
    - Enseñar cómo navegar por la consola.
    - Hablar sobre algunos de los servicios más clave y aprovecharlos para ejemplificar lo que se aprendió en la sección anterior.
- Hablar por encima de Docker.
    - Qué es la contenedorización?
    - Cómo instalamos Docker?

---
### Descanso
---

### Práctica
---
- Crear entorno virtual e instalar FastAPI, Uvicorn, Scikit Learn (versión ligera) y Mangum
- Contenedorizar.
    - Explicar el Dockerfile
    - Comandos build y run
- Escribir código
    - Explicar FastAPI
        - Decoradores
        - Rutas
        - async
    - Explicar Pydantic
        - Tipado
        - Validación
        - OOP
    - Integrar modelo en la API
        - Modelos Pydantic para estructuras de datos de entrada y salida
        - Integración de model.predict() en un endpoint
- Desplegar a Lambda y a EC2 (O solo a una, depende del tiempo)
- Usar la API desde una app de Streamlit