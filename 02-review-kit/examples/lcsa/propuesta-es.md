# ATLAS — Un asistente de IA para los servicios al ciudadano de Larkfield

> Ejemplo ficticio de entrenamiento. Esta propuesta incumple a propósito 8 de los 42 requisitos de la convocatoria (ver `../../tests/materials/rulebook-answer-key.md`).

**Propuesta presentada al Fondo Meridian para Servicios Públicos Digitales**
**Convocatoria de Propuestas MF-CFP-2026/02 — Inteligencia Artificial Responsable en los Servicios al Ciudadano**

| | |
|---|---|
| Solicitante | Agencia de Servicios al Ciudadano de Larkfield (LCSA), entidad pública del gobierno regional de Larkfield |
| Dependencia ejecutora | Oficina de Transformación Digital (OTD) de la LCSA |
| Representante legal | Sra. Helena Varga, Directora General |
| Líder del proyecto | Sr. Tomas Rivell, Jefe de la Oficina de Transformación Digital |
| Líder técnica | Sra. Amara Okafor, Arquitecta Sénior de Soluciones, OTD |
| Contacto | Tomas Rivell, t.rivell@lcsa.example, +00 555 0142 |
| Subvención solicitada | USD 365.200 |
| Cofinanciación de la LCSA | USD 88.000 (en especie) |
| Costo total del proyecto | USD 453.200 |
| Período de ejecución | 18 meses, del 1 de marzo de 2027 al 31 de agosto de 2028 |
| Idioma y extensión | Español; parte narrativa de 13 páginas A4 en letra de 11 puntos, sin contar anexos |
| Presentación | Portal en línea del Fondo, 12 de enero de 2027 (parte narrativa en PDF; Anexo B en formato de hoja de cálculo; demás anexos en archivos PDF separados) |

---

## 1. Resumen

La Agencia de Servicios al Ciudadano de Larkfield (LCSA) atiende cerca de 410.000 visitas presenciales al año. Más de la mitad corresponden a asuntos sencillos (información, citas, estado de solicitudes, certificados estándar), pero generan esperas promedio de 38 minutos en nuestras oficinas más concurridas, mientras que muchas solicitudes del subsidio de vivienda y de la exención de tasas por discapacidad se devuelven por falta de documentos.

Proponemos un piloto de 12 meses de ATLAS, un asistente de IA para los servicios al ciudadano, en dos oficinas de atención (Northgate y Riverside) y en el portal web de la LCSA. ATLAS responderá preguntas usando únicamente los manuales de servicio de la LCSA (recuperación de información, sin entrenamiento con datos personales) y completará trámites de bajo riesgo: citas, estado de solicitudes y certificados. Para el subsidio de vivienda y la exención de tasas por discapacidad, solo hará una verificación previa de documentos; un funcionario de casos adopta cada decisión. Los canales presencial y telefónico se mantienen sin cambios.

Esperamos reducir la espera promedio en las oficinas piloto de 38 a 22 minutos, duplicar la proporción de trámites sencillos completados sin visita y elevar la satisfacción de los usuarios de 3,4 a 4,0 sobre 5. Una decisión de continuidad (*go/no-go*) en el mes 17 determinará si ATLAS se extiende a las otras nueve oficinas de la LCSA.

El proyecto dura 18 meses y lo lidera la Oficina de Transformación Digital de la LCSA. Solicitamos una subvención de USD 365.200; el costo total del proyecto es de USD 453.200.

## 2. Contexto y problema

La LCSA fue creada por ordenanza regional en 2015 como ventanilla única del gobierno regional de Larkfield. Opera 11 oficinas de atención, un centro de llamadas y un portal web.

Los registros de servicio de 2026 de la LCSA muestran tres problemas relacionados. Primero, el 58 % de las visitas presenciales corresponde a información o a trámites de bajo riesgo que no requieren el criterio de un funcionario de casos. En las dos oficinas más concurridas, Northgate y Riverside, el sistema de gestión de turnos registra una espera promedio de 38 minutos. Segundo, solo el 22 % de las solicitudes de bajo riesgo de las zonas de influencia de las dos oficinas se completa sin visita, principalmente porque la información del portal es difícil de encontrar. Tercero, el 31 % de las solicitudes del subsidio de vivienda y de la exención de tasas por discapacidad se devuelve por estar incompleto. Como el sistema actual de gestión de casos registra cada nueva presentación como un expediente nuevo, la LCSA no puede medir de forma confiable el tiempo transcurrido entre la primera presentación y la decisión para estas solicitudes.

