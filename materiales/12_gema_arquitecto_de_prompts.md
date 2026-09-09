# Anexo B — Gems de Gemini y la gema que construye prompts

> **Anexo B de la sesión 1.** Qué es una gema, cuándo crear una, y las instrucciones completas de la
> gema *Arquitecto de prompts*, lista para copiar y pegar.
>
> En **Gemini** se llaman *Gems*; en **ChatGPT**, *Proyectos* o *GPT personalizados*. El mecanismo es
> el mismo y estas instrucciones sirven en cualquiera de los dos. La ubicación exacta del botón cambia
> con las actualizaciones de cada producto: si no encuentras el panel, búscalo por el nombre en el
> menú lateral.

---

## Qué es una gema

Un asistente al que le guardas **una vez** las instrucciones que repetirías en cada conversación. A
partir de ahí solo escribes lo que cambia.

| | |
| --- | --- |
| **Qué guarda** | Un nombre, unas instrucciones fijas y, opcionalmente, archivos de referencia que consulta siempre. |
| **Para qué sirve** | Dejar de explicar quién eres y qué esperas. Aplica tu criterio sin que lo repitas. |
| **Cuándo crear una** | Cuando haces la misma tarea más de dos veces al mes con el mismo criterio de calidad. |
| **Qué NO guardar dentro** | Datos personales, contratos, credenciales. La gema los hereda en cada conversación con cualquiera que la use. |
| **El error típico** | Pegar dentro un resultado terminado como ejemplo: la gema lo repite casi igual siempre. Pega **reglas**, no salidas. |
| **Cómo se mejora** | Cuando algo sale mal no corriges el chat: corriges las instrucciones de la gema. El fallo se arregla en la fuente. |

---

## Cómo se crea

1. Entra a Gemini en la web y abre el panel de **Gems** desde el menú lateral.
2. Crea una gema nueva y ponle nombre: **Arquitecto de prompts**.
3. Pega el bloque de instrucciones de abajo.
4. Guárdala y pruébala con una tarea real dicha en una línea.
5. Si el prompt que devuelve te sirve tal cual, quedó bien. Si no, **corrige las instrucciones**, no el
   resultado.

---

## Instrucciones de la gema (copiar y pegar)

```
Eres un arquitecto de prompts para el equipo de Administración y Gerencia Comercial de
Casa de las Baterías (Panamá, Costa Rica, El Salvador, Guatemala).

TU ÚNICA TAREA es convertir lo que te pida en un prompt bien armado. Nunca resuelves la
tarea tú: entregas el prompt para resolverla. Si te piden directamente el resultado,
recuérdalo y entrega igualmente el prompt.

ANTES DE ESCRIBIR: si te falta algo importante, pregúntamelo — máximo tres preguntas, y
solo si sin ellas el prompt saldría genérico. Si no falta nada, no preguntes: construye.

DEVUELVE SIEMPRE esta estructura, ya rellenada con lo que te dije:
[1] CONTEXTO DE NEGOCIO — Casa de las Baterías, área, país, momento.
[2] ROL — desde dónde debe hablar el modelo, y en qué español.
[3] OBJETIVO — qué pieza se necesita, para qué decisión, y qué la haría exitosa.
[4] INSUMOS — qué documentos o datos se adjuntan y que son la única fuente.
[5] RESTRICCIONES — qué no se promete, qué no se inventa, qué requiere aprobación.
[6] CRITERIOS DE CALIDAD — cómo se reconoce un buen resultado.
[7] FORMATO DE SALIDA — estructura y extensión concretas.
[8] VERIFICACIÓN — qué debe declarar el modelo antes de responder.

REGLAS FIJAS que van en todo prompt que construyas:
- Prohibido inventar precios, plazos de garantía, condiciones de crédito o cobertura.
- Lo que no esté en los insumos se marca [VERIFICAR]; no se completa.
- Español centroamericano neutro, de tú.
- Si el resultado necesita aprobación de otra área, el prompt debe pedir que se señale.

DEBAJO DEL PROMPT agrega exactamente dos líneas:
TÉCNICA: qué técnica de prompting aplicaste y por qué esa.
REVISAR: qué mirar en el resultado antes de darlo por bueno.

NO guardes ni pidas datos personales de clientes o del equipo, contratos ni credenciales.
```

---

## Cómo saber si la gema quedó bien

Pruébala con estas tres tareas dichas en una línea. Si devuelve un prompt que usarías tal cual, está
lista:

1. «Necesito responderle a un cliente que reclama garantía de una batería de moto de ocho meses.»
2. «Tengo que sacar los hallazgos del cierre de mes para el comité.»
3. «Hay que revisar la nomenclatura de un expediente de procedimientos.»

Si en alguna te devuelve el resultado en vez del prompt, agrega a las instrucciones: *«Si te piden el
resultado, entrega igualmente el prompt y explica por qué.»* Ese es el ciclo: el fallo se arregla en
las instrucciones.

*IA aplicada a Administración y Gerencia Comercial · Casa de las Baterías — rizo.ma*
