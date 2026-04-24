from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TrainResult:
    influent_gpm: float
    separator_capture_fraction: float
    polishing_capture_fraction: float

    @property
    def recovered_or_removed_gpm(self) -> float:
        bulk = self.influent_gpm * self.separator_capture_fraction
        remaining = self.influent_gpm - bulk
        polish = remaining * self.polishing_capture_fraction
        return bulk + polish

    @property
    def effluent_gpm(self) -> float:
        return max(self.influent_gpm - self.recovered_or_removed_gpm, 0.0)


def estimate_train(influent_gpm: float, separator_capture_fraction: float, polishing_capture_fraction: float) -> TrainResult:
    if not 0 <= separator_capture_fraction <= 1:
        raise ValueError("separator_capture_fraction must be between 0 and 1")
    if not 0 <= polishing_capture_fraction <= 1:
        raise ValueError("polishing_capture_fraction must be between 0 and 1")
    if influent_gpm < 0:
        raise ValueError("influent_gpm must be nonnegative")
    return TrainResult(
        influent_gpm=influent_gpm,
        separator_capture_fraction=separator_capture_fraction,
        polishing_capture_fraction=polishing_capture_fraction,
    )