Según la encuesta de usuarios de 2026 (n = 1.180), el 34 % de quienes visitan las oficinas tiene 60 años o más, el 12 % reporta una discapacidad, el 57 % son mujeres y el 18 % no tiene acceso a internet en el hogar.

## 3. Objetivos y teoría del cambio

**Objetivo general:** lograr que los servicios al ciudadano de la LCSA sean más rápidos, más fáciles y más inclusivos mediante el uso responsable de la IA.

**Objetivos específicos:**

- OE1. Resolver consultas de información y trámites de bajo riesgo a través de ATLAS, reduciendo las visitas evitables y los tiempos de espera.
- OE2. Reducir las solicitudes incompletas del subsidio de vivienda y de la exención de tasas por discapacidad mediante la verificación previa de documentos, manteniendo las decisiones en manos de los funcionarios de casos.
- OE3. Generar evidencia sobre exactitud, experiencia de usuario e inclusión para una decisión informada sobre el escalamiento.

**Teoría del cambio.** Si los residentes pueden obtener respuestas confiables y completar trámites sencillos en cualquier momento mediante un asistente que se basa únicamente en los manuales aprobados de la LCSA, y si los solicitantes saben antes de presentar su solicitud qué documentos les faltan, entonces menos personas harán fila y se devolverán menos expedientes, lo que liberará a los funcionarios de casos para los casos complejos. Esto supone que ATLAS responde con exactitud y que las personas que prefieren la atención humana siguen recibiéndola en igualdad de condiciones; el muestreo de calidad, las pruebas de accesibilidad y los canales humanos sin cambios atienden estos supuestos.

## 4. Actividades y plan de trabajo

**A1. Fase inicial (meses 1–4).** Conformación del comité directivo; licitación abierta de los servicios de integración; curaduría de unas 1.400 páginas de manuales de servicio; levantamiento de datos de línea de base.

**A2. Construcción y pruebas (meses 2–4).** Integración con los sistemas de citas, seguimiento de solicitudes y certificados; índice de recuperación; auditorías de accesibilidad y de seguridad; pruebas de usabilidad con 60 usuarios.

**A3. Capacitación y gestión del cambio (meses 3–6).** Capacitación de 120 funcionarios.

**A4. Operación del piloto (meses 5–16).** Doce meses de operación en Northgate, Riverside y el portal, con muestreo mensual de calidad de al menos 200 respuestas y rondas de pruebas con usuarios en los meses 8 y 13.

**A5. Evaluación y decisión (meses 15–18).** Evaluación final externa; decisión de continuidad sobre el escalamiento en el mes 17; informe final y difusión.

| Actividad | M1–3 | M4–6 | M7–9 | M10–12 | M13–15 | M16–18 |
|---|---|---|---|---|---|---|
| A1 Fase inicial | ● | ● (M4) | | | | |
| A2 Construcción y pruebas | ● (M2–3) | ● (M4) | | | | |
| A3 Capacitación | ● (M3) | ● | | | | |
| A4 Operación del piloto | | ● (desde M5) | ● | ● | ● | ● (M16) |
| A5 Evaluación y decisión | | | | | ● (M15) | ● |

El mes 1 es marzo de 2027. **Hitos:** adjudicación de la licitación (M2); puesta en marcha en ambas oficinas y en el portal (M5); revisión de medio término (M11); decisión de continuidad (M17).

**Gestión y personal clave.** Un comité directivo presidido por la Directora General, del que forma parte el Oficial de Protección de Datos, se reúne trimestralmente; la gestión diaria está a cargo de la OTD. El líder del proyecto, Tomas Rivell, dirige la OTD desde 2021 y lideró el rediseño del portal de la LCSA. La líder técnica, Amara Okafor, tiene diez años de experiencia en proyectos de integración en el sector público. Un coordinador del proyecto y dos especialistas de contenido se contratarán a término fijo.

**Plan de adquisiciones.** Los servicios de integración (USD 96.000) se contratarán mediante una licitación abierta y competitiva que exige al menos tres ofertas válidas; si se reciben menos, la licitación se relanzará. La suscripción a la plataforma, la auditoría de seguridad, la investigación con usuarios y la evaluación final se contratarán mediante solicitudes de cotización a al menos tres proveedores. Los quioscos y las tabletas se comprarán a través del acuerdo marco vigente de la LCSA para equipos de TI.

**Informes y evaluación.** La LCSA presentará informes de avance narrativos y financieros para los meses 1–6, 7–12 y 13–18, cada uno dentro de los 30 días siguientes al final del período, y un informe final narrativo y financiero dentro de los 60 días siguientes a la fecha de terminación, es decir, a más tardar el 30 de octubre de 2028. La evaluación final estará a cargo de un evaluador externo seleccionado de forma competitiva, sin ninguna relación contractual ni jerárquica con la LCSA para la ejecución de actividades del proyecto.

