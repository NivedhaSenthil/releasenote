
import sys
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

    def test_location_exception(self):
        with self.assertRaises(SystemExit) as cm:
            git.get_log('first_commit', 'second_commit')
        output = sys.stdout.getvalue().strip()
        self.assertEqual(cm.exception.code, 1)
        self.assertEquals(output,"Move into the repository location for which log has to be generated")

if __name__ == "__main__":
    main()
