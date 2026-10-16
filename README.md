# ¿Qué opina el cliente? Clasificación de sentimiento en reseñas de productos de Amazon

## Fuente de datos

**1. Amazon Sales Dataset** (`amazon.csv`)
Autor: [completar], disponible en [Kaggle]([link]). Licencia: [confirmar en la ficha de Kaggle].

**2. Reseñas de Amazon con polaridad** (`train_lite.csv`, 10,000 reseñas)
Fuente: [completar con el dataset original y su link]. Licencia: [confirmar].

Los datasets no se incluyen en este repositorio; descárgalos desde los links anteriores.
Este proyecto es de carácter educativo/portafolio y no comercial.

## Pregunta de negocio
¿Se puede clasificar automáticamente una reseña como positiva, neutra o negativa para medir la satisfacción de los clientes sin leer cada comentario?

## Resultados
Se compararon tres clasificadores sobre ~11,500 reseñas (80% entrenamiento, 20% prueba: 2,293 reseñas).

| Modelo | Accuracy | F1 macro |
|---|---|---|
| Naive Bayes | 0.73 | 0.59 |
| Random Forest (max_depth=20) | 0.78 | 0.55 |
| **Regresión logística** | **0.82** | **0.71** |

![matriz de confusión](matriz_confusion.png)

## Hallazgos
1. La regresión logística fue el mejor modelo (82% de accuracy, F1 macro de 0.71) y es el que se guardó para su uso.
2. La clase "Neutro" es la más difícil de predecir (F1 de 0.47 en el mejor modelo): solo representa el 3% de las reseñas.
3. El accuracy puede engañar: el Random Forest tiene mejor accuracy que Naive Bayes, pero detecta apenas el 4% de las reseñas neutras. Por eso se comparó también con F1 macro.
4. Un modelo basado en diccionarios (TextBlob) no se entrena y no se evaluó contra las etiquetas reales; se usó solo de forma exploratoria.

## Consideraciones durante la preparación de datos
1. En `amazon.csv` casi todas las reseñas son positivas (1,110 positivas, 348 neutras y 6 negativas), por lo que se combinó con un segundo dataset para tener ejemplos negativos.
2. Las etiquetas de `amazon.csv` se construyeron a partir del rating; las del segundo dataset ya venían con polaridad binaria. Ambas fuentes tienen criterios de etiquetado distintos.
3. Se eliminaron las filas con rating no numérico.
4. Distribución final de clases: Positivo 52.9%, Negativo 44.0%, Neutro 3.0%.

## Definiciones
* Positivo: rating ≥ 4.0
* Neutro: rating ≥ 3.0 y < 4.0
* Negativo: rating < 3.0
* F1 macro: promedio del F1 de las tres clases sin ponderar por tamaño, para que la clase neutra pese igual que las demás

## Limitaciones
* La clase neutra tiene pocos ejemplos, por lo que su predicción es poco confiable.
* Las reseñas deben estar en inglés.
* [Si aplica: el caso de uso con laptops es demostrativo; falta evaluarlo con reseñas no vistas durante el entrenamiento.]

## Estructura del repositorio
* `01_exploracion/`: análisis exploratorio de las reseñas
* `02_modelos/`: entrenamiento y comparación de modelos
* `03_caso_de_uso/`: aplicación del modelo a productos
* `app/`: aplicación web en Django que usa el modelo guardado

## Herramientas utilizadas
Python, pandas, scikit-learn, spaCy, TextBlob, matplotlib, seaborn, Django

## Autoría
Modelo y análisis: [tu nombre]. Aplicación web (Django): [quién la desarrolló; si no fue tuya, dilo aquí].

## Participantes

* Alessandro Elías Hesse Pulache
* Mauricio Andrés Canchis Fernández
