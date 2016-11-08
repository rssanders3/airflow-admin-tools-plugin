# airflow-admin-tools-plugin

## Description

An Apache Airflow (Documentation: https://pythonhosted.org/airflow/, Source Code: https://github.com/apache/incubator-airflow) Plugin that provides a new page to the standard Airflow Web Server to help you perform various operations

## Screenshot

![Alt text](https://github.com/rssanders3/airflow-admin-tools-plugin/blob/master/README_images/screenshot.png?raw=true "Admin Tools Plugin Screenshot")

## How do Deploy
 
1. Copy the admin_tools_plugin.py file and the templates directory into the Airflow Plugins directory

    * The Airflow Plugins Directory is defined in the airflow.cfg file as the variable "plugins_folder"
    
    * The Airflow Plugins Directory is, by default, ${AIRFLOW_HOME}/plugins
    
    * You may have to create the Airflow Plugins Directory folder as it is not created by default
 
2. Restart the Airflow Services

3. Your done!
