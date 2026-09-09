# El filtro de las 8 preguntas — ¿sale o no sale?

> **Material de práctica del taller.** Es la adaptación, para Administración y Gerencia Comercial,
> del filtro que el equipo de Mercadeo de Casa de las Baterías ya usa. Se aplica a **todo** lo que
> produzca la IA antes de que salga a un cliente, a jefatura o a un comité. Cárgalo dentro de tu
> clon para que lo aplique solo.
>
> Se usa en la **Sesión 1, ejercicio 3**.

---

## Cómo puntuar

Marca cada punto como **Sí / No / Dudoso**. Regla dura: **un solo "No" en los puntos 4, 6 o 7
detiene el envío** hasta corregir. Los "Dudoso" se resuelven preguntando al modelo o verificando
en la fuente.

| # | Pregunta | Qué buscas | Si falla |
| --- | --- | --- | --- |
| 1 | ¿Cumple el objetivo del pedido? | Responde a lo que pediste, no a algo parecido. | Reescribe el objetivo en el prompt (parte `[3]`). |
| 2 | ¿Suena a una persona de Casa de las Baterías? | Cercano, claro, directo, sin gritar mayúsculas ni sonar a folleto. | Recuerda el tono en las restricciones (parte `[5]`) o dale tus ejemplos. |
| 3 | ¿Promete algo que no puedes sostener? | Plazos, excepciones o condiciones que no están en la política. | Quita la promesa o consíguela aprobada por quien corresponde. |
| 4 | ¿Usa cifras, precios o plazos que tú no le diste? | Todo número debe poder rastrearse al insumo. | **DETENER.** Marca `[VERIFICAR]` y confirma en la fuente. |
| 5 | ¿Propone un siguiente paso concreto? | Qué pasa después, quién lo hace, para cuándo. | Pide explícitamente el siguiente paso. |
| 6 | ¿Inventó algún dato? | Cruza cada afirmación contra lo que le pegaste. | **DETENER.** Elimina lo inventado; exige la fuente. |
| 7 | ¿Requiere aprobación de otra área? | Crédito, garantías, descuentos fuera de rango, cambios de control. | **DETENER.** Deriva antes de enviar. |
| 8 | ¿Es usable tal cual, o hay que rehacerlo? | Si vas a reescribir más del 20 %, el problema está en el pedido. | Vuelve al prompt, no al texto. |

---

## Versión corta, para pegar dentro de tu clon

```
Antes de entregarme la versión final, evalúa tu propia respuesta con estas ocho preguntas y
responde cada una con sí o no y una línea de justificación:
1. ¿Cumple el objetivo que pedí?
2. ¿Suena a una persona de Casa de las Baterías o suena a IA?
3. ¿Promete algo que no puedo sostener?
4. ¿Usa cifras, precios o plazos que yo no te di?
5. ¿Propone un siguiente paso concreto?
6. ¿Inventaste algún dato?
7. ¿Algo de esto necesita aprobación de otra área?
8. ¿Se usa tal cual o hay que rehacerlo?
Después entrégame solo la versión corregida.
```

*IA aplicada a Administración y Gerencia Comercial · Casa de las Baterías — rizo.ma*
