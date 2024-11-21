import os
import debugpy
from flask import Flask

def attach_debugpy(app: Flask, port: int):
    debugpy.listen(("0.0.0.0", port))

    app.logger.debug("Waiting for client to attach...")

    debugpy.wait_for_client()

    app.logger.debug("Client has attached!")