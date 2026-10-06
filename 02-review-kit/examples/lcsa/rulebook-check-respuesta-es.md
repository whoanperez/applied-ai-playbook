**Verificado contra:** Fondo Meridian, Convocatoria MF-CFP-2026/02 (publicada el 1 de octubre de 2026; plazo 15 de enero de 2027, 17:00 UTC) · **Trabajo:** ATLAS, propuesta de la LCSA
**Resultado:** 61 requisitos · ✅ 45 cumplidos · ❌ 7 no cumplidos · ◐ 1 parcial · ? 8 sin poder verificar
**Veredicto:** No se puede presentar tal como está. Hay tres fallos de elegibilidad y admisibilidad: el período de ejecución empieza el 1 de marzo de 2027 y la convocatoria no permite iniciar antes del 1 de abril de 2027; faltan las hojas de vida del personal clave, que son un anexo obligatorio; y la cofinanciación es del 19,4 % cuando el mínimo es el 20 %. Además hay tres errores de presupuesto (costos indirectos, evaluación final y suscripción en la nube). Todos se corrigen con cambios acotados, y quedan más de tres meses hasta el plazo.

Un apunte: usted escribe «ASCL» y la propuesta usa «LCSA» en todo el texto. No es un requisito de la convocatoria, pero conviene que coincida con el nombre de la entidad que figura en los anexos y en el portal. Uso «LCSA» abajo.

### Corregir antes de presentar

1. **R07 · Fecha de inicio** · convocatoria §3 → propuesta, portada y §4
   - **Regla:** «la fecha de inicio más temprana permitida del período de ejecución es el 1 de abril de 2027, y ninguna actividad del proyecto puede comenzar, ni puede incurrirse en ningún costo, antes de esa fecha».
   - **Problema:** la portada dice «del 1 de marzo de 2027 al 31 de agosto de 2028» y §4 dice «El mes 1 es marzo de 2027». Eso es un mes antes de lo permitido. Los costos de marzo (personal contratado, suscripción, horas en especie) no serían elegibles.
   - **Fix:** mover todo un mes. 18 meses desde el 1 de abril de 2027 terminan el 30 de septiembre de 2028, que sigue siendo ≤ 31 de diciembre de 2028 (R08). Texto para pegar:
     - Portada: «Período de ejecución: 18 meses, del 1 de abril de 2027 al 30 de septiembre de 2028».
     - §4: «El mes 1 es abril de 2027.»
     - §4, informes: «…dentro de los 60 días siguientes a la fecha de terminación, es decir, a más tardar el 29 de noviembre de 2028.» Los informes semestrales vencen el 30 de octubre de 2027, el 30 de abril de 2028 y el 30 de octubre de 2028.
     - §9: «…durante al menos 24 meses después del 30 de septiembre de 2028…».
   - Vea también «Para revisar a mano» sobre la licitación y otros trabajos previos al 1 de abril.

2. **R36 · Hojas de vida del personal clave (anexo obligatorio)** · convocatoria §6 → propuesta, lista de anexos
   - **Regla:** «La propuesta debe ir acompañada de… las hojas de vida del personal clave (véase el Anexo I)». El Anexo I define personal clave como «como mínimo, el líder del proyecto y el líder técnico».
   - **Problema:** los anexos A a F no incluyen hojas de vida. El Anexo F es un organigrama y términos de referencia, que no sustituyen una hoja de vida. Es un anexo que falta, y eso puede dejar la propuesta fuera de trámite.
   - **Fix:** añadir un anexo con las hojas de vida de Tomas Rivell (líder del proyecto) y Amara Okafor (líder técnica), como PDF separado. Línea para la lista de anexos: «**Anexo G** — Hojas de vida del personal clave (líder del proyecto y líder técnica)».

3. **R10 · Cofinanciación ≥ 20 %** · convocatoria §4 y Anexo I → propuesta §10
   - **Regla:** «una cofinanciación equivalente a por lo menos el 20 % del costo total del proyecto». El Anexo I define el costo total como costos directos elegibles más costos indirectos, subvención y cofinanciación incluidas.
   - **Problema:** `88.000 / 453.200 = 19,4 % < 20 %`. El mínimo es `0,20 × 453.200 = 90.640`; faltan 2.640. La frase de §10 «aproximadamente una quinta parte» oculta que está por debajo. Además, las correcciones de los puntos 4 a 6 cambian el costo total, así que la cifra final es la del presupuesto corregido de abajo.
   - **Fix:** subir la cofinanciación a USD 90.025 (20,06 % del costo total corregido; ver el cuadro). En el cuadro lo hago con más tiempo de personal de planta en la partida 1.3. Esa es la vía más simple, pero depende de que LCSA pueda respaldarlo con hojas de tiempo; si prefiere efectivo u otro aporte en especie, el monto mínimo es el mismo. Reemplazar la frase final de §10 por: «El aporte de la LCSA, de USD 90.025 y totalmente en especie, equivale al 20,06 % del costo total del proyecto (USD 448.885).» El Anexo C tiene que reflejar la cifra nueva.