## 5. Marco de resultados

**Indicadores de efecto**

| Indicador | Línea de base (año, fuente) | Meta (M18) | Medio de verificación |
|---|---|---|---|
| E1. Tiempo promedio de espera para trámites de bajo riesgo en las oficinas piloto | 38 minutos (2026, sistema de gestión de turnos) | 22 minutos | Reportes mensuales del sistema de turnos |
| E2. Proporción de solicitudes de bajo riesgo de las zonas de influencia del piloto completadas sin visita a la oficina | 22 % (2026, registros de servicio de la LCSA) | 45 % | Registros de transacciones del portal, de ATLAS y de las oficinas |
| E3. Satisfacción de los usuarios con los canales piloto (escala 1–5) | 3,4 (2026, encuesta de usuarios de la LCSA, n = 1.180) | 4,0 | Encuestas de salida y en línea, trimestrales |
| E4. Tiempo promedio desde la primera presentación hasta la decisión, solicitudes del subsidio de vivienda y de la exención de tasas por discapacidad en las oficinas piloto | Se establecerá a partir de los registros de casos durante la fase inicial (M3) | Reducción del 30 % | Extractos del sistema de gestión de casos |
| E5. Proporción de usuarios de 65 años o más o con discapacidad que califican los canales piloto como fáciles de usar | 51 % (2026, encuesta de accesibilidad de la LCSA, n = 420) | 70 % | Encuestas de usuarios desagregadas |

**Indicadores de producto**

| Indicador | Meta | Medio de verificación |
|---|---|---|
| P1. ATLAS en operación en las dos oficinas piloto y en el portal | 3 canales en funcionamiento en el M5 | Actas de aceptación de la puesta en marcha |
| P2. Exactitud de las respuestas de ATLAS en el muestreo mensual de calidad | ≥ 95 % de respuestas correctas | Informes de muestreo de calidad |
| P3. Funcionarios capacitados en el uso y la supervisión de ATLAS | 120 funcionarios | Registros de asistencia y pruebas posteriores a la capacitación |
| P4. Interfaces que aprueban la auditoría externa de accesibilidad | 100 % de las interfaces de ATLAS | Informe de auditoría externa |
| P5. Participantes en pruebas de usabilidad | 60 antes de la puesta en marcha, incluidas ≥ 15 personas con discapacidad y ≥ 15 personas de 65 años o más | Informes de pruebas |

Todos los indicadores medidos a nivel individual se desagregarán por sexo, grupo de edad y condición de discapacidad.

**Criterios de continuidad (M17).** ATLAS solo se extenderá a las otras nueve oficinas si, durante los últimos seis meses de operación, la exactitud de las respuestas es de al menos el 95 %, el E1 se ha reducido al menos un 30 %, el E3 es de al menos 3,9 y no se ha producido ningún incidente grave de datos personales.

## 6. Inclusión y accesibilidad

**Análisis de género e inclusión.** La encuesta de usuarios de 2026 y los grupos focales con el personal identifican cinco grupos en riesgo de exclusión: las personas mayores, que representan un tercio de los visitantes y usan menos el portal; las personas con discapacidad visual, auditiva o cognitiva; las mujeres con responsabilidades de cuidado, que son el 64 % de quienes solicitan el subsidio de vivienda y tienen dificultades con el horario de atención; las personas con baja alfabetización; y los residentes sin internet en el hogar. Los principales riesgos son un asistente difícil de usar para estos grupos y el descuido de los canales humanos de los que dependen.

**Medidas.** ATLAS usará lenguaje claro y una opción de lectura en voz alta; los quioscos ofrecen interacción por voz y tamaño de texto ajustable. La interfaz conversacional, las páginas del portal y las interfaces de los quioscos y las tabletas cumplirán la norma nacional de accesibilidad web en su nivel de conformidad intermedio, verificado mediante una auditoría externa antes de la puesta en marcha y de nuevo en el mes 12. Las pruebas de usabilidad previas a la puesta en marcha involucrarán a 60 usuarios, incluidas al menos 15 personas con discapacidad y 15 personas de 65 años o más, convocadas con la Red de Derechos de las Personas con Discapacidad de Larkfield y el Consejo de Personas Mayores de Larkfield; las dos rondas de pruebas durante el piloto seguirán las mismas cuotas. Al menos la mitad de los participantes serán mujeres, con sesiones en horarios variados para facilitar la participación de quienes cuidan. Todos los servicios del piloto seguirán disponibles de forma presencial y telefónica, con los mismos horarios y el mismo personal, durante el proyecto y después de él.

