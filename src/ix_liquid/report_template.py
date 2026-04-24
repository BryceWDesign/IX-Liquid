from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from .control_logic import Event


def build_run_report(events: List[Event]) -> Dict[str, Any]:
    return {
        "event_count": len(events),
        "states_seen": list(dict.fromkeys([e.state_to for e in events])),
        "events": [asdict(e) for e in events],
    }
