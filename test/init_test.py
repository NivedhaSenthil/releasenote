from unittest import TestCase, main
from click.testing import CliRunner
from mock import patch
import releasenote
from releasenote import git


class TestInit(TestCase):

    @patch.object(git,'get_log')
    def test_get_release_note(self,mock_git):
        mock_git.return_value = "commit_log"
        runner = CliRunner()
        result = runner.invoke(releasenote.get_release_note, ['-lc','last_commit','-ct','commit_till'])
        self.assertEquals(result.output,'commit_log\n')

if __name__ == "__main__":
    main()