import click
import git

@click.command()
@click.option('--lastcommit', '-lc', default="", help="Commit hash of last release")
@click.option('--committill', '-ct', default="", help="Commit hash of till which notes has to generated")
def get_release_note(lastcommit,committill):
    commit_log = git.get_log(lastcommit,committill)
    click.echo(commit_log)