# Validación C1–C5 — Ciclo del Fósforo

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
- Resultado: ❌ No

### C2 — Beneficio de Acoplamiento
- Definición: RMSE acoplado < RMSE desacoplado.
- Resultado: —

### C3 — Ablación EDI
- Definición: EDI > 0.01 y significativo por permutación.
- EDI = -1.000000
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
- CR = 1.0645675760514877
- Pass: ✅ Sí

### No-localidad
- Efecto macro no reducible a una única celda dominante.
- Dominance share: 0.0016037485275738773
- Pass: ✅ Sí

### Persistencia
- El efecto macro persiste en ventanas temporales.
- Std ratio: 0.3753782054536408
- Pass: ✅ Sí

## Veredicto
- **Nivel**: 0
- **Overall pass**: ❌ No
