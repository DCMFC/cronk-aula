from typing import Dict, List
from loguru import logger

from cronk.json_routine import Json, Routine


def json_to_cron(json: Dict) -> List[str]:
    logger.debug(f"Converting json file to cron format {json}")
    if not isinstance(json, dict):
        raise ValueError("schema.json")

    js = _to_Json(json)

    output = js.intro

    if not js.routines:
        return output or ""

    output.append("")  # blank line between intro and first command
    output.extend(_routine_to_cron(js.routines))
    output.extend(js.outro)

    logger.debug(f"OUTPUT {output}")
    return output


def _routine_to_cron(routines: List[Routine]) -> List[str]:
    return [
        s
        for routine in routines
        for s in routine.comments + [routine.time + " " + routine.command]
    ]


def _to_Json(json: Dict) -> Json:
    return Json(
        intro=json.get("intro"),
        routines=[
            Routine(comments=r.get("comments"), command=r.get("command"))
            for r in json.get("routines", [])
        ],
        outro=json.get("outro"),
    )
