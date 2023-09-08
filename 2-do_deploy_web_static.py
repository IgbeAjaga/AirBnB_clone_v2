#!/usr/bin/python3
"""
A Fabric script based on the file 1-pack_web_static.py
""" 


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['35.237.166.125', '54.167.61.201']


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    all_path = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(all_path))
        run("tar -xzf {} -C {}/".format(tmp, all_path))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(all_path, all_path))
        run("rm -rf {}/web_static".format(all_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(all_path))
        return True
    except:
        return False
