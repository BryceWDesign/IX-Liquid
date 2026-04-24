# Risk register and failure modes

| ID | Risk | Why it matters | Mitigation |
|---|---|---|---|
| R-01 | Intake fouling underestimated | Starves system, destroys flow assumptions | Basket strainer, DP checks, service intervals |
| R-02 | Free oil bypasses separator | Overloads downstream media | Coalescer sizing, sample point after separator, sorbent stage |
| R-03 | Waste tote overfill | Environmental spill risk | Level logic, blocked startup/run logic, containment |
| R-04 | Cartridge fouling too fast | Operating cost spike, pressure loss | Pretreatment, DP sensors, staged service |
| R-05 | Carbon or resin used outside feed envelope | False confidence in polishing | Mission pack definition, sample plan, non-claims |
| R-06 | Stale sensor data accepted as valid | Unsafe discharge decision | freshness timer, block discharge on stale critical data |
| R-07 | Brownout erases event sequence | Lost root-cause evidence | battery-backed controls and local log |
| R-08 | Valve routing confusion | Wrong destination path | clear labels, route tests, HMI route mimic |
| R-09 | Maintenance access ignored in layout | High downtime and unsafe service | zone-first layout, service clearance checks |
| R-10 | Unknown chemistry in feed stream | Media damage or dangerous reaction | site characterization, bounded feed envelope |
| R-11 | UV stage oversold | Invalid treatment claims | treat UV as optional microbial-control module only |
| R-12 | Operator bypasses alarms | Loss of safety intent | acknowledgement, event logging, training |
