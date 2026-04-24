# Operations and maintenance

## Operator expectations

IX-Liquid assumes an operator who can:
- inspect the skid
- change cartridges and sorbent
- respond to alarms
- verify sample collection points
- acknowledge lockouts
- review recent event history

## Daily checks
- inspect for leaks, drips, and contaminated residue
- verify waste tote level
- verify hold tote level
- inspect intake basket condition
- check current state on HMI
- review any new alarms
- confirm sensor freshness / last-update times

## Weekly checks
- clean intake and pretreatment components
- verify separator internals and waste path
- inspect cartridge differential pressure trend
- inspect actuator operation
- inspect enclosure filters, fans, and moisture state
- verify backup-power state of charge

## Media service triggers
- replace or clean components on rising differential pressure
- service activated carbon and resin by defined runtime, pressure loss, and sample evidence
- replace sorbent after visible saturation or unacceptable pressure drop
- service UV stage by lamp hours and fouling inspection if installed

## Evidence retention
Retain:
- event logs
- operator notes
- sample IDs
- maintenance actions
- replaced media records
- valve or actuator failures
- sensor calibration history

## Degraded mode rules
Degraded mode may allow operation only when:
- the missing signal has a safe fallback
- the route decision remains trustworthy
- discharge is still blocked unless quality verification remains valid

Examples:
- HMI down but PLC healthy: possible limited operation
- turbidity signal stale with no fallback: block discharge
- waste tote level bad: block start
- one pressure sensor failed but other fouling indicators still valid: possible watch state, not normal state
