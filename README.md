# IX-Liquid

**IX-Liquid** is a bounded, field-deployable **liquid-remediation pilot platform** for contaminated surface water, oily runoff, spill-response holding tanks, maintenance-yard washdown, and other small mixed-liquid cleanup jobs where a full permanent plant would be overkill.

It is designed to do five things in sequence:

1. **Protect itself from bad feed** with intake screening and pretreatment.
2. **Knock down free oil, debris, and suspended solids** before expensive polishing media sees the load.
3. **Polish the remaining liquid** with cartridge filtration, activated carbon, and an optional ion-exchange mission pack.
4. **Verify output quality** with pressure, flow, conductivity, pH, ORP, turbidity, and state-aware controls.
5. **Route water safely** to discharge, recirculation, or hold depending on measured conditions and machine health.

## What IX-Liquid is for

Use IX-Liquid as a **pilot or response unit**, not as a fantasy municipal plant and not as a universal drinking-water machine.

Good fits:
- marinas and fueling zones
- oily stormwater and runoff pilots
- maintenance yards and washdown recovery
- spill-response support at small sites
- temporary remediation trials
- field studies to decide whether a permanent treatment train is justified

## What IX-Liquid is not

IX-Liquid is **not**:
- a municipal wastewater plant
- a drinking-water guarantee
- a PFAS destruction claim
- a substitute for site-specific permitting, sampling, or licensed engineering
- a claim of unattended operation in every environment

## Standalone architecture

IX-Liquid stands on four layers:

- **Capture layer**: coarse strainer, grit knockdown, coalescing separator, sorbent stage
- **Polishing layer**: cartridge filtration, activated carbon, optional ion exchange, optional UV-C
- **Verification layer**: flow, level, pressure, differential pressure, pH, ORP, conductivity, turbidity
- **Operations layer**: permissive-based startup, staged shutdown, event logging, maintenance flags, degraded mode, operator HMI

## Nominal pilot envelope

This repo is intentionally scoped to a **small pilot skid**:
- nominal flow target: **8 GPM**
- stretch target: **12 GPM**
- feed type: contaminated non-sewage liquid streams with debris/oil/particulate loading
- deployment: skid, pad, trailer, or dockside temporary install
- power: shore power or generator with battery-backed controls

## Build cost and time

Budgetary pilot-build range from this repo's BOM:
- **Low estimate:** $40,372
- **High estimate:** $66,515

Planning estimate for a serious first field pilot:
- **Team:** 3-5 engineers + 1-2 technicians/fabricators
- **Build window:** about **14-20 weeks** from design freeze to factory acceptance test
- **Nicer deployable/trailerized version:** **6-9 months**

See:
- [`bom/ix_liquid_bom.csv`](bom/ix_liquid_bom.csv)
- [`docs/ASSEMBLY.md`](docs/ASSEMBLY.md)
- [`docs/BUILD_SCHEDULE.md`](docs/BUILD_SCHEDULE.md)
- [`docs/PROOF_OF_CONCEPT.md`](docs/PROOF_OF_CONCEPT.md)

## Repo layout

```text
IX-Liquid/
├── bom/
├── configs/
├── docs/
├── examples/
├── schemas/
├── src/
├── tests/
├── assets/
└── tools/
```

## Fast start for repo users

1. Read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
2. Read [`docs/SAFETY_AND_NON_CLAIMS.md`](docs/SAFETY_AND_NON_CLAIMS.md)
3. Review [`bom/ix_liquid_bom.csv`](bom/ix_liquid_bom.csv)
4. Walk through [`docs/ASSEMBLY.md`](docs/ASSEMBLY.md)
5. Run the small control-logic model in `src/ix_liquid/`
6. Use [`docs/PROOF_OF_CONCEPT.md`](docs/PROOF_OF_CONCEPT.md) as the first validation ladder

## License

Apache 2.0. See [`LICENSE`](LICENSE).
