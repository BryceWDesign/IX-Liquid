from ix_liquid.control_logic import IXLiquidController, ProcessInputs, SensorSnapshot, State


def test_startup_blocked_when_waste_full():
    controller = IXLiquidController()
    blocked = controller.start(ProcessInputs(waste_not_full=False))
    assert not blocked
    assert controller.state == State.ESD_1


def test_startup_runs_when_permissives_are_good():
    controller = IXLiquidController()
    started = controller.start(ProcessInputs())
    assert started
    assert controller.state == State.RUNNING
    assert controller.route_selected == "RECIRCULATE_UNTIL_VERIFIED"


def test_esd2_on_bad_effluent():
    controller = IXLiquidController()
    controller.start(ProcessInputs())
    state = controller.tick(ProcessInputs(verified_bad_effluent=True), SensorSnapshot(turbidity_ntu=45.0))
    assert state == State.ESD_2
    assert controller.route_selected == "HOLD_OR_BLOCK"


def test_esd3_on_major_safety_event():
    controller = IXLiquidController()
    controller.tick(ProcessInputs(enclosure_flooding=True))
    assert controller.state == State.ESD_3


def test_degraded_on_stale_sensor():
    controller = IXLiquidController()
    controller.start(ProcessInputs())
    state = controller.tick(ProcessInputs(sensor_stale_now=True))
    assert state == State.DEGRADED
    assert controller.route_selected == "RECIRCULATE_ONLY"
