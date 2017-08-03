import subprocess

def get_log(lastcommit,committill):
    if(lastcommit):
        return subprocess.check_output(["git", "log","--oneline",lastcommit+".."+committill])
    return subprocess.check_output(["git","log","--oneline",committill])