4. **R12 · Costos indirectos ≤ 7 %** · convocatoria §4 y Anexo I → propuesta §10, partida 8.1
   - **Regla:** «una tasa fija de hasta el 7 % del total de los costos directos elegibles». El Anexo I define los costos directos elegibles como los financiados con la subvención o con la cofinanciación.
   - **Problema:** `30.200 / 423.000 = 7,14 % > 7 %`; el máximo era `0,07 × 423.000 = 29.610`. Si se calcula solo sobre la subvención, es peor: `30.200 / 335.000 = 9,0 %`.
   - **Fix:** fijar la partida 8.1 en USD 29.360 sobre los costos directos corregidos (`29.360 / 419.525 = 7,0 %`; tope `29.366`). Ver el cuadro.

5. **R59 · Evaluación final ≥ 3 % de la subvención** · convocatoria §14 nota 3 → propuesta §10, partida 6.2
   - **Regla:** «La evaluación final debe presupuestarse por un valor no inferior al 3 % de la subvención solicitada».
   - **Problema:** `9.000 / 365.200 = 2,46 % < 3 %`; el mínimo era `0,03 × 365.200 = 10.956`.
   - **Fix:** partida 6.2 en USD 11.000 (`11.000 / 358.860 = 3,07 %`, mínimo `10.766`). Ver el cuadro.

6. **R13 · Suscripción en la nube: solo la parte dentro del período de ejecución** · convocatoria §5 → propuesta §10, partida 2.2
   - **Regla:** las suscripciones y los servicios en la nube «son elegibles únicamente por la parte de su vigencia que coincida con el período de ejecución… la parte correspondiente a cualquier período posterior a la fecha de terminación del proyecto no es elegible… aun cuando se pague durante el período de ejecución».
   - **Problema:** la partida 2.2 («contratada por 24 meses… y pagada a la firma del contrato») imputa `24 × 1.250 = 30.000` a la subvención. El proyecto dura 18 meses, así que solo `18 × 1.250 = 22.500` es elegible. Los `6 × 1.250 = 7.500` de los meses 19 a 24 no lo son, y tampoco pueden contar como cofinanciación, porque no son un costo elegible.
   - **Fix:** partida 2.2 en USD 22.500. Texto de justificación: «Suscripción a la plataforma de modelo de lenguaje y nube, a USD 1.250 mensuales. Se imputan al proyecto los 18 meses de la ejecución (abril de 2027 a septiembre de 2028). Los meses posteriores, pagados por adelantado para obtener la tarifa con descuento, los cubre la LCSA con su presupuesto ordinario y no se imputan al proyecto ni a la cofinanciación.»

   **Presupuesto corregido** (aplica R10, R12, R13 y R59 a la vez; solo cambian las filas marcadas):

   | N.º | Partida | Subvención | Cofinanciación | Total |
   |---|---|---:|---:|---:|
   | 1.3 ◄ | Tiempo del personal de planta, en especie (2.490 h × USD 22,50) | – | 56.025 | 56.025 |
   | 2.2 ◄ | Suscripción a la plataforma y nube (18 meses × 1.250) | 22.500 | – | 22.500 |
   | 6.2 ◄ | Evaluación final externa | 11.000 | – | 11.000 |
   | | Resto de partidas sin cambio (1.1, 1.2, 2.1, 2.3, 3.1, 4.1, 4.2, 5.1, 6.1, 7.1) | 296.000 | 34.000 | 330.000 |
   | | **Total costos directos** | **329.500** | **90.025** | **419.525** |
   | 8.1 ◄ | Costos indirectos | 29.360 | – | 29.360 |
   | | **Costo total del proyecto** | **358.860** | **90.025** | **448.885** |

   Verificación con las cifras corregidas: subvención 358.860 en [150.000; 400.000] ✅; cofinanciación `90.025 / 448.885 = 20,06 %` ≥ 20 % ✅; indirectos `29.360 / 419.525 = 7,0 %` ≤ 7 % ✅; evaluación `11.000 / 358.860 = 3,07 %` ≥ 3 % ✅; visibilidad `6.000 / 358.860 = 1,67 %` ≤ 2 % ✅; equipos `18.000 / 419.525 = 4,3 %` ≤ 10 % ✅ (con los USD 10.000 de servidores existentes, 6,7 %). Hay que actualizar las cifras en la portada y en el Resumen («subvención de USD 358.860; costo total de USD 448.885»), en el Anexo B y en el Anexo C. Las 2.490 horas son una propuesta mía para llegar al 20 %: confirme que LCSA puede registrarlas con hojas de tiempo; si no, use otra fuente de aporte.

