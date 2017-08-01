from subprocess import call

def getlog():
    call(["git", "st"])
