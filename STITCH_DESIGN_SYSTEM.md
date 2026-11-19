---
name: "UniQuiz DZ System"
description: "A bilingual & trilingual SaaS design system for Algerian university quiz creation, examination delivery, and academic evaluation."
---

## Overview

UniQuiz DZ is an institutional SaaS platform built for Algerian higher education (Faculties of Technology, Mechanical Engineering, and Energetics). It accommodates university instructors, department administrators, and engineering students across French, English, and Arabic (RTL). The visual identity combines a clean modern SaaS structure with authoritative academic poise: deep Algerian Navy Blue (`#0B1B3D`) grounding the workspace, vibrant Royal Blue (`#1D4ED8`) for focus and primary actions, and warm neutral slate surfaces ensuring low cognitive strain during complex evaluations.

## Colors

The palette leverages a high-contrast Navy & Royal Blue hierarchy. Primary roles provide institutional authority, secondary roles deliver actionable focus, and feedback colors follow standard academic grade thresholds (Success >= 14/20, Warning 10-13.9/20, Error < 10/20).

- **Primary:** Deep institutional navy blue reflecting Algerian university rigor.
- **Secondary:** Energetic Royal Blue driving actions and progress states.
- **Surface & Neutrals:** Crisp white and light slate layers tailored for clean SaaS dashboards.
- **Academic Grading:** Clear semantic cues calibrated for Algeria's 20-point scale.

```yaml
colors:
  navy-brand: "#0B1B3D"
  royal-blue: "#1D4ED8"
  royal-hover: "#1E40AF"
  royal-light: "#EFF6FF"
  slate-border: "#CBD5E1"
  slate-muted: "#475569"
  grade-high: "#15803D"
  grade-mid: "#92400E"
  grade-low: "#991B1B"
  light:
    primary: "#0B1B3D"
    on-primary: "#FFFFFF"
    secondary: "#1D4ED8"
    on-secondary: "#FFFFFF"
    surface: "#FFFFFF"
    on-surface: "#0F172A"
    surface-variant: "#F1F5F9"
    on-surface-variant: "#334155"
    outline: "#94A3B8"
    outline-variant: "#CBD5E1"
    success: "#15803D"
    on-success: "#FFFFFF"
    warning: "#92400E"
    on-warning: "#FFFFFF"
    error: "#991B1B"
    on-error: "#FFFFFF"
  dark:
    primary: "#93C5FD"
    on-primary: "#0B1B3D"
    secondary: "#60A5FA"
    on-secondary: "#0B1B3D"
    surface: "#0B132B"
    on-surface: "#F8FAFC"
    surface-variant: "#1E293B"
    on-surface-variant: "#CBD5E1"
    outline: "#334155"
    outline-variant: "#1E293B"
    success: "#4ADE80"
    on-success: "#064E3B"
    warning: "#FBBF24"
    on-warning: "#78350F"
    error: "#F87171"
    on-error: "#641717"
```

## Typography

Pairing **Red Hat Display** for clean structural headlines with **Radio Canada Big** for multilingual body legibility and **Source Code Pro** for numerical scores, formulas, and thermodynamics engineering values.

```yaml
typography:
  display-lg:
    fontFamily: "Red Hat Display"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 44px
    letterSpacing: -0.5px
  display-lg-mobile:
    fontFamily: "Red Hat Display"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 34px
    letterSpacing: -0.25px
  headline-xl:
    fontFamily: "Red Hat Display"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 40px
    letterSpacing: -0.5px
  headline-xl-mobile:
    fontFamily: "Red Hat Display"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 32px
    letterSpacing: -0.25px
  headline-lg:
    fontFamily: "Red Hat Display"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 32px
    letterSpacing: -0.2px
  headline-lg-mobile:
    fontFamily: "Red Hat Display"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: -0.1px
  headline-md:
    fontFamily: "Red Hat Display"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: 0px
  headline-sm:
    fontFamily: "Red Hat Display"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 26px
    letterSpacing: 0px
  title-lg:
    fontFamily: "Red Hat Display"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px
    letterSpacing: 0px
  body-lg:
    fontFamily: "Radio Canada Big"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: 0px
  body-md:
    fontFamily: "Radio Canada Big"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0px
  body-sm:
    fontFamily: "Radio Canada Big"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
    letterSpacing: 0px
  label-lg:
    fontFamily: "Radio Canada Big"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 20px
    letterSpacing: 0.1px
  label-md:
    fontFamily: "Radio Canada Big"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 16px
    letterSpacing: 0.2px
  label-sm:
    fontFamily: "Radio Canada Big"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 14px
    letterSpacing: 0.2px
  code-md:
    fontFamily: "Source Code Pro"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0px
```

## Layout & Spacing

A structured SaaS layout model combining a persistent desktop sidebar (width 260px) and a fixed top bar (height 64px) with high-density content containers. Mobile experiences fold navigation into touch-friendly bottom bars or top header drawbars.

```yaml
spacing:
  gutter-xs: 4px
  gutter-sm: 8px
  gutter-md: 16px
  gutter-lg: 24px
  gutter-xl: 32px
  section: 40px
  page-margin: 24px
```

## Elevation & Depth

Subtle border-led depth replaces heavy drop shadows. Surfaces rest on crisp hairline borders (`outline-variant`) with optional low-opacity ambient lift (`0 1px 3px 0 rgba(15, 23, 42, 0.06)`). Active examination sheets and modal overlays take high-elevation focus masks to eliminate testing distractions.

## Shapes

Precise, geometric rounding reflecting engineering instruments. Inputs, buttons, and cards maintain moderate radii to convey structural stability.

```yaml
rounded:
  sm: 4px
  DEFAULT: 6px
  md: 8px
  lg: 12px
  xl: 16px
  full: 9999px
```

## Motion & Micro-interaction

Micro-interactions are snappy and reassuring. Countdown timers, question submission badges, and language toggles update crisply without disruptive bouncy layout shifts.

```yaml
motion:
  state-change:
    duration: 120ms
    delay: 0ms
    timingFunction: ease-out
  surface-enter:
    duration: 200ms
    delay: 0ms
    timingFunction: cubic-bezier(0.16, 1, 0.3, 1)
  surface-exit:
    duration: 120ms
    delay: 0ms
    timingFunction: cubic-bezier(0.4, 0, 1, 1)
```

## Voice & Content Strategy

The voice of UniQuiz DZ is authoritative, clear, and bilingual/trilingual.
- **Tone:** Academic, exact, encouraging.
- **Grades:** Always formatted in the Algerian standard `XX.XX / 20` (e.g., `16.50 / 20.00` - "Mention Très Bien").
- **Language support:** Native toggles between English (`EN`), French (`FR`), and Arabic (`AR`, with `dir="rtl"` layout).
- **Domain vocabulary:** Mechanical Engineering & Thermodynamics (e.g., "Carnot Cycle Efficiency", "Rankine Cycle Superheating", "Enthalpy & Entropy Variations", "Module: ME-302").
