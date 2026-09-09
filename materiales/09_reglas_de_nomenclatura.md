# Regla de nomenclatura documental — Casa de las Baterías

> **Material de práctica del taller.** Regla ilustrativa con la forma típica de una norma de
> control documental. **No es la norma oficial de Casa de las Baterías**: se usa en la
> **Sesión 2, ejercicio 11** para practicar la auditoría automatizada. Si tu área tiene su regla
> real, sustitúyela: el ejercicio funciona igual.

## Estructura del nombre de archivo

**Procedimientos:**

```
PR-<AREA>-<###>_<Titulo_En_Palabras_Capitalizadas>_v<N>.<ext>
```

**Anexos:**

```
PR-<AREA>-<###>-ANEXO-<LETRA>_<titulo_en_minusculas>_v<N>.<ext>
```

## Reglas

1. `<AREA>` son exactamente **tres letras mayúsculas**: `ADM` (Administración), `COM` (Comercial),
   `OPE` (Operaciones), `FIN` (Finanzas).
2. `<###>` es el correlativo de **tres dígitos**, con ceros a la izquierda. `014`, nunca `14`.
3. El separador entre el código y el título es un **guion bajo**. Dentro del código, guion medio.
4. El título **no lleva espacios, ni tildes, ni caracteres especiales**: se usan guiones bajos.
5. La versión va al final, siempre **`v` minúscula** seguida del número: `v1`, `v2`, `v10`.
6. `<LETRA>` del anexo es una sola letra mayúscula, correlativa desde `A` sin saltos.
7. El anexo hereda el código completo del procedimiento al que pertenece.

## Ejemplos válidos

```
PR-ADM-014_Gestion_de_Cotizaciones_v2.md
PR-ADM-014-ANEXO-A_formato_de_cotizacion_v2.md
PR-COM-007_Atencion_de_Reclamos_v4.md
PR-OPE-102-ANEXO-B_ruta_de_despacho_v1.md
```

## Reglas de integridad del expediente

8. **Todo anexo referenciado debe existir** en el expediente.
9. **Todo anexo que existe debe estar referenciado** al menos una vez desde su procedimiento.
   Un anexo huérfano se elimina o se justifica.
10. El **código declarado dentro** del documento debe coincidir con el del nombre del archivo.
11. Las referencias cruzadas indican la **versión vigente**, no una anterior.
12. Un mismo anexo se nombra **igual en todas las menciones** del procedimiento.
