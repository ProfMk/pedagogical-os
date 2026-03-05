# PEDAGOGICAL OS – ROADMAP TÉCNICO v3.0
Versión: 3.0  
Fecha: 1 Marzo 2026  
Objetivo: Sistema gobernado y estable listo para piloto en julio 2026.

---

## OBJETIVO ESTRATÉGICO

Construir un Sistema Operativo Pedagógico:

- Arquitectura limpia (DDD + Layered)
- Snapshot por periodo (indicator_result)
- Gobernanza institucional formal
- Dashboard docente funcional
- Cierre y reapertura auditados
- IA opcional controlada
- Listo para colegio piloto (1200 estudiantes)

---

## PRINCIPIOS ARQUITECTÓNICOS CONGELADOS

1. indicator_result ES snapshot por periodo.
2. No se crea tabla snapshot adicional.
3. Periodos pueden cerrarse y reabrirse.
4. Toda acción de cierre/reapertura queda auditada.
5. Docente no puede modificar periodo cerrado.
6. Reapertura solo por rol autorizado.
7. Gobernanza > nuevas features.

---

## MARZO – GOBERNANZA Y BLINDAJE

- Use case CloseAcademicPeriod
- Use case ReopenAcademicPeriod
- Tabla academic_period_event
- Bloqueo override si periodo cerrado
- Tests negativos obligatorios

Resultado: sistema institucionalmente seguro.

---

## ABRIL – UI DOCENTE BASE

- Login institucional_user
- Dashboard docente
- Visualización estado periodo
- Override desde UI
- Control básico por roles

Resultado: usable por docentes reales.

---

## MAYO – OPERATIVIDAD REAL

- Importación masiva estudiantes
- Carga batch evidencias
- Recalculo engine
- Optimización performance

Resultado: sistema estable para 1200 estudiantes.

---

## JUNIO – IA CONTROLADA + FREEZE

- Endpoint generación actividades
- Auditoría mínima IA
- Beta testing interno
- Freeze pre-piloto

---

## JULIO – PILOTO REAL

Sistema estable, gobernado y usable en colegio real.