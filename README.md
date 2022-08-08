### Retos
###### Karla Castro Ascencio

**Reto 1**: Dado el sheet [click](https://docs.google.com/spreadsheets/d/1Y3h7fp-rMq-jZGf_Xb-SYzJcRKKDxjfUP4WQkQ7iKBY/edit?usp=sharing) , dirigirse al tab reto1 donde se encuentra una tabla con los autores que han sido clasificados en base a sentimiento, country y theme. Se necesita que se realice una pivot table en la cual las columnas base sean author y sentimiento y las columnas variables sean country y thema.

**Solución**: Dntro del [sheet](https://docs.google.com/spreadsheets/d/1Y3h7fp-rMq-jZGf_Xb-SYzJcRKKDxjfUP4WQkQ7iKBY/edit?usp=sharing) se generó la hoja `Result` con los datos tabulados que generó el scrip `test1.py`.
Se adjunta el chromedriver para facilitar la ejecución.

**Reto 2** : *Problema d Monty Hall*

En este concurso, el concursante escoge una puerta entre tres, y su premio consiste en lo que se encuentra detrás. Una de ellas oculta un coche, y tras las otras dos hay una cabra. Sin embargo, antes de abrirla, el presentador, que sabe dónde está el premio, abre una de las otras dos puertas y muestra que detrás de ella hay una cabra. Ahora tiene el concursante una última oportunidad de cambiar la puerta escogida ¿Debe el concursante mantener su elección original o escoger la otra puerta? ¿Hay alguna diferencia?

**Solución**: La solución seria que el participante debe cambiar de puerta, originalmente el participante solo tiene un 33.33..% de probabilidad de acertar al coche mientras que la probabilidad de perfer es de 66.66..%, una vez que una de las puertas es revelada la puerta de la elección inicial conserva el 33.33% pero la puerta libre, es decir que no se ha escogido aumenta su probabilidad a un 66.66..%. Así que, en efecto hay diferencia.
Definidiendo los valores en la variable `attemps` cada vez mas grande, con tendencia al infinito es mas cercana la probabilidad al 60%.
Si se añade una nueva puerta las probabilidades para la puerta seleccionada inicialmente se conserva, para la puerta restante que quedaba con el 66.66% se divide y regresa nuevamente al 33.33..%.


**Reto 3**:  Algunas veces la data requerida a extraer no está disponible en alguna api o link oficial de descarga, por eso en algunas ocasiones acudimos al Scraping de páginas web para lograr este reto. Una manera de realizar esto es usando el api de SELENIUM para python , la cual nos permite simular una navegación web , interactuar con la página y bajar la data requerida.
Esta página [link](http://www.pbclibrary.org/raton/mousercise.htm) está orientada a ambientar a las personas con el uso del mouse en sus computadoras. El desafío en este reto es mediante el uso de python y SELENIUM, crear un script que permita avanzar en los diferentes niveles de la página mencionada interactuando con los elementos y siguiendo las órdenes que se muestran. La página tiene 41 niveles.

**Solución**: El script genera la simulación sel flujo hasta donde fue posible.



