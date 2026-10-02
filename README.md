# IA aplicada a Administración y Gerencia Comercial CasaBat

Programa 2026 de tres sesiones presenciales con ritmo flexible para Administración y Gerencia Comercial de Casa de las Baterías. Los 48 laboratorios recorren selección de herramienta, síntesis documental, investigación, prototipado, Gems, comunicación operativa, garantías, ventas, devoluciones, expedientes y cierre mensual. La sesión 3 se construyó aparte: responde, una por una, las cuatro necesidades que la cohorte escribió en el formulario previo.

- Cliente: Casa de las Baterías
- Formato: presencial o remoto con facilitador
- Carga en vivo: 16 laboratorios por sesión y 4 por bloque
- Práctica: 16 ejercicios en 4 niveles
- Materiales para participantes: 23 DOCX y 4 XLSX
- Datos: todos los casos y cifras son ficticios

## Rótulo en pantalla y nombre de archivo

Los archivos conservan su nombre original para no romper los enlaces ya compartidos. Lo que cambió en octubre de 2026 fue el orden del programa.

| Rótulo en pantalla | Archivo | Título |
| --- | --- | --- |
| Sesión 1 | `sesion-3.html` | IA para Administración y Gerencia Comercial |
| Sesión 2 | `sesion-2.html` | Del dato a una decisión defendible |
| Sesión complementaria | `sesion-1.html` | De la necesidad a la capacidad |

Los verificadores nombran las sesiones por su archivo, no por su rótulo.

## Diseño curricular

### Sesión 1 De una necesidad a capacidad instalada

| Bloque | Laboratorios |
| --- | ---: |
| Elegir el entorno | 4 |
| Investigar y convertir | 4 |
| Crear una Gem útil | 4 |
| Llevarla a operación | 4 |

### Sesión 2 Cerrar el mes con evidencia

| Bloque | Laboratorios |
| --- | ---: |
| Investigar el dato | 4 |
| Explicar sin inventar causas | 4 |
| Resolver con datos y documentos | 4 |
| Convertir análisis en decisión | 4 |

### Sesión 3 IA para Administración y Gerencia Comercial

Diseñada desde el formulario previo (5 respuestas de la cohorte). Cada bloque resuelve una necesidad escrita por los participantes, citada entre comillas en el deck.

| Bloque | Responde a | Laboratorios |
| --- | --- | ---: |
| Pedir bien la primera vez | «qué prompts usar» · 3 de 5 respondientes | 4 |
| Que suene a ti | «que no se vea que es IA» | 4 |
| Tus cifras en una pantalla | «ejemplo de dashboard o gráficos» · 3 de 5 | 4 |
| Procedimientos sin dolor | «nomenclatura y códigos de procedimientos» | 4 |

El laboratorio de tablero trae una receta por herramienta —Gemini, ChatGPT y Claude— en slides propios, porque el formulario reportó ChatGPT en tres respuestas y Gemini en dos. Cada receta entrega un bloque para copiar y pegar.

Cierra un anexo opcional con tres caminos que no pasan por escribir un texto: el expediente convertido en resumen de audio con NotebookLM, la cámara de Gemini Live sobre una batería en sucursal, y una tarea programada de ChatGPT que revisa cada lunes las cotizaciones vencidas.

## Materiales

Los archivos Office son las fuentes canónicas para el curso. No se mantienen copias paralelas del contenido en Markdown o CSV.

```text
materiales/
  00_contexto_marca_casabat.docx
  01_especificacion_de_tarea.docx
  02_pruebas_de_aceptacion.docx
  03_politica_garantia.docx
  04_ventas_sucursales_2026.xlsx
  05_correos_pendientes.xlsx
  06_correos_de_referencia.docx
  07_notas_comite_operaciones.docx
  08_reporte_mensual_mayo.docx
  09_reglas_de_nomenclatura.docx
  10_PR-ADM-014_v3_BORRADOR.docx
  11_tecnicas_de_prompting.docx
  12_contexto_persistente_y_flujos.docx
  13_notas_recorrido_sucursales.docx
  14_inventario_demanda_sucursales.xlsx
  15_prompts_que_fallaron.docx
  16_maestro_procedimientos.xlsx
  17_tecnicas_y_cuando_usarlas.docx
  18_reclamos_de_clientes.docx
  19_comprobante_foto.png
  20_comparativa_herramientas.docx
  21_cotizaciones_semestre.xlsx
  22_que_puedo_subir.docx
  expediente-PR-ADM-014/
    Anexo B - Tabla de descuentos.docx
    PR-ADM-014-ANEXO-A_formato_de_cotizacion_v2.docx
    PR-ADM-014-ANEXO-C_matriz_de_aprobacion_V1.docx
    PR-ADM-014-ANEXO-F_registro_de_llamadas_v1.docx
    PR-ADM-014_Gestion_de_Cotizaciones_v2.docx
    PR-ADM-14-ANEXO-D_condiciones_de_credito_v1.docx
```

