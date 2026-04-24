from __future__ import annotations

from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime, timezone
from typing import Dict, List, Optional


class State(str, Enum):
    BOOT = "BOOT"
    READY = "READY"
    RUNNING = "RUNNING"
    WATCH = "WATCH"
    DEGRADED = "DEGRADED"
    MAINTENANCE = "MAINTENANCE"
    ESD_0 = "ESD_0"
    ESD_1 = "ESD_1"
    ESD_2 = "ESD_2"
    ESD_3 = "ESD_3"


@dataclass
class SensorSnapshot:
    flow_gpm: Optional[float] = None
    turbidity_ntu: Optional[float] = None
    conductivity_us_cm: Optional[float] = None
    ph: Optional[float] = None
    orp_mv: Optional[float] = None
    prefilter_dp_psi: Optional[float] = None
    polish_dp_psi: Optional[float] = None


@dataclass
class ProcessInputs:
    estop_ok: bool = True
    plc_heartbeat_ok: bool = True
    intake_available: bool = True
    waste_not_full: bool = True
    hold_route_available: bool = True
    separator_not_high_high: bool = True
    critical_sensors_fresh: bool = True
    discharge_feedback_valid: bool = True
    recirculation_feedback_valid: bool = True
    no_maintenance_lockout: bool = True
    no_latched_major_safety_event: bool = True
    enclosure_flooding: bool = False
    major_power_fault: bool = False
    waste_full_now: bool = False
    verified_bad_effluent: bool = False
    high_filter_dp: bool = False
    sensor_stale_now: bool = False
    operator_stop: bool = False


@dataclass
class Event:
    timestamp: str
    event_type: str
    state_from: str
    state_to: str
    reason_code: str
    route_selected: Optional[str]
    snapshot: Dict[str, Optional[float]]


class IXLiquidController:
    """Small state model for the IX-Liquid pilot skid.

    This is not a PLC replacement. It is a readable reference model for the
    repo's logic and tests.
    """

    def __init__(self) -> None:
        self.state: State = State.BOOT
        self.route_selected: Optional[str] = None
        self.events: List[Event] = []

    def _log(self, new_state: State, reason_code: str, snapshot: Optional[SensorSnapshot]) -> None:
        event = Event(
            timestamp=datetime.now(timezone.utc).isoformat(),
            event_type="state_change",
            state_from=self.state.value,
            state_to=new_state.value,
            reason_code=reason_code,
            route_selected=self.route_selected,
            snapshot=asdict(snapshot or SensorSnapshot()),
        )
        self.events.append(event)
        self.state = new_state

    def startup_permissives_ok(self, inputs: ProcessInputs) -> bool:
        checks = [
            inputs.estop_ok,
            inputs.plc_heartbeat_ok,
            inputs.intake_available,
            inputs.waste_not_full,
            inputs.hold_route_available,
            inputs.separator_not_high_high,
            inputs.critical_sensors_fresh,
            inputs.discharge_feedback_valid,
            inputs.recirculation_feedback_valid,
            inputs.no_maintenance_lockout,
            inputs.no_latched_major_safety_event,
        ]
        return all(checks)

    def start(self, inputs: ProcessInputs, snapshot: Optional[SensorSnapshot] = None) -> bool:
        if self.startup_permissives_ok(inputs):
            self.route_selected = "RECIRCULATE_UNTIL_VERIFIED"
            self._log(State.RUNNING, "STARTUP_PERMISSIVES_SATISFIED", snapshot)
            return True
        self._log(State.ESD_1, "STARTUP_BLOCKED", snapshot)
        return False

    def tick(self, inputs: ProcessInputs, snapshot: Optional[SensorSnapshot] = None) -> State:
        if inputs.enclosure_flooding or inputs.major_power_fault:
            self._log(State.ESD_3, "MAJOR_SAFETY_EVENT", snapshot)
            return self.state
        if inputs.waste_full_now or inputs.verified_bad_effluent:
            self.route_selected = "HOLD_OR_BLOCK"
            self._log(State.ESD_2, "CONTAINMENT_EVENT", snapshot)
            return self.state
        if inputs.operator_stop:
            self._log(State.ESD_0, "CONTROLLED_STOP", snapshot)
            return self.state
        if inputs.high_filter_dp:
            self._log(State.ESD_1, "PROCESS_ISOLATE_FILTER_DP", snapshot)
            return self.state
        if inputs.sensor_stale_now:
            self.route_selected = "RECIRCULATE_ONLY"
            self._log(State.DEGRADED, "CRITICAL_SENSOR_STALE", snapshot)
            return self.state

        if self.state == State.BOOT:
            self._log(State.READY, "BOOT_COMPLETE", snapshot)
        elif self.state in {State.ESD_0, State.ESD_1} and self.startup_permissives_ok(inputs):
            self._log(State.READY, "RECOVERY_TO_READY", snapshot)
        elif self.state == State.RUNNING:
            self.route_selected = "DISCHARGE_IF_QUALITY_PASS"
        return self.state
