# Proof of concept

## Objective

Prove that IX-Liquid can:
1. protect itself from bad feed,
2. remove bulk oil/solids before polishing media,
3. make correct routing decisions,
4. preserve evidence during faults,
5. produce repeatable pilot data without overstating treatment claims.

## Proof ladder

### P0 — Paper proof
Deliverables:
- architecture
- state machine
- alarm matrix
- BOM
- assembly plan
- sample plan

Exit criteria:
- no unresolved contradiction between routing, power, and maintenance access

### P1 — Dry proof
Tasks:
- energize panel
- verify HMI
- verify all inputs and outputs
- test startup permissives
- test staged shutdown logic
- force stale-data and bad-sensor cases

Exit criteria:
- every block reason visible on HMI
- every emergency level lands in the intended state

### P2 — Clean-water proof
Tasks:
- run clean water through all valid routes
- measure stable nominal flow at 8 GPM target
- verify pressure losses by stage
- confirm no leaks and no trapped drain issues

Exit criteria:
- 60 minutes stable run at nominal pilot flow
- no uncontrolled overflow
- no ambiguous route behavior

### P3 — Surrogate contaminated-water proof
Suggested feed:
- clean water + representative oil loading + solids surrogate
- do not use unknown hazardous chemistry for first proof

Tasks:
- test separation performance
- test cartridge and polishing path response
- test waste tote logic
- test recirculation on bad quality
- capture influent and effluent samples

Exit criteria:
- no visible free oil at verified discharge point during controlled trials
- discharge blocks correctly on induced high-turbidity / bad-sensor / waste-full conditions
- service triggers occur before catastrophic fouling

### P4 — Field pilot proof
Tasks:
- deploy at a bounded site
- operate with inspection plan
- maintain daily service log
- collect independent samples
- compare operating cost and service burden to objectives

Exit criteria:
- no major safety event
- log completeness >95%
- all blocked discharges traceable to sensor or process state
- operator can reconstruct every major stop

## Recommended measurements

- influent flow
- effluent flow
- turbidity trend
- conductivity trend
- pH
- ORP
- separator level
- waste tote level
- pre/post filter differential pressure
- event log timestamps
- route decision timestamps

## Core acceptance criteria

The first proof should be modest and falsifiable.

Recommended initial criteria:
- maintain **8 GPM nominal** pilot flow on clean-water shakedown
- correctly refuse startup when any critical permissive is false
- correctly route to hold or recirculation when final verification is out of bounds
- preserve event history through a simulated brownout
- demonstrate at least one full service cycle without destructive teardown