## 7. Protección de datos y ética de la IA

**Base jurídica.** Todo el tratamiento se basa en el ejercicio de las funciones de servicio público de la LCSA conforme a su ordenanza de creación; para los datos de salud contenidos en los certificados de discapacidad, también en la disposición de la ley de protección de datos aplicable relativa a la gestión de prestaciones sociales.

**Categorías de datos.** Datos de identificación y de contacto; referencias y estado de solicitudes y citas; documentos cargados para la verificación previa, que pueden incluir certificados de ingresos y certificados de discapacidad; y registros de conversación.

**Conservación.** Los registros de conversación se seudonimizan al recogerse, se conservan 90 días para el muestreo de calidad y luego se eliminan. Los documentos cargados, los resultados de la verificación previa y las referencias de las solicitudes se guardan en el expediente y siguen su plazo de conservación según la tabla de retención documental de la LCSA (cinco años). Los datos de citas se conservan dos años, igual que en los canales existentes.

**EIPD.** En noviembre de 2026 se completó una EIPD que cubre todos los tratamientos del piloto, revisada por el Oficial de Protección de Datos de la LCSA (Anexo D).

**Sin entrenamiento con datos personales.** ATLAS genera respuestas únicamente a partir de los manuales aprobados de la LCSA mediante recuperación de información; no se entrena ni se ajusta ningún modelo. Los contratos con los proveedores de la plataforma y de la integración excluirán cualquier uso de los datos de la LCSA para entrenar o mejorar sus modelos.

**Decisiones humanas.** ATLAS verifica si las solicitudes del subsidio de vivienda y de la exención de tasas por discapacidad están completas e indica a los solicitantes qué documentos faltan; no puede aprobar, rechazar ni modificar una solicitud. Cada decisión la adopta un funcionario de casos. Los certificados que expide ATLAS solo reproducen registros existentes.

**Transparencia y contacto humano.** Toda conversación, en el portal y en los quioscos, se inicia con un aviso claro de que el usuario está hablando con un asistente de IA. En cada paso está disponible la opción «hablar con una persona», que transfiere al usuario a un funcionario por chat o, fuera del horario del chat, a la línea telefónica de 24 horas del centro de llamadas.

## 8. Gestión de riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| ATLAS da respuestas incorrectas o inventadas | Media | Alto | Respuestas restringidas a los manuales aprobados, con indicación de la fuente; muestreo mensual de calidad; transferencia automática cuando la confianza es baja |
| Violación de seguridad de datos personales | Baja | Alto | Medidas de la EIPD; registros seudonimizados; auditoría de seguridad y prueba de penetración antes de la puesta en marcha |
| Baja adopción por parte del personal | Media | Medio | Participación temprana del personal de primera línea en el diseño; capacitación; canal de retroalimentación |
| Baja adopción o exclusión de usuarios mayores y de personas con discapacidad | Media | Alto | Auditoría de accesibilidad; cuotas en las pruebas; quioscos asistidos; canales humanos sin cambios |
| Retraso en la licitación de integración | Media | Medio | Pliegos preparados con antelación; actividades de integración y de pruebas superpuestas en el plan de trabajo |
| Cambio de prioridades institucionales tras el ciclo presupuestal regional | Baja | Alto | Carta de compromiso de la Directora General; costos de operación incluidos en el proyecto de presupuesto institucional |

El comité directivo revisará la matriz de riesgos trimestralmente y la actualizará en cada informe de avance.

## 9. Sostenibilidad

El costo de operación de ATLAS a la escala del piloto se estima en USD 52.000 al año (suscripción a la plataforma, mantenimiento y un especialista de contenido). La LCSA se compromete a financiar la operación de ATLAS en las dos oficinas piloto y en el portal durante al menos 24 meses después del 31 de agosto de 2028, con cargo a su presupuesto ordinario de funcionamiento (programa 03, «Canales digitales»), según lo confirma la carta de la Directora General (Anexo C). La decisión de continuidad se refiere a la extensión a las otras nueve oficinas, que se financiaría con el presupuesto regional de 2029.

## 10. Presupuesto y justificación del presupuesto

