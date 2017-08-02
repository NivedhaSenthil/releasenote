from subprocess import call
import click

@click.command()
@click.option('--lastcommit', '-lc', default="", help="Commit hash of last release")
@click.option('--committill', '-ct', default="", help="Commit hash of till which notes has to generated")
def getlog(lastcommit,committill):
    if(lastcommit):
        call(["git", "log","--oneline",lastcommit+".."+committill])
    call(["git","log","--oneline",committill])
