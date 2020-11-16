Burriking 🍔🍟
====================================
A little burguer shop with global ambitions.

## Index

- [Specs](/README.md) 
- [Instructions](/docs/instructions.md) 
- [How it was developed](/docs/how-it-was-developed.md) 
- [API doc](/docs/api/orders.md) 

## Historia

### Los comienzos
Un día Albert E. quedó con un buen amigo para comentarle que quería abrir un restaurante. Era una idea que le estaba rondando por la cabeza desde hacía varios años, como la asignatura que siempre tienes pendiente o como aquella novia/o que nunca funcionó. Para ello necesitaba un socio en el que confiar ciegamente la receta secreta del aliño de carne para hamburguesa de su querida madre. Allí en un sofá de su casa, cerveza en mano, se empezó a forjar la idea. Aunque no eran empresarios, sabían que tenían que estudiar a la competencia, hicieron un recorrido por las mejores hamburgueserías de Torrevieja, Guardamar, Villena y, finalmente Benejúzar. Al final llegaron a una conclusión: no hay hamburgueserías que traten su producto desde un punto de vista estrictamente gourmet.

Mientras buscaban la ubicación adecuada, un día Albert paseando por Malasaña pasó por delante del antiguo Sumo, mítico restaurante japones de los años setenta, ¡se traspasaba!. Albert no durmió hasta conseguir convencer a su dueño, de que el japones ya no estaba en auge y que tenían que apostar por las hamburguesas.

Finalmente, el sueño se convirtió en realidad y así empezó una increíble historia...

### En la actualidad
Burriking está presente en Madrid, Valencia y Cáceres, con un total de 24 tiendas, 240 empleados y una facturación de cuatro millones de euros anuales. El éxito de nuestras tiendas actuales es tal, que ahora mismo nos encontramos en un proceso de expansión para llevar Burriking a 16 países con 470 tiendas más en total. Para soportar tal brutal expansión, el equipo técnico tiene que escalar el sistema que se emplea ahora mismo, basado en hojas de excel y comunicación manual entre los propios empleados. Lo bueno de tener un sistema informático tan rudimentario es que da mucha libertad al equipo técnico para tomar decisiones de diseño nuevas, además, como todos los procesos son manuales, podremos definir como serán estos procesos con nuestras futuras herramientas.

## Producto
Albert, nuestro CEO, le ha pedido a la CTO (Mabel O.) que le entregue en las próximas dos semanas un MVP técnico que actúe como base y ejemplo para poder dárselo a la empresa consultora de turno (Evil Corp). Este MVP va a estar acotado en funcionalidad, pero definirá la calidad del software a desarrollar por Evil Corp. 

Aquí entras tú como desarrollador de Burriking, para llevar a cabo el desarrollo del MVP del backend. Como puedes ver, es una pequeña pero importante tarea, pues tendrá implicaciones en la arquitectura de todo el futuro sistema de Burriking.

### Que se necesita
En esta primera versión solo se requiere que **el backend de soporte a dos casos de uso**:

- Hacer un pedido soportando todas las especificaciones que se indican.
- Listar los pedidos hechos por un usuario. De cada pedido se tiene que mostrar al menos toda la comida pedida, el precio total y la fecha de realización del pedido.

Mabel en una charla escuchó que el uso de servicios o incluso microservicios están de moda. Ha escuchado que son buenos para escalar sistemas y probablemente lo tenga en cuenta para valorar el MVP. Pero a ella no le importan mucho los lenguajes de programación, porque cree que todos son buenos (incluso Lisp), así que tienes total libertad de elección para el lenguaje.

### Pedidos
Los clientes pueden crear su pedido eligiendo entre una increíble selección de hamburguesas, patatas y refrescos de una gran calidad. Un pedido se compone de uno o varios de estos ingredientes (hamburguesas, patatas o refrescos). 

El precio del pedido se calcula en función los ingredientes que lo componen, y el tamaño de los mismos. Además, los pedidos pueden tener asociados alguna promoción.

### Carta Actual
El precio de la hamburguesa base de 125g es de 5€, y con un recargo en función del tamaño, lo mismo aplica para refrescos y patatas. En el plan de expasión se habla de más formas de personalización de la hamburguesa que vendrán determinadas por un nuevo departamento de I+D, no deberíamos de saberlo, pero en unos meses ¡tendremos nuevas opciones para personalizar la hamburguesa! 

- Hamburguesas:

    * Tamaños: 125g (5€), 250g (+2.5€) o 380g (+3.5€).  

- Patatas:
    
    * Tamaños: pequeñas (2€), mediano(+1.5€) o grandes (+2.5€).
 
- Refresco: 
    
    * Tamaños: pequeño (1.5€), mediano (+2.5€), grande (+3.5€).

### Promociones
Además para incentivar el consumo de ciertos ingredientes, es posible sacar promociones que afecten al precio total del pedido, en función de varios parámetros. Los parámetros de los que dependen las promociones en este compomento son, la composición y la fecha de creación del pedido, aunque en el futuro se podría dar soporte a reglas adicionales.

En este momento hay varias promociones activas:

- Euromanía: Se te descuenta un 10% de tu pedido. Válido miércoles y domingo.
- Refrescomanía: Si pides dos refrescos grandes y unas patatas se te descuenta el iva (21%). Válido solo días laborales.
- Burrimenu: Si pides una hamburguesa, un refresco y unas patatas tienes un descuento del 15%. Válido solo los fines de semana.

Además, un pedido solo puede ser afectado por la promoción de menor descuento.

## Procesos

### Pedido de un cliente

Ahora mismo cuando un cliente llega a uno de nuestros restaurantes mantiene una conversación, tal que:  
...  
Customer "C": Buenos días.  
Barista "B": Buenos días.  
...  
C: Eh tron, yo y la Yoly tenemos hambre, me pones una hamburguesa y patatas grandes.  
B: ¿Señor, quiere bebida? Así tiene la promoción "burrimenú" y le sale más barato.  
C: Ah, sí claro.  
...  
C: ¿Cuánto es mi pedido?  
B: Su pedido son 11,05€.  
C: Toma 20€.  
B: Gracias. Tome sus 18,95€ de cambio.  
C: Gracias.
... 
C: ¿Está mi pedido ya?  
B: Sí. Aquí lo tiene.  
...  
B: Adiós.  
C: Adiós. 

### Gestión de Almacén

En esta conversación el barista tiene abierto un excel, donde en una hoja especial llamada "Almacén", va mirando las provisiones que les quedan. En el caso de que el customer pida algo de lo que no queda, el barista se lo comunica.

===========

## Nota del equipo de Citibox
El ejercicio simula ser un proyecto real para intentar abarcar varias fases del ciclo de lanzamiento de un proyecto software. Su objetivo principal es demostrar conocimientos y razonamientos al problema propuesto. Para demostrar conocimientos y/o razonamientos no hace falta que sea mediante el código de programación. La solución propuesta puede estar formada por código de programación, artefactos del diseño de software, diagrams e incluso ideas bien reflejadas. Lo que sí debe estar implementado es lo que se pide explícitamente en el enunciado.

Además tienes que saber que se valorarán positivamente que exista un archivo con instrucciones específicas acerca de como está estructurada la prueba, como puede ser arrancada y probada, además de como crear/levantar un entorno de desarrollo y ser capaces de pasar los tests.

La prueba debería contener un testing mínimo que valide el correcto funcionamiento de los casos (tanto unitarios como E2E). 

**Es muy importante que la prueba funcione y consiga pasar sus propios tests**

Y lo más importante si tienes cualquier duda ¡pregúntanos! 
Fdo: Citibox Backend Team ❤️
