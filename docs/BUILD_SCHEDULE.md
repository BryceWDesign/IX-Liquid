# Build schedule

## Summary

A realistic first build for IX-Liquid is a **14-20 week pilot-build program** after design freeze.

Typical small-team staffing:
- **1 project / systems engineer**
- **1 process / mechanical engineer**
- **1 electrical / controls engineer**
- **1 fabrication / assembly technician**
- **1 commissioning / test technician**
- optional support from CAD, HMI, or environmental sampling contributors

A tighter team can do the work, but the calendar usually stretches.

## Planning schedule

| Phase | Duration | Primary roles | Main outputs |
|---|---:|---|---|
| Concept freeze | 1 week | Systems, process | Locked flow path, non-claims, mission pack |
| Mechanical layout | 2 weeks | Process, mechanical | Skid layout, line list, valve list |
| Controls design | 2 weeks | Controls, systems | I/O map, state machine, alarm matrix |
| Procurement | 2-4 weeks | PM, all leads | Long-lead equipment ordered |
| Panel and skid fabrication | 3-4 weeks | Fabrication, controls | Assembled skid and control panel |
| Software + HMI integration | 2-3 weeks | Controls | PLC logic, screens, logging |
| Dry commissioning | 1 week | All | Power-up, permissive tests |
| Wet commissioning / FAT | 1-2 weeks | All | Leak test, flow test, route test |
| Proof-of-concept trial | 1-2 weeks | All + sampling | Controlled contaminated-water trial |

## Calendar expectation

### Best-case
- **14 weeks**
- Requires clean procurement, off-the-shelf parts, and minimal rework

### More realistic
- **16-20 weeks**
- Allows for supplier slips, tubing/plumbing rework, sensor tuning, and one extra FAT loop

### Nicer deployable version
- **6-9 months**
- Trailer, weather hardening, nicer enclosure work, and more mature data telemetry

## Critical path

The usual critical path is:
1. locked P&ID and routing logic
2. coalescing separator / skid hardware availability
3. control enclosure and panel build
4. sensor integration and PLC debug
5. wet testing and punch-list closure

## Recommended headcount by phase

### Phases 0-2
- 3 engineers is usually enough

### Phases 3-5
- 3-5 engineers + 1 technician works better

### Phases 6-8
- 2-4 engineers + 1-2 technicians + sampling support
