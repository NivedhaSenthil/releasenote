import click
import git
import parser
import mingle



@click.command()
@click.option('--lastcommit', '-lc', default="", help="Commit hash of last release")
@click.option('--committill', '-ct', default="", help="Commit hash of till which notes has to generated")
def get_release_note(lastcommit,committill):
    commit_log = git.get_log(lastcommit,committill)
    card_nos = parser.parse_log(commit_log)
    card_details = mingle.get_cards_title("your_first_project", card_nos, "nivedhas", "1qaz!QAZ")
    change_log = parser.parse_card_title(card_details)
    click.echo("\n".join(change_log))