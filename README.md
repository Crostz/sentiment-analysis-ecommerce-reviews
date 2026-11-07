# ¿Qué opina el cliente? Clasificación de sentimiento en reseñas de productos de Amazon

## Fuente de datos

**1. Amazon Reviews for Sentiment Analysis** (`amazon.csv`)
Autor: [Adam Bittlingmayer], disponible en [Kaggle](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews/data). Licencia: [Unknown].

Los datasets no se incluyen en este repositorio; descárgalos desde los links anteriores.
Este proyecto es de carácter educativo/portafolio y no comercial.

## Pregunta de negocio
¿Se puede clasificar automáticamente una reseña como positiva o negativa para medir la satisfacción de los clientes sin leer cada comentario?

## Resultados
Se compararon tres clasificadores sobre 180,000 reseñas para el entrenamiento y 20,000 para la prueba.

| Modelo | Accuracy | F1 macro |
|---|---|---|
| **Regresión logística** | **0.92** | **0.92** |

## Hallazgos
1. La regresión logística fue el mejor modelo (92% de accuracy, F1 macro de 0.92) y es el que se guardó para su uso.

## Consideraciones durante la preparación de datos
1. En `amazon.csv` casi todas las reseñas son positivas (1,110 positivas, 348 neutras y 6 negativas), por lo que se combinó con un segundo dataset para tener ejemplos negativos.
2. Las etiquetas de `amazon.csv` se construyeron a partir del rating; las del segundo dataset ya venían con polaridad binaria. Ambas fuentes tienen criterios de etiquetado distintos.
3. Se eliminaron las filas con rating no numérico.
4. Distribución final de clases: Positivo 52.9%, Negativo 44.0%, Neutro 3.0%.

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
