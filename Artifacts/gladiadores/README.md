# Dinamica Gladiadores - Tesis de Hiperobjetos

**Proposito**
Simular una defensa y refutacion de la tesis desde posiciones tecnicas y filosoficas, con jueces especialistas. Cada perfil incluye dinamica y entregables.

**Contexto base de la tesis (resumen operativo)**
- Hipotesis H1: un hiperobjeto es real si el modelo macro (ODE) demuestra eficacia causal metaestable sobre el micro (ABM).
- Metricas clave: EDI (umbral > 0.30 con asimilacion; > 0.05 en zero-nudging) y CR (umbral 2.0).
- Protocolo C1-C5: convergencia, robustez, determinismo aleatorio, linter de realidad, reporte de fallos.
- Reglas de rechazo: EDI < 0.30, coupling < 0.10, RMSE < e-10, EDI > 0.90.
- Casos: validados (Contaminacion, Movilidad), fallidos o parciales (Finanzas, Justicia, Estetica, etc.).

**Reglas de juego (por turnos)**
- Se juega en rondas por equipos: `equipo_defensor` (2 defensores), `equipo_critico` (2 atacantes) y `equipo_jueces` (3 jueces).
- Cada equipo tiene su turno y dentro de ese turno, cada miembro tiene su subturno para responder.
- Cada intervencion dura 3 minutos o 300 palabras (lo que ocurra primero).
- En cada intervencion se debe citar al menos 1 elemento de H1, C1-C5, EDI/CR o un caso.
- No se permiten respuestas ad hominem; toda critica debe proponer prueba o cambio concreto.
- Cada miembro puede pedir un derecho a replica (maximo 1 por persona en toda la dinamica).
- Los jueces no debaten: solo hacen preguntas y dictamen final.

**Entrega y trazabilidad (obligatorio)**
- Toda intervencion debe quedar en `Artifacts/gladiadores/HistorialDiscucion/iteracion_N/`.
- Nombre de archivos:
- `defensor_respuesta_N.md`
- `critico_respuesta_N.md`
- `jueces_preguntas_N.md`
- `jueces_veredicto_N.md`
- `moderador_comentarios_N.md`
- El equipo `equipo_jueces` deja **preguntas** en la iteracion actual (ej.: `jueces_preguntas_4.md`) y el siguiente turno es del defensor en **iteracion N+1**.
- Las cifras y afirmaciones tecnicas deben ser trazables a `metrics.json`, codigo o reportes con ruta exacta.

**Archivo de turnos**
- Archivo simple para ver y actualizar el turno: `Artifacts/gladiadores/turno.txt`.
- Se avanza manualmente reemplazando la linea `Turno actual:`.

**Orden recomendado**
1. Equipo defensor (2 defensores) expone tesis y fundamentos.
2. Equipo critico (2 atacantes) ataca supuestos y evidencia.
3. Equipo jueces (3 jueces) emite veredicto con puntaje y recomendaciones.

**Perfiles**
- `Artifacts/gladiadores/defensor_cientifico/perfil.md`
- `Artifacts/gladiadores/defensor_filosofico/perfil.md`
- `Artifacts/gladiadores/critico_cientifico/perfil.md`
- `Artifacts/gladiadores/critico_filosofico/perfil.md`
- `Artifacts/gladiadores/juez_complejidad/perfil.md`
- `Artifacts/gladiadores/juez_filosofia_ciencia/perfil.md`
- `Artifacts/gladiadores/juez_modelado_validacion/perfil.md`
