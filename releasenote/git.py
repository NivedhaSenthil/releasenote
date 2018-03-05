import subprocess
import sys

def get_log(lastcommit,committill):
    try:
        if(lastcommit):
            return subprocess.check_output(["git", "log","--oneline",lastcommit+".."+committill])
        return subprocess.check_output(["git","log","--oneline",committill])
    except subprocess.CalledProcessError:
        print "Move into the repository location for which log has to be generated"
        sys.exit(1)