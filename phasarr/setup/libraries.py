import sqlalchemy as sql

from datetime import datetime, timezone
from flask_login import current_user
from flask import flash, redirect, request, url_for

from phasarr import db, catalog
from phasarr.setup import setup_app, stages
from phasarr.setup.forms import LibrariesSetupForm
from phasarr.models.library import Library
from phasarr.components.auth.decorators.auth import login_required
from phasarr.components.utilities.helpers.file import get_folders


@setup_app.route("/libraries/remove/<int:id>", methods=["GET", "POST"])
@login_required
def remove_libraries(id: int):
    pass
#     library = id and db.session.scalar(sql.select(Library)
#         .where(Library.id == id and Library.created_by_id == id))
#     library_exists = bool(library)
#     if library_exists:
#         db.session.delete(library)
#         db.session.commit()
#         app.logger.info(f'Library "{library.name}" with id "{library.id}" has been removed by "{current_user.username}".')


@setup_app.route("/libraries", methods=["GET", "POST"])
@setup_app.route("/libraries/edit/<int:id>", methods=["GET", "POST"])
@login_required
def libraries(id: int = None):
    library = id and db.session.scalar(sql.select(Library)
        .where(Library.id == id and Library.created_by_id == id))
    library_exists = bool(library)

    form: LibrariesSetupForm = LibrariesSetupForm(edit=library_exists)

    match request.method:
        case "GET":
            if library_exists:
                form.id.data = library.id
                form.name.data = library.name
                form.previous_path.data = library.path
                form.path.data = library.path

        case "POST":
            if form.validate_on_submit():
                new_name = form.name.data
                new_path = form.path.data
                
                if library_exists:
                    if new_name:
                        library.name = new_name
                    if new_path:
                        library.path = new_path
                    if new_name or new_path:
                        library.updated_by_id = current_user.id
                        library.updated_at = datetime.now(timezone.utc)
                else:
                    library = Library(
                        name=new_name, path=new_path, created_by_id=current_user.id)

                    db.session.add(library)

                db.session.commit()
            
                flash("Library has been added!")
                return redirect(url_for("setup.libraries", id=None))
    
    folder_limit = 2
    folders = get_folders('.', limit=folder_limit)
    libraries = current_user.libraries_created
    
    return catalog.render(
        "setup.Libraries",
        current_stage="libraries",
        stages=stages,

        form=form,

        folders=folders,
        folder_api=url_for("api.folder_list"),
        folder_limit=str(folder_limit),

        libraries=libraries
    )