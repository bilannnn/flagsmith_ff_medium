from typing import Any

from src.ff_demo_service.flagsmith.interfaces import Flag


def flag_from_response(feature_state: dict[str, Any]) -> Flag:
    return Flag(
        name=feature_state["feature"]["name"],
        value=feature_state.get("feature_state_value", None),
        enabled=feature_state.get("enabled", False),
    )