7. **R38 · Línea de base de todo indicador de efecto** · convocatoria §7 y nota 2 → propuesta §5, indicador E4
   - **Regla:** «Todo indicador de efecto debe tener un valor de línea de base cuantificado, que indique el año al que se refiere el valor y su fuente». La nota 2 añade que, si se prevé una encuesta durante el proyecto para afinar los datos, «el valor disponible en el momento de la presentación debe reportarse igualmente como línea de base».
   - **Problema:** E1, E2, E3 y E5 cumplen (con año y fuente), pero E4 dice «Se establecerá a partir de los registros de casos durante la fase inicial (M3)». No hay valor, y §2 admite que la LCSA hoy no puede medir ese tiempo porque cada nueva presentación se registra como expediente nuevo. Además, el único objetivo específico sobre solicitudes incompletas (OE2) queda sin ningún indicador con línea de base.
   - **Fix, una de dos vías:**
     - (a) Antes del 15 de enero de 2027, reconstruir a mano el tiempo de una muestra de expedientes cerrados de 2026 y reportarlo con año, fuente y método. Plantilla: «[valor] días (2026, revisión manual de [n] expedientes cerrados del subsidio de vivienda y de la exención de tasas, reconstruyendo la fecha de la primera presentación; se afinará en la fase inicial)». Los corchetes los tiene que llenar usted con datos reales.
     - (b) Añadir un indicador que sí tiene línea de base en la propia propuesta: «E6. Proporción de solicitudes del subsidio de vivienda y de la exención de tasas devueltas por estar incompletas, en las oficinas piloto. Línea de base: 31 % (2026, registros de servicio de la LCSA). Meta (M18): [por definir por la LCSA]. Medio de verificación: extractos del sistema de gestión de casos.» Esto mantiene el total en seis indicadores de efecto. Si deja E4, conviene hacer también (a).
   - Si cambia el marco de resultados, hay que reflejarlo en el Anexo A.

8. **R50 · Responsable de cada riesgo** · convocatoria §10 → propuesta §8
   - **Regla:** la matriz debe indicar, para cada riesgo, «su probabilidad, su impacto, las medidas de mitigación y el responsable del riesgo, es decir, la persona o dependencia encargada de hacer seguimiento al riesgo y de aplicar las medidas de mitigación».
   - **Problema:** la matriz tiene las columnas Riesgo, Probabilidad, Impacto y Mitigación. No tiene la columna de responsable.
   - **Fix:** añadir una columna «Responsable». Propuesta que usted debe confirmar:

     | Riesgo | Responsable |
     |---|---|
     | Respuestas incorrectas o inventadas | Líder técnica (A. Okafor) |
     | Violación de seguridad de datos personales | Oficial de Protección de Datos de la LCSA |
     | Baja adopción por parte del personal | Líder del proyecto (T. Rivell) |
     | Baja adopción o exclusión de usuarios mayores y personas con discapacidad | Líder del proyecto (T. Rivell), con el especialista de contenido |
     | Retraso en la licitación de integración | Líder del proyecto, con el área de contratación de la LCSA |
     | Cambio de prioridades institucionales | Directora General (H. Varga), presidenta del comité directivo |

### Matriz de cumplimiento