| N.º | Partida presupuestal | Subvención (USD) | Cofinanciación LCSA (USD) | Total (USD) |
|---|---|---:|---:|---:|
| 1.1 | Coordinador del proyecto (término fijo, 18 meses) | 54.000 | – | 54.000 |
| 1.2 | Dos especialistas de contenido y diseño conversacional (término fijo, 12 meses cada uno) | 72.000 | – | 72.000 |
| 1.3 | Tiempo del personal de planta de la LCSA (OTD, funcionarios de casos, Oficial de Protección de Datos) — en especie | – | 54.000 | 54.000 |
| 2.1 | Servicios de integración y desarrollo de ATLAS | 96.000 | – | 96.000 |
| 2.2 | Suscripción a la plataforma de modelo de lenguaje y nube | 30.000 | – | 30.000 |
| 2.3 | Auditoría de seguridad y pruebas de penetración | 14.000 | – | 14.000 |
| 3.1 | Equipos para puntos de atención (4 quioscos accesibles, 6 tabletas) | 18.000 | – | 18.000 |
| 4.1 | Capacitación del personal y gestión del cambio | 16.000 | 6.000 | 22.000 |
| 4.2 | Pruebas de accesibilidad e investigación con usuarios | 12.000 | – | 12.000 |
| 5.1 | Comunicación y visibilidad | 6.000 | – | 6.000 |
| 6.1 | Línea de base, encuestas de seguimiento y recolección de datos | 8.000 | – | 8.000 |
| 6.2 | Evaluación final externa | 9.000 | – | 9.000 |
| 7.1 | Espacio de oficina, alojamiento e infraestructura existente — en especie | – | 28.000 | 28.000 |
| | **Total costos directos** | **335.000** | **88.000** | **423.000** |
| 8.1 | Costos indirectos | 30.200 | – | 30.200 |
| | **Costo total del proyecto** | **365.200** | **88.000** | **453.200** |

**Justificación del presupuesto.**

- **1.1–1.2.** Personal contratado específicamente para el proyecto a término fijo, según la escala salarial de la LCSA (USD 3.000 mensuales, incluidas las cargas patronales).
- **1.3.** Tiempo del personal de planta, contabilizado únicamente como cofinanciación en especie: 2.400 horas a un costo salarial real promedio de USD 22,50 por hora, registradas en hojas de tiempo.
- **2.1.** Integración con los sistemas de citas, seguimiento de solicitudes y certificados, y capa de recuperación de información; licitación abierta (véase la Sección 4).
- **2.2.** Suscripción a la plataforma de modelo de lenguaje y nube, contratada por 24 meses a partir del mes 1 y pagada a la firma del contrato para obtener una tarifa con descuento de USD 1.250 mensuales.
- **2.3.** Auditoría de seguridad y prueba de penetración antes de la puesta en marcha.
- **3.1.** Cuatro quioscos accesibles (USD 3.000 cada uno) y seis tabletas para atención asistida por funcionarios (USD 1.000 cada una).
- **4.1.** Diseño e impartición de la capacitación para 120 funcionarios (subvención); salas de capacitación aportadas por la LCSA, valoradas a su costo interno de USD 250 por día durante 24 días (cofinanciación).
- **4.2.** Auditorías de accesibilidad, sesiones de pruebas de usabilidad y compensación a los participantes.
- **5.1.** Señalización, materiales y eventos de difusión. El apoyo y el logotipo del Fondo figurarán en todos los materiales de comunicación, las publicaciones, la pantalla de bienvenida de ATLAS y los quioscos.
- **6.1–6.2.** Extracción de la línea de base, encuestas trimestrales y muestreo de calidad; evaluación final externa (véase la Sección 4).
- **7.1.** Espacio de trabajo para el equipo del proyecto durante 18 meses al costo interno de la LCSA de USD 1.000 mensuales (USD 18.000), más capacidad existente de servidores y red valorada a su costo depreciado (USD 10.000).
- **8.1.** Costos indirectos que cubren apoyo financiero, de contratación, jurídico y de auditoría.

El aporte de la LCSA, de USD 88.000 y totalmente en especie, representa aproximadamente una quinta parte del costo total del proyecto.

---

## Anexos

- **Anexo A** — Marco lógico
- **Anexo B** — Presupuesto detallado (plantilla de hoja de cálculo del Fondo)
- **Anexo C** — Carta de compromiso de cofinanciación, firmada por la Directora General, representante legal de la LCSA según su ordenanza de creación
- **Anexo D** — Evaluación de impacto relativa a la protección de datos del piloto ATLAS
- **Anexo E** — Cartas de apoyo de la Red de Derechos de las Personas con Discapacidad de Larkfield y del Consejo de Personas Mayores de Larkfield
- **Anexo F** — Organigrama de la Oficina de Transformación Digital y términos de referencia de los cargos del proyecto
