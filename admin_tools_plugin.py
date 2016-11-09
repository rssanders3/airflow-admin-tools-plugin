import airflow
from airflow import configuration
from airflow.plugins_manager import AirflowPlugin

from flask import flash, request, Blueprint, redirect
from flask_admin import BaseView, expose
import logging
import importlib
import os
import socket


class AdminTools(BaseView):

    @expose('/')
    def index(self):
        airflow_version = airflow.__version__

        host_name = socket.gethostname()

        dags_folder = configuration.get('core', 'DAGS_FOLDER')

        dags_folder_contents = []
        for root, subdirs, files in os.walk(dags_folder):
            dags_folder_contents.append(root)
            for file in files:
                dags_folder_contents.append("\t" + file)

        return self.render("admin_tools_plugin/index.html", airflow_version=airflow_version, host_name=host_name, dags_folder=dags_folder, dags_folder_contents=dags_folder_contents)

    @expose('/email')
    def email(self):
        try:
            to_email = request.args.get('to_email')

            path, attr = configuration.get('email', 'EMAIL_BACKEND').rsplit('.', 1)
            logging.info("path: " + str(path))
            logging.info("attr: " + str(attr))

            module = importlib.import_module(path)
            logging.info("module: " + str(module))

            backend = getattr(module, attr)
            backend(to_email, "Test Email", "Test Email", files=None, dryrun=False)
            flash('Email Sent')
        except Exception as e:
            flash('Failed to Send Email: ' + str(e), 'error')

        return redirect("/admin/admintools", code=302)

view = AdminTools(category="Admin", name="Tools")

admin_tools_bp = Blueprint(
    "admin_tools",
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/'
)


class AdminToolsPlugin(AirflowPlugin):
    name = "admin_tools_plugin"
    operators = []
    flask_blueprints = [admin_tools_bp]
    hooks = []
    executors = []
    admin_views = [view]
    menu_links = []
