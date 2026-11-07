# ¿Qué opina el cliente? Clasificación de sentimiento en reseñas de productos de Amazon

## Fuente de datos

**1. Amazon Reviews for Sentiment Analysis** 
Autor: [Adam Bittlingmayer], disponible en [Kaggle](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews/data). Licencia: [Unknown].

Los datasets no se incluyen en este repositorio; descárgalos desde los links anteriores.
Este proyecto es de carácter educativo/portafolio y no comercial.

## Pregunta de negocio
¿Se puede clasificar automáticamente una reseña como positiva o negativa para medir la satisfacción de los clientes sin leer cada comentario?

## Resultados
Se elaboró un modelo sobre 200,000 reseñas, 180,000 para el entrenamiento y 20,000 para la prueba.

| Modelo | Accuracy | F1 macro |
|---|---|---|
| **Regresión logística** | **0.92** | **0.92** |

## Hallazgos
1. La regresión logística fue el mejor modelo (92% de accuracy, F1 macro de 0.92) y es el que se guardó para su uso.

## Consideraciones durante la preparación de datos
1. Las clases, positiva y negativa, se encuentran balanceadas, y la diferencia en volumen es mínima.
2. No solo el contenido de las reseñas aporta al modelo, también se debe considerar el título de la reseña.
3. Artefactos en el texto como las mayúsculas enriquecen el análisis de sentimientos, por lo que el preprocesamiento no debe ser muy intrusivo.

## Definiciones
* Positivo: rating >= 4.0
* Negativo: rating <= 3.0
* F1 macro: promedio del F1 de las tres clases sin ponderar por tamaño, para que la clase neutra pese igual que las demás

## Limitaciones
* Las reseñas deben estar en inglés.

## Estructura del repositorio
* `notebooks/`: análisis exploratorio de las reseñas
* `modelos/`: entrenamiento y comparación de modelos
* `pagina/`: aplicación web en Django que usa el modelo guardado

## Herramientas utilizadas
Python, pandas, scikit-learn, spaCy, matplotlib, seaborn, Django

## Autoría
* Alessandro Elías Hesse Pulache
* Mauricio Andrés Canchis Fernández
