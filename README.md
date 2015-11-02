# dynamic_typesetting

Implementación de Programación dinámica para la justificación del texto según un conjunto de palabras y un márgen máximo por línea dado.

Dependencias
----
1. Interfaz **TkInter** usada para el diseño de la interfaz del programa.[1] ([tutorial])
2. Widget **MultiListBox**, creada por _Bob Hauck_.[2]

Manual de uso
----
Inice el fichero `gui.py` mediante:

`$ python gui.py`

Para abrir un fichero con el conjunto de palabras deseado, acceda al menu _File_ y seleccione la opción _Open_. Se le abrirá una ventana para seleccionar el fichero, elija y acepte.

Al cerrarse la ventana podrá observar que en la lista de la izquierda que en un principio estaba vacía, aparece su lista de palabras junto a la longitud de cada una en la segunda columna.

Seleccione el margen mediante la escala situada en la parte superior derecha de la ventana o introduciendo en número en la caja a su derecha, y active el _Typeset_ con el botón con un nombre homónimo. Puede repetir en proceso volviendo a pulsar el botón.

Para limpiar la lista de palabras y la caja de texto, selección en el menú _File_ la opción _Clear_

Autoría y distribución
----
**Autor**: [Ismael J. Taboada](https://github.com/ismtabo)

**Fecha de modificación**: 02 de Noviembre de 2015

### Distribución

El programa se hizo con fines educativos para la asignatura de **Algoritmos y Computación** de la mención de _ del Grado Superior de Ingenería Informática_ en la **Escuela Técnica Superior de Ingeniería Informática** ([ETSII](inf.uva.es)).

La distribución está sujeta a las condiciones descritas en la cabecera del fichero `multilistbox.py`, debido al Copyright que contiene dicho fichero.


[1]: https://wiki.python.org/moin/TkInter
[tutorial]: http://www.tutorialspoint.com/python/tk_text.htm
[2]: http://tkinter.unpythonic.net/wiki/mhMultiListBox
