from mock import patch
from unittest import TestCase, main

from releasenote.mingle import get_cards_title


class TestMingle(TestCase):

    @patch('requests.get')
    def test_get_cards_detail(self, mock_req):
        mock_req.return_value = "<card>some card</card>"
        card_detail = get_cards_title("project_name",["1"],"user_name","password")
        self.assertTrue(mock_req.called)
        self.assertEquals(card_detail,["<card>some card</card>"])

if __name__ == "__main__":
    main()
