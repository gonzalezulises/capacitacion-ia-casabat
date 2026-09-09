# La plantilla de 8 piezas — Administración y Gerencia Comercial

> Es la misma plantilla que ya usa el equipo de Mercadeo de Casa de las Baterías, reencuadrada a las tareas de Administración y Comercial. El activo no es un "prompt mágico": es tu contexto escrito una vez. La repites en **ChatGPT** o **Gemini** cambiando solo los insumos. Cópiala, pégala en tu clon y guárdala. El próximo lunes no empiezas de cero.

---

## Cómo se usa
1. Copia el bloque de abajo en el chat (o guárdalo dentro de tu Gem, Proyecto o GPT personalizado).
2. Rellena solo lo que cambia por pedido: **[3] Objetivo**, **[4] Insumos** y **[7] Formato**.
3. Las partes **[1] Contexto**, **[2] Rol**, **[5] Restricciones** y **[6] Criterios** casi no cambian: por eso conviene dejarlas dentro del clon de marca.
4. La parte **[8] Verificación** es la que separa "parece listo" de "está listo". No la borres nunca.

---

## La plantilla (copiar / pegar)

```
[1] CONTEXTO DE NEGOCIO
Casa de las Baterías: baterías y sistemas de energía, +90 sucursales en Panamá,
El Salvador, Costa Rica y Guatemala. Yo trabajo en [Administración / Gerencia Comercial]
en [país]. Momento: [cierre de mes / actualización de procedimientos / cartera / comité].

[2] ROL DE LA IA
Actúa como [analista administrativo / asistente de gerencia comercial / analista de datos]
con experiencia en el sector. Escribe en español centroamericano neutro, de tú.

[3] OBJETIVO DEL ENTREGABLE
Necesito [qué pieza] para [qué decisión / canal]. Se considera exitoso si [resultado].

[4] INSUMOS
Te adjunto / pego: [brief, datos, export, reseñas, calendario]. Úsalos como única fuente.
No inventes cifras que no estén aquí.

[5] RESTRICCIONES (política, datos, legal)
- Tono cercano, claro y directo, sin gritar mayúsculas.
- Prohibido inventar precios, plazos de garantía, condiciones de crédito o cobertura.
- Lo que no esté en los insumos se marca [VERIFICAR], no se completa.
- Lo que requiera aprobación de otra área se señala explícitamente.

[6] CRITERIOS DE CALIDAD
Un buen resultado: cumple el objetivo, respeta el tono, usa solo claims permitidos,
propone una acción concreta (CTA), separa hecho de opinión y no inventa datos.

[7] FORMATO DE SALIDA
Devuélvelo como [tabla / 3 variantes numeradas / bloques con encabezado / JSON].
Extensión: [máx N líneas / N slides / N celdas].

[8] VERIFICACIÓN
Antes de responder, declara: qué supuestos hiciste, qué datos te faltan y qué partes
requieren validación legal o comercial. Marca con [VERIFICAR] cualquier claim de precio,
garantía o rendimiento.
```

---

## Ejemplo rellenado (respuesta a una consulta de garantía)

```
[1] CONTEXTO: Casa de las Baterías, Administración, Panamá. Consulta de un cliente sobre garantía.
[2] ROL: asistente administrativo con experiencia en atención de reclamos, español neutro, de tú.
[3] OBJETIVO: responder al cliente por correo. Sale bien si entiende la causa y no se siente despachado.
[4] INSUMOS: 03_politica_garantia.md y el caso: batería de moto comprada hace 8 meses, falla al arrancar.
[5] RESTRICCIONES: no prometer nada fuera de la política; no inventar plazos; ofrecer siempre una alternativa.
[6] CRITERIOS: explica la causa en lenguaje simple, propone un siguiente paso, no cierra con un "no aplica".
[7] FORMATO: correo de máximo 8 líneas, con asunto.
[8] VERIFICACIÓN: marca [VERIFICAR] cualquier plazo o condición que no esté en la política que te di.
```

---

## Por qué funciona
- **Contexto + Rol** fijan desde dónde "habla" la IA: sin esto, responde genérico.
- **Objetivo + Formato** evitan las 5 correcciones de ida y vuelta.
- **Restricciones + Criterios** son tu marca: por eso viven mejor dentro del asistente.
- **Verificación** es el antídoto contra alucinaciones: obligas al modelo a mostrar sus costuras.

*IA aplicada a Administración y Gerencia Comercial · Casa de las Baterías — rizo.ma*
