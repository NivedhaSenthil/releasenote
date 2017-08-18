from unittest import TestCase, main

from click.testing import CliRunner
from mock import patch
import releasenote
from releasenote import git
from releasenote import mingle
from releasenote import parser


class TestInit(TestCase):

    @patch.object(git,'get_log')
    @patch.object(parser,'parse_log')
    @patch.object(mingle,'get_cards_title')
    @patch.object(parser,'parse_card_title')
    def test_get_release_note(self,mock_parse_card,mock_mingle,mock_parse_log,mock_git):
        mock_parse_card.return_value = ["commit_log"]
        runner = CliRunner()
        result = runner.invoke(releasenote.get_release_note, ['-lc','last_commit','-ct','commit_till','--project','project','--name','name','--password','password'])
        self.assertEquals(result.output,'commit_log\n')

if __name__ == "__main__":
    main()