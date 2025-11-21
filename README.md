## Qué aprendí
Aprendí el flujo de trabajo completo de un proyecto de Machine Learning básico: Comprendí que las computadoras no leen texto como nosotros, por lo que es necesario convertir las palabras en números (vectores) utilizando herramientas como CountVectorizer. Aprendí a conectar un modelo lógico matemático (el script de detección) con una interfaz visual (Tkinter), permitiendo que un usuario interactúe con el algoritmo sin tocar el código. Entendí cómo este algoritmo utiliza la probabilidad para clasificar textos basándose en la frecuencia de palabras clave típicas de "Spam" o "Ham".

## Qué utilizamos
Para desarrollar este detector, se usaron las siguientes tecnologías y librerías:
Lenguaje: Python 3.x como base lógica.
Pandas: Para cargar el archivo spam.csv y manipular las columnas de datos (etiquetas y mensajes).
Scikit-Learn: La librería central para la inteligencia artificial. Específicamente usé:
train_test_split: Para separar datos de prueba y entenamiento.
CountVectorizer: Para transformar el texto en una matiz numérica.
MultinomialNB: El modelo de clasificación probabilístia.
Tkinter: Para construir la ventana, los botones y las etiquetas de resultados de la interfaz gráfica.

## Qué se podría mejorar
Aunque el programa funciona: Actualmente, el modelo se entrena cada vez que abro el programa. Podría usar algo para guardar el modelo entrenado y cargarlo al instante, ahorrando tiempo. Además de la precisión (Accuracy), podría agregar algo para ver cuántos correos legítimos fueron clasificados erróneamente como spam (falsos positivos).

## Conclusión personal y qué proyecto puedo realizar a futuro
La realización de este programa me permitió comprender cómo se aplican los conceptos teóricos de la Inteligencia Artificial en problemas de la vida real. Sprendí no solo sobre el entrenamiento de modelos, sino también sobre la importancia de crear herramientas accesibles paa el usuario final.

## Un siguiente proyecto podría ser un Analizador de Sentimientos. 
Usando una lógica muy similar, podría entrenar un modelo con reseñas de películas o productos para que el programa detecte si un comentario es Positivo, Negativo o Neutral. Esto tendría una aplicación comercial directa muy valiosa.