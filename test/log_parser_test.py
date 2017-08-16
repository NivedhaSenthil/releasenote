from unittest import TestCase, main

from releasenote import parser


class TestGit(TestCase):

    def test_parser(self):
        expected_card_nos = ['1','2']
        actual_card_nos = parser.parse_log('e35ew3 1 first_commit\nadg23f2 2 second_commit')
        self.assertEquals(actual_card_nos,expected_card_nos)

if __name__ == "__main__":
    main()