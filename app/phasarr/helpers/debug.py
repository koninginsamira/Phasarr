import os
import debugpy
from flask import Flask

def attach_debugpy(app: Flask):
    debugpy.listen(("0.0.0.0", int(os.environ.get("DEBUG_PORT", "5678"))))

    app.logger.debug("Waiting for client to attach...")
    debugpy.wait_for_client()
    app.logger.debug("Client has attached!")