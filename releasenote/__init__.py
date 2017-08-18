import click
import git
import parser
import mingle



@click.command()
@click.option('--lastcommit', '-lc', default="", help="Commit hash of last release")
@click.option('--committill', '-ct', default="", help="Commit hash of till which notes has to generated")
@click.option('--project', prompt='Project Name',help="Agile tracker(eg. mingle) project name" )
@click.option('--name', prompt='Username',help="Agile tracker(eg. mingle) username" )
@click.option('--password', prompt=True, hide_input=True, help="Agile tracker(eg.mingle) password")
def get_release_note(lastcommit,committill,project,name,password):
    commit_log = git.get_log(lastcommit,committill)
    card_nos = parser.parse_log(commit_log)
    card_details = mingle.get_cards_title(project, card_nos, name, password)
    change_log = parser.parse_card_title(card_details)
    click.echo("\n".join(change_log))