Los defectos de los libros y del expediente son intencionales. Alimentan las respuestas objetivas de los ejercicios y están protegidos por verificadores.

## Estructura técnica

```text
index.html                    hub del programa
sesion-1.html                 deck generado de la sesión 1
sesion-2.html                 deck generado de la sesión 2
sesion-3.html                 deck generado de la sesión 3
practica.html                 guía de 16 ejercicios
build/s1.py                   fuente de la sesión 1
build/s2.py                   fuente de la sesión 2
build/s3.py                   fuente de la sesión 3
build/materiales_sesion3.py   genera los materiales 15 y 16
build/practica.py             fuente de la práctica
build/deck.py                 componentes del deck
build/office_reader.py        lectura OOXML para verificadores
materiales/                   fuentes Office canónicas
materiales.zip                descarga conjunta
deck-stage.js                 motor del deck
verifica.mjs                  estructura, tiempos y enlaces
verifica-curriculo-2026.mjs   conceptos y carga curricular
verifica-materiales.mjs       formatos, defectos y trazabilidad
verifica-practica.mjs         respuestas objetivas
verifica-lenguaje.mjs         lenguaje llano de la sesión 3
verifica-maestro.mjs          fallos del maestro de procedimientos
verifica-insumos.mjs          que ningún laboratorio pida algo que no existe
verifica-cotizaciones.mjs     cifras y patrón del archivo comercial
verifica-layout.js            desbordes visuales en navegador
```

## Generación

Los HTML de sesión y práctica son generados. Se editan las fuentes en `build/`.

```bash
python3 build/build.py
python3 build/practica.py
```

Si cambia un material, se vuelve a crear el paquete:

```bash
zip -qr materiales.zip materiales -x '*.DS_Store'
```

## Verificación

```bash
node verifica.mjs
node verifica-curriculo-2026.mjs
node verifica-materiales.mjs
node verifica-practica.mjs
node verifica-lenguaje.mjs
node verifica-maestro.mjs
node verifica-insumos.mjs
node verifica-cotizaciones.mjs
```

Las compuertas verifican:

- 48 laboratorios, 4 por bloque y ritmo administrado por el facilitador;
- situación, rol, entrada, decisión, entregable y criterio en cada laboratorio;
- 23 DOCX y 4 XLSX sin formatos retirados;
- conservación de filas, tipos y defectos didácticos;
- tres nombres conformes y tres no conformes en el expediente;
- enlaces publicados y respuestas objetivas de la práctica;
- lenguaje de la sesión 3: frases de 25 palabras o menos, sin jerga de la lista negra, sin conceptos en mayúsculas y con cada laboratorio anclado en algo real de CasaBat;
- cifras del maestro de procedimientos recalculadas desde el XLSX y contrastadas contra las publicadas en el deck;
- insumos de los 48 laboratorios: todo archivo nombrado existe, toda referencia a otro laboratorio apunta hacia atrás y ningún prompt deja huecos sin explicar;
- criterios que describen el resultado y no predicen lo que hará el modelo, y ausencia de superlativos sin prueba comparativa;
- cifras y patrón del archivo de cotizaciones recalculados desde el XLSX: si el descuento alto deja de convertir peor, el laboratorio pierde su hallazgo y la compuerta avisa.

Para la comprobación visual, se sirve el sitio localmente y se ejecuta `verifica-layout.js` en cada deck.

```bash
python3 -m http.server 8877
```

## Navegación del deck

| Tecla | Acción |
| --- | --- |
| `←` `→` · `PgUp` `PgDn` · `Espacio` | Anterior o siguiente |
| `Home` `End` | Primer o último slide |
| `R` | Reiniciar |

Imprimir y guardar como PDF exporta un slide por página.

## Licencia

Privado. Material de capacitación para Casa de las Baterías vía Rizo.ma. No redistribuir sin autorización.
