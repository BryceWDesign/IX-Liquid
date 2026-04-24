# Acceptance criteria

## Pilot build acceptance

### Mechanical acceptance
- all components mounted with service clearance
- no unsupported pipe spans likely to fatigue
- all valves labeled and reachable
- secondary containment installed under leak-prone hardware
- no cross-zone drainage into controls area

### Electrical acceptance
- panel layout documented
- terminal numbers match drawings/configs
- all field devices individually verified
- backup power preserves controls and logging during short brownout
- alarm tower and HMI both show critical state

### Controls acceptance
- startup permissives enforced
- stale-data timeout enforced
- route decisions traceable in the event log
- ESD_0 through ESD_3 perform as designed
- manual acknowledgement required after ESD_2 and ESD_3

### Process acceptance
- clean-water nominal pilot flow established
- no visible free oil at controlled discharge during proof test
- differential pressure instrumentation catches filter loading
- final routing blocks discharge when quality verification fails
- samples can be collected upstream, midstream, and downstream

## Documentation acceptance
- BOM complete
- assembly instructions complete
- state machine documented
- I/O map complete
- alarm matrix complete
- commissioning checklist complete
- maintenance log template present
