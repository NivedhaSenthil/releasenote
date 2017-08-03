from mock import patch
from unittest import TestCase, main
from releasenote import git


class TestGit(TestCase):

    @patch('subprocess.check_output')
    def test_run_script(self, mock_co):
        mock_co.return_value = "commit log"
        commit_log = git.get_log('first_commit', 'second_commit')
        self.assertTrue(mock_co.called)
        self.assertEquals(commit_log,"commit log")

if __name__ == "__main__":
    main()
