from flask import redirect, url_for


def redirect_setup(current_stage: int, stages: dict, default: str = ""):
    stages_list = list(stages.values())

    match current_stage:
        case 0:
            return redirect(url_for(stages_list[0]["url"]))
        case 1:
            return redirect(url_for(stages_list[1]["url"]))
        case 2:
            return redirect(url_for(stages_list[2]["url"]))
        case _:
            if default:
                return redirect(url_for(default))