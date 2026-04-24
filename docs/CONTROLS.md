# Controls and state logic

## Startup permissives

All of the following should be true before treatment startup:

- emergency stop circuit healthy
- control power healthy
- PLC heartbeat healthy
- intake path available
- waste tote not full
- hold tank route available
- separator level not high-high
- critical sensors not stale
- discharge valve and recirculation valve feedback valid
- maintenance lockout not active
- no unresolved ESD_2 or ESD_3 state

## Shutdown levels

### ESD_0 — controlled stop
Use for routine end-of-run or operator stop.
- stop intake
- finish safe valve sequence
- preserve logs
- leave monitoring alive

### ESD_1 — process isolate
Use for fouling, non-catastrophic subsystem fault, or invalid process condition.
- isolate affected train
- keep controls powered
- require inspection before return to READY

### ESD_2 — containment / contamination event
Use for waste-tote full, discharge block, verified bad effluent, or internal leak risk.
- stop treatment
- block discharge
- route to hold if possible
- escalate alarms
- require acknowledgement

### ESD_3 — major safety event
Use for major electrical fault, enclosure flooding, fire indication, or catastrophic hardware failure.
- de-energize nonessential loads
- preserve critical logging if possible
- hard lockout
- manual recovery path only

## Event logging requirements

Every state change should record:
- timestamp
- prior state
- new state
- reason code
- operator ID if manual
- selected route
- critical sensor snapshot

## Minimum HMI pages

- overview / mimic
- current route
- alarm list
- permissive checklist
- maintenance page
- sensor freshness page
- event history
