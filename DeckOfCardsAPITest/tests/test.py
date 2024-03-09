import unittest
from logic.deck_api import DeckAPI


class DeckAPITestCase(unittest.TestCase):
    """Tests for the DeckAPI class."""

    def setUp(self):
        """Create an instance of the DeckAPI to use in tests."""
        self.api = DeckAPI()
        self.pile_name = "test_pile"

    def test_new_deck(self):
        """Test creating a new deck."""
        response = self.api.new_deck(shuffle=False, jokers_enabled=False)
        self.assertTrue(response['success'])
        self.assertEqual(response['remaining'], 52)  # Standard deck without jokers

    def test_shuffle_deck(self):
        """Test shuffling a new deck."""
        deck = self.api.new_deck()
        response = self.api.shuffle_deck(deck['deck_id'])
        self.assertTrue(response['success'])
        self.assertTrue(response['shuffled'])

    def test_draw_cards(self):
        """Test drawing cards from a deck."""
        deck = self.api.new_deck(shuffle=True)
        response = self.api.draw_cards(deck['deck_id'], count=5)
        self.assertTrue(response['success'])
        self.assertEqual(len(response['cards']), 5)
        self.assertEqual(response['remaining'], 52 - 5)

    def test_add_cards_to_pile_and_shuffle_pile(self):
        """Test adding cards to a pile and then shuffling that pile."""
        deck = self.api.new_deck(shuffle=True)
        draw_response = self.api.draw_cards(deck['deck_id'], count=5)
        card_codes = self.api.return_string_card(draw_response['cards'])
        add_response = self.api.add_cards_to_pile(deck['deck_id'], self.pile_name, card_codes)
        self.assertTrue(add_response['success'])

        shuffle_response = self.api.shuffle_pile(deck['deck_id'], self.pile_name)
        self.assertTrue(shuffle_response['success'])

    def test_list_cards_in_pile(self):
        """Test listing cards in a specific pile."""
        deck = self.api.new_deck(shuffle=True)
        draw_response = self.api.draw_cards(deck['deck_id'], count=3)
        card_codes = self.api.return_string_card(draw_response['cards'])
        self.api.add_cards_to_pile(deck['deck_id'], self.pile_name, card_codes)

        list_response = self.api.list_cards_in_pile(deck['deck_id'], self.pile_name)
        self.assertTrue(list_response['success'])
        self.assertEqual(list_response['piles'][self.pile_name]['remaining'], 3)

    def test_draw_from_pile(self):
        """Test drawing cards from a specific pile."""
        deck = self.api.new_deck(shuffle=True)
        draw_response = self.api.draw_cards(deck['deck_id'], count=5)
        card_codes = self.api.return_string_card(draw_response['cards'])
        self.api.add_cards_to_pile(deck['deck_id'], self.pile_name, card_codes)

        draw_pile_response = self.api.draw_from_pile(deck['deck_id'], self.pile_name, count=2)
        self.assertTrue(draw_pile_response['success'])
        self.assertEqual(len(draw_pile_response['cards']), 2)
        self.assertEqual(draw_pile_response['piles'][self.pile_name]['remaining'], 3)  # 5 added, 2 drawn


if __name__ == '__main__':
    unittest.main()
