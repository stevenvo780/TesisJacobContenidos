# Validación C1–C5 — Riesgo Biológico Global

## Fase Sintética (Ground Truth)
- C1 (Convergencia): ✅ Sí
- C2 (Beneficio acoplamiento): —
- C3 (Ablación EDI): —
- C4 (Robustez ruido): —
- C5 (Parsimonia): —

**Gate sintético**: C2+C3+C4 deben pasar para habilitar fase real.
- Gate resultado: —

## Fase Real (Datos Empíricos)

### C1 — Convergencia
- Definición: ABM y ODE deben ajustar la serie con error < umbral.
- Resultado: ✅ Sí

### C2 — Beneficio de Acoplamiento
- Definición: RMSE acoplado < RMSE desacoplado.
- Resultado: —

### C3 — Ablación EDI
- Definición: EDI > 0.01 y significativo por permutación.
- EDI = 0.105111
- Resultado: —

### C4 — Robustez al Ruido
- Definición: EDI estable bajo 5 niveles de ruido (CV < umbral).
- Resultado: —

### C5 — Parsimonia
- Definición: modelo macro mejora predicción sin sobreajuste.
- Resultado: —

## Propiedades Adicionales

### Symploké
- Cohesión interna > externa → delimitación funcional.
- CR = 1.0018780148511328
- Pass: ✅ Sí

### No-localidad
- Efecto macro no reducible a una única celda dominante.
- Dominance share: 0.0016001971972706155
- Pass: ✅ Sí

### Persistencia
- El efecto macro persiste en ventanas temporales.
- Std ratio: 4.527399326784245
- Pass: ✅ Sí

## Veredicto
- **Nivel**: 1
- **Overall pass**: ❌ No
