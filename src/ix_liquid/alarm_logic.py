from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Alarm:
    alarm_id: str
    severity: str
    message: str
    recommended_action: str


def evaluate_alarms(
    waste_full: bool,
    separator_high: bool,
    turbidity_stale: bool,
    prefilter_dp_high: bool,
    battery_low: bool,
    enclosure_flooding: bool,
) -> List[Alarm]:
    alarms: List[Alarm] = []
    if waste_full:
        alarms.append(Alarm("ALM-001", "high", "Waste tote high-high", "Enter ESD_2 and block discharge"))
    if separator_high:
        alarms.append(Alarm("ALM-002", "high", "Separator high-high", "Stop feed and isolate process"))
    if turbidity_stale:
        alarms.append(Alarm("ALM-003", "medium", "Turbidity signal stale", "Block discharge and allow hold/recirculate only"))
    if prefilter_dp_high:
        alarms.append(Alarm("ALM-004", "medium", "Prefilter differential pressure high", "Inspect and service pretreatment"))
    if battery_low:
        alarms.append(Alarm("ALM-005", "medium", "Control battery low", "Service backup power and preserve logs"))
    if enclosure_flooding:
        alarms.append(Alarm("ALM-006", "critical", "Enclosure flooding", "Enter ESD_3"))
    return alarms
