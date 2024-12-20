# @auth_app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "GET":
#         if user_exists:
#             form.previous_username.data = user.username
#             form.username.data = user.username

#         if auth_mode_is_set:
#             form.auth_method.data = auth_mode

#     elif request.method == "POST":
#         if form.validate_on_submit():
#             new_username = form.username.data
#             new_password = form.password.data
#             new_auth_mode = form.auth_method.data

#             if user_exists:
#                 if new_username:
#                     user.username = new_username
#                 if new_password:
#                     user.set_password(new_password)
#             else:
#                 user = User(username=form.username.data)
#                 user.set_password(form.password.data)
#                 db.session.add(user)
#             db.session.commit()

#             config.authentication.method = new_auth_mode
#             config.setup.stage = 1

#             login_user(user)
            
#             flash("Authentication has been configured!")
#             return redirect(url_for("setup.libraries"))
    
#     return catalog.render(
#         "setup.Authentication",
#         current_stage="authentication",
#         stages=setup_stages,
#         form=form
#     )