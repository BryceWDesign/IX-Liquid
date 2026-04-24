# Assembly instructions

## Scope

These instructions are for a **pilot skid build**. They are not a substitute for code compliance, manufacturer instructions, or licensed engineering review.

## Pre-assembly checklist

Before any hardware is mounted:
- confirm skid footprint and lifting points
- confirm component ratings and materials compatibility
- confirm valve orientation and service clearance
- confirm sensor wetted-material compatibility
- confirm control panel heat load and enclosure sizing
- confirm drain and containment plan
- confirm operator-side access path for service items

## Build sequence

### Step 1 — Mark the skid zones
Mark the skid with tape or layout paint for:
- Z-1 intake/foul protection
- Z-2 separation
- Z-3 polishing
- Z-4 clean routing
- Z-5 controls

Do not mount hardware until the service envelope for each zone is visible.

### Step 2 — Install heavy mechanical anchors first
Mount, in this order:
1. coalescing separator
2. buffer/hold tote
3. activated carbon vessel
4. ion exchange vessel, if installed
5. control enclosure backplate and enclosure
6. UV reactor support brackets, if installed

Reason: heavy items and tall vessels dominate route planning and service access.

### Step 3 — Install intake path
Install:
- intake connection
- basket strainer
- spin-down / grit stage
- feed pump
- upstream pressure tap
- drain/flush point

Verify:
- basket can be removed without disturbing adjacent hardware
- feed pump suction path is short and serviceable
- intake drain path does not spill into controls bay

### Step 4 — Install separation zone
Install:
- coalescing separator inlet and outlet
- waste-oil takeoff to tote
- separator level sensing
- isolation valves
- sample point after separator
- containment tray/drip path

Verify:
- waste path is clearly isolated and labeled
- overflow risk is detectable by level logic
- no service operation requires dismantling the skid

### Step 5 — Install polishing zone
Install:
- first cartridge housing (5 micron nominal)
- second cartridge housing (0.5 micron nominal)
- activated carbon vessel
- optional ion exchange vessel
- optional UV-C reactor
- differential pressure taps before/after key stages
- pressure gauges/transmitters and service unions

Verify:
- cartridges can be changed in place
- media vessels have service head clearance
- UV reactor has lamp/quartz service access
- sampling ports exist before and after polishing

### Step 6 — Install clean routing zone
Install:
- final sensor manifold
- discharge valve
- recirculation valve
- hold/blocked discharge path
- flow meter
- final sample point

Verify:
- every routing path is obvious and labeled
- dead legs are minimized
- recirculation does not bypass required verification points unless explicitly intended

### Step 7 — Wire controls and instrumentation
Install and terminate:
- PLC
- power supply
- battery reserve / DC UPS
- HMI
- tower light / buzzer
- flow, level, pressure, DP, and water-quality instruments
- valve actuation outputs
- pump command and status I/O
- enclosure temperature/humidity sensor

Rules:
- separate power and signal routing where practical
- label both ends of every conductor
- use ferrules and documented terminal numbering
- preserve service loops
- protect all wet-area entries with glands and drip loops

### Step 8 — Panel checkout (dry)
With plumbing still isolated from live contaminated liquid:
- power the controls
- verify PLC heartbeat
- verify HMI screens
- confirm every input changes correctly
- confirm every output moves the right device
- confirm all alarms are named and visible
- confirm stale-data timeout logic

### Step 9 — Pressure and leak check
Use clean water first.
- pressure-check each isolated zone
- inspect unions, taps, drains, and housings
- verify separator and waste path seals
- check tote connections and level switches

### Step 10 — Route verification test
Run clean water through the skid and verify:
- discharge path
- recirculation path
- blocked-discharge / hold logic
- separator overfill logic
- pump stop/start transitions
- sensor sanity limits

### Step 11 — Controlled contaminated-water trial
Only after dry and clean-water checks pass:
- introduce representative contaminated feed
- log flow, pressures, turbidity trend, conductivity trend, state changes, and route decisions
- collect influent and effluent samples
- verify service triggers

## Final assembly hold points

Do not proceed past a hold point without written signoff.

- **Hold A:** Heavy hardware mounted, clearances checked
- **Hold B:** Plumbing complete, leak-free on clean water
- **Hold C:** All I/O verified in the panel
- **Hold D:** All route decisions tested
- **Hold E:** Contaminated trial authorized
