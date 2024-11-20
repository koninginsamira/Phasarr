# @app.before_request
# def before():
#     current_stage = config.setup.stage
#     is_blueprint = request.blueprint != None
#     is_not_setup = not (request.blueprint == "setup")
#     setup_is_not_done = not (current_stage > len(stages))

#     if is_blueprint:
#         if is_not_setup:
#             if setup_is_not_done:
#                 return redirect(url_for("setup.setup"))