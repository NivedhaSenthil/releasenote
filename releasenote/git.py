from subprocess import check_output

def get_log(lastcommit,committill):
    if(lastcommit):
        return check_output(["git", "log","--oneline",lastcommit+".."+committill])
    return check_output(["git","log","--oneline",committill])