| # | Requisito (convocatoria §) | Estado | Evidencia en la propuesta |
|---|---|---|---|
| R01 | Solicitante: entidad pública nacional o subnacional que presta servicios al público (§2) | ✅ | Portada: «entidad pública del gobierno regional de Larkfield»; opera 11 oficinas |
| R02 | Constituida legalmente ≥ 3 años al plazo (§2, nota 1) | ✅ | §2: «creada por ordenanza regional en 2015» (≈ 11 años al 15/01/2027) |
| R03 | Proyecto que introduce o mejora herramientas de IA en servicios de uso directo (§2) | ✅ | §1: ATLAS para información, citas, estado de solicitudes y certificados |
| R04 | Diseñado como piloto de alcance limitado (§2) | ✅ | §1: «dos oficinas de atención (Northgate y Riverside) y en el portal» |
| R05 | Punto go/no-go con criterios explícitos y medibles (§2) | ✅ | §5: «Criterios de continuidad (M17)»: exactitud ≥ 95 %, E1 −30 %, E3 ≥ 3,9, sin incidente grave |
| R06 | Duración de 12 a 24 meses (§3) | ✅ | Portada: 18 meses |
| R07 | Inicio no antes del 1/04/2027; sin actividad ni costo antes (§3) | ❌ | Portada: «del 1 de marzo de 2027»; §4: «El mes 1 es marzo de 2027» |
| R08 | Terminar a más tardar el 31/12/2028 (§3) | ✅ | 31/08/2028 (30/09/2028 tras la corrección) |
| R09 | Subvención entre USD 150.000 y 400.000 (§4) | ✅ | 365.200 (358.860 corregida) |
| R10 | Cofinanciación ≥ 20 % del costo total (§4, Anexo I) | ❌ | 88.000 / 453.200 = 19,4 % < 20 % |
| R11 | Aportes en especie valorados al costo, con método explicado (§4) | ✅ | §10: 1.3 (2.400 h × 22,50 = 54.000); 4.1 (24 × 250 = 6.000); 7.1 (18 × 1.000 + 10.000 = 28.000) |
| R12 | Costos indirectos ≤ 7 % de los directos elegibles (§4, Anexo I) | ❌ | 30.200 / 423.000 = 7,14 % > 7 % |
| R13 | Software y nube: solo la parte dentro del período de ejecución (§5) | ❌ | 2.2: 24 meses pagados; 24 × 1.250 = 30.000, elegible 18 × 1.250 = 22.500 |
| R14 | Personal contratado para el proyecto elegible; salarios de planta no (§5) | ✅ | 1.1–1.2 término fijo; planta solo en 1.3, en especie |
| R15 | Equipos ≤ 10 % de los costos directos (§5) | ✅ | 18.000 / 423.000 = 4,3 % (6,6 % con los 10.000 de servidores existentes) |
| R16 | Sin costos no elegibles: terrenos, obras, vehículos, deudas, multas, intereses, pérdidas cambiarias, imprevistos (§5) | ✅ | Ninguna partida del cuadro de §10 cae en esas categorías |
| R17 | Costos identificables en la contabilidad y no financiados por otro donante (§5) | ? | La propuesta no lo declara |
| R18 | Redactada en inglés o español (§6) | ✅ | Español |
| R19 | Parte narrativa ≤ 15 páginas A4, letra ≥ 11 pt (§6) | ? | Portada: «13 páginas A4 en letra de 11 puntos» (declarado; no se puede contar en Markdown) |
| R20 | Diez secciones, en el orden indicado (§6) | ✅ | Secciones 1 a 10 en el orden exigido |
| R21 | Resumen ≤ 300 palabras (§6) | ✅ | 255 palabras (conteo) |
| R22 | Resumen con problema, solución, resultados, subvención y costo total (§6) | ✅ | §1: espera de 38 min; ATLAS; 38→22 min; «subvención de USD 365.200… costo total… USD 453.200» |
| R23 | Contexto: servicios, usuarios y evidencia del problema (§6) | ✅ | §2: 58 % de visitas de bajo riesgo; 38 min; 31 % devueltas; encuesta n = 1.180 |
| R24 | Objetivos general y específicos y teoría del cambio (§6) | ✅ | §3: objetivo general, OE1–OE3, «Teoría del cambio» |
| R25 | Actividades y cronograma por mes o trimestre (§6) | ✅ | §4: A1–A5 y tabla por trimestre |
| R26 | Arreglos de gestión y personal clave (§6) | ✅ | §4: «Gestión y personal clave» (comité directivo, OTD) |
| R27 | Personal clave: líder del proyecto y líder técnico (Anexo I) | ✅ | Portada: T. Rivell (líder del proyecto), A. Okafor (líder técnica) |
| R28 | Plan de adquisiciones (§6) | ✅ | §4: «Plan de adquisiciones» |
| R29 | Arreglos de informes y evaluación (§6) | ✅ | §4: «Informes y evaluación» |
| R30 | Cuadro de presupuesto por partida, con columnas separadas para subvención y cofinanciación (§6) | ✅ | §10: columnas «Subvención (USD)» y «Cofinanciación LCSA (USD)» |
| R31 | Justificación de cada partida (§6) | ✅ | §10: «Justificación del presupuesto» cubre 1.1 a 8.1 |
| R32 | Anexo: marco lógico (§6) | ? | Anexo A listado; no compartido (debe reproducir el marco de §5, según §7) |
| R33 | Anexo: presupuesto detallado en la plantilla del Fondo (§6) | ? | Anexo B listado; no compartido |
| R34 | Anexo: carta de cofinanciación firmada por el representante legal (§6) | ? | Anexo C listado, «firmada por la Directora General»; firma no verificable |
| R35 | Anexo: EIPD que cubra los tratamientos del piloto (§6, §9) | ? | Anexo D listado; no compartido (ver la fecha en «Para revisar a mano») |
| R36 | Anexo: hojas de vida del personal clave (§6) | ❌ | Lista de anexos A–F: no hay hojas de vida |
| R37 | Anexo: ≥ 1 carta de apoyo de una organización de usuarios (§6) | ? | Anexo E listado (Red de Derechos de las Personas con Discapacidad y Consejo de Personas Mayores); no compartido |
| R38 | Todo indicador de efecto con línea de base cuantificada, año y fuente (§7, nota 2) | ◐ | E1, E2, E3, E5 con año y fuente; E4: «Se establecerá… durante la fase inicial (M3)» |
| R39 | Todo indicador con meta cuantificada al final y medio de verificación (§7) | ✅ | E1–E5 y P1–P5 con meta y medio de verificación |
| R40 | Análisis de género e inclusión con grupos en riesgo y medidas (§8) | ✅ | §6: cinco grupos en riesgo y «Medidas» |
| R41 | Interfaces con la norma nacional de accesibilidad, nivel intermedio o superior (§8) | ✅ | §6: interfaz conversacional, portal y quioscos «en su nivel de conformidad intermedio», con auditoría externa |
| R42 | Ningún servicio solo por el canal de IA; canales presencial y telefónico en igualdad de condiciones durante todo el proyecto (§8) | ✅ | §6: «Todos los servicios del piloto seguirán disponibles de forma presencial y telefónica, con los mismos horarios y el mismo personal» |
| R43 | Pruebas con usuarios antes y durante el piloto, con personas con discapacidad y de 65 años o más (§8) | ✅ | §6 y P5: 60 usuarios, ≥ 15 y ≥ 15; las rondas durante el piloto «seguirán las mismas cuotas» |
| R44 | Base jurídica, categorías de datos y plazos de conservación (§9) | ✅ | §7: «Base jurídica», «Categorías de datos», «Conservación» (90 días, 5 años, 2 años) |
| R45 | Sin entrenar ni mejorar modelos con datos personales; contratos lo excluyen (§9) | ✅ | §7: «no se entrena ni se ajusta ningún modelo… Los contratos… excluirán cualquier uso» |
| R46 | Decisiones sobre beneficios adoptadas por un funcionario humano (§9) | ✅ | §7: «Cada decisión la adopta un funcionario de casos» |
| R47 | Informar al usuario de que habla con una IA (§9) | ✅ | §7: aviso al inicio de toda conversación |
| R48 | Poder pasar a un agente humano en cualquier momento (§9) | ✅ | §7: «hablar con una persona» en cada paso, con línea telefónica 24 h |
| R49 | Matriz de riesgos con probabilidad, impacto y mitigación (§10) | ✅ | §8: columnas Probabilidad, Impacto y Mitigación |
| R50 | Responsable de cada riesgo (§10) | ❌ | §8: no hay columna ni responsable |
| R51 | Explicar cómo se operará la solución tras la subvención (§11) | ✅ | §9: costo de operación de USD 52.000 al año, alcance del piloto |
| R52 | Compromiso de financiar la operación ≥ 12 meses tras el fin del período (§11) | ✅ | §9: «al menos 24 meses después del 31 de agosto de 2028» |
| R53 | Identificar la fuente de los recursos (§11) | ✅ | §9: «programa 03, “Canales digitales”» |
| R54 | Contratos > USD 50.000 con procedimiento competitivo y ≥ 3 ofertas válidas (§12) | ✅ | Integración 96.000: licitación abierta, ≥ 3 ofertas, relanzamiento si hay menos; los demás contratos < 50.000 |
| R55 | Visibilidad en partida separada y ≤ 2 % de la subvención (§13) | ✅ | 5.1: 6.000 / 365.200 = 1,64 % ≤ 2 % |
| R56 | Reconocer al Fondo con su logotipo en materiales, publicaciones e interfaces (§13) | ✅ | 5.1: logotipo en materiales, publicaciones, pantalla de bienvenida de ATLAS y quioscos |
| R57 | Informes semestrales ≤ 30 días y final ≤ 60 días (§14) | ✅ | §4: ≤ 30 días; final al 30/10/2028 = 31/08/2028 + 60 días (pasa al 29/11/2028 con R07) |
| R58 | Evaluación final externa e independiente (§14, nota 3) | ✅ | §4: evaluador «sin ninguna relación contractual ni jerárquica con la LCSA» |
| R59 | Evaluación presupuestada ≥ 3 % de la subvención (§14, nota 3) | ❌ | 6.2: 9.000 / 365.200 = 2,46 % < 3 % |
| R60 | Presentar por el portal antes del 15/01/2027 17:00 UTC (§15) | ✅ | Portada: 12 de enero de 2027 (fecha prevista) |
| R61 | Narrativa en un PDF; presupuesto en su formato de hoja de cálculo; demás anexos en PDF separados (§15) | ? | Portada lo prevé; se verifica al cargar los archivos |

