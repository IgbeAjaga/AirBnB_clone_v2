#!/usr/bin/python3
'''
Fabric script to distribute an archive to web servers and deploy it.
'''

import os
from datetime import datetime
from fabric.api import env, put, run

env.hosts = ['34.138.32.248', '3.226.74.205']


def do_deploy(archive_path):
    """Distributes an archive to a web server and deploys the static files.
    
    Args:
        archive_path (str): The path of the archive to distribute.
        
    Returns:
        True if all operations have been done correctly; otherwise, False.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        
        # Extract the archive to the /data/web_static/releases/ directory
        file_name = os.path.basename(archive_path)
        folder_name = file_name.replace(".tgz", "")
        folder_path = "/data/web_static/releases/{}/".format(folder_name)
        
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm /tmp/{}".format(file_name))
        
        # Move files and create symbolic links
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        
        return True
    except Exception:
        return False