### Para revisar a mano

- **R35 · Fecha de la EIPD.** §7 dice «En noviembre de 2026 se completó una EIPD». Hoy es 6 de octubre de 2026, así que esa frase habla de un hecho que aún no ocurrió. Corrija el texto con el estado real, por ejemplo «Se completará el [fecha]» o «Se completó el [fecha]», y confirme que el Anexo D cubre todos los tratamientos del piloto, en especial los datos de salud de los certificados de discapacidad y los registros de conversación.
- **R34 · Anexo C.** Que esté firmada por la Sra. Varga, que tenga el monto nuevo de cofinanciación (USD 90.025) y que confirme también el compromiso de sostenibilidad de 24 meses que §9 le atribuye. §9 cita el Anexo C para eso, y la convocatoria lo describe solo como carta de cofinanciación.
- **R32, R33 · Anexos A y B.** El Anexo A debe reproducir el marco de resultados de §5 (con E4 o E6 corregido); el Anexo B tiene que ser la plantilla del Fondo y coincidir con el presupuesto corregido.
- **R37 · Anexo E.** Que existan las dos cartas, firmadas y de organizaciones que representan a usuarios.
- **R17 · Costos.** Que ninguna partida ya esté financiada por otro donante o por otra subvención del Fondo, y que todas se puedan identificar en la contabilidad de LCSA.
- **R19 · Extensión.** Contar las páginas en el PDF final: ≤ 15 A4, letra ≥ 11 pt. Al añadir el indicador E6 y la columna de responsables, compruebe que sigue en 15 o menos.
- **R61 · Paquete de archivos.** Narrativa en un único PDF; Anexo B en hoja de cálculo original; los demás anexos en PDF separados.
- **Trabajos previos al 1 de abril (R07).** El hito «adjudicación de la licitación (M2)» y el riesgo «pliegos preparados con antelación» sugieren trabajo antes de empezar. Preparar los pliegos sin costo imputado no es un problema, pero no lance la licitación ni cargue horas en especie (R10) antes del 1 de abril de 2027, o pasan a no elegibles.

### Recomendado, no obligatorio

1. Añadir a la matriz de riesgos un riesgo tecnológico explícito (fallas de integración, caídas del servicio, dependencia del proveedor). §10 dice que el Fondo espera ver riesgos tecnológicos, y hoy la matriz solo tiene el de respuestas incorrectas, el de seguridad y el de retraso de licitación.
2. Alinear la definición de E1 con su línea de base. Los 38 minutos de §2 son la espera promedio general de Northgate y Riverside, pero E1 se refiere a «trámites de bajo riesgo». Un evaluador puede preguntar por esa diferencia, y afecta a la puntuación de diseño y metodología (25 puntos).
3. Mencionar en §4 que los términos de referencia de la evaluación final se enviarán al Fondo para su revisión antes de contratar al evaluador (§14, nota 3). Es un paso que el Fondo hará de todos modos, y mostrarlo refuerza la credibilidad de la evaluación independiente.

¿Quiere que aplique estas correcciones al documento (fechas, presupuesto, columna de responsables, indicador E6 y lista de anexos)? Solo lo haré si me lo confirma, y los valores entre corchetes tendrá que darlos usted.
