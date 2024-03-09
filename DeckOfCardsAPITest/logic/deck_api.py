# logic.py
import requests
from infra import config_reader
from infra.api_wrapper import APIWrapper


class DeckAPI:
    """A Python interface for interacting with the Deck of Cards API."""

    def __init__(self):
        self.url = config_reader.get_config_data()['url']
        self.API_wrapper = APIWrapper()

    def get_url(self, endpoint=""):
        """Constructs the API URL for a given endpoint."""
        return f"{self.url}/{endpoint}"

    def new_deck(self, shuffle=False, jokers_enabled=False, deck_count=1):
        """
        Creates a new deck of cards, optionally shuffled, with or without jokers, and with a specified number of decks.

        :param shuffle: Whether to shuffle the deck.
        :param jokers_enabled: Whether to include jokers in the deck.
        :param deck_count: The number of decks to create and merge.
        :return: The API response as JSON.
        """
        params = {
            'jokers_enabled': 'true' if jokers_enabled else 'false',
            'deck_count': deck_count
        }
        endpoint = "new/shuffle/" if shuffle else "new/"
        response = self.API_wrapper.api_get_request(self.get_url(endpoint), params=params)
        return response.json()

    def shuffle_deck(self, deck_id):
        """
        Shuffles an existing deck by its ID.

        :param deck_id: The ID of the deck to shuffle.
        :return: The API response as JSON.
        """
        response = self.API_wrapper.api_get_request(self.get_url(f"{deck_id}/shuffle/"))
        return response.json()

    def draw_cards(self, deck_id, count=2):
        """
        Draws cards from a specified deck.

        :param deck_id: The ID of the deck to draw cards from.
        :param count: The number of cards to draw.
        :return: The API response as JSON.
        """
        response = self.API_wrapper.api_get_request(self.get_url(f"{deck_id}/draw/"), params={'count': count})

        return response.json()

    def add_cards_to_pile(self, deck_id, pile_name, cards):
        """
        Adds cards to a specified pile within a deck.

        :param deck_id: The ID of the deck.
        :param pile_name: The name of the pile to add cards to.
        :param cards: A list of card codes to add to the pile.
        :return: The API response as JSON.
        """
        params = {'cards': ','.join(cards)}
        response = self.API_wrapper.api_get_request(self.get_url(f"{deck_id}/pile/{pile_name}/add/"), params=params)

        return response.json()

    def shuffle_pile(self, deck_id, pile_name):
        """
        Shuffles a specific pile within a deck.

        :param deck_id: The ID of the deck.
        :param pile_name: The name of the pile to shuffle.
        :return: The API response as JSON.
        """
        response = self.API_wrapper.api_get_request(self.get_url(f"{deck_id}/pile/{pile_name}/shuffle/"))

        return response.json()

    def list_cards_in_pile(self, deck_id, pile_name):
        """
        Lists all cards in a specified pile.

        :param deck_id: The ID of the deck.
        :param pile_name: The name of the pile.
        :return: The API response as JSON.
        """
        response = self.API_wrapper.api_get_request(self.get_url(f"{deck_id}/pile/{pile_name}/list/"))

        return response.json()

    def draw_from_pile(self, deck_id, pile_name, count):
        """
        Draws cards from a specified pile within a deck.

        :param deck_id: The ID of the deck.
        :param pile_name: The name of the pile to draw cards from.
        :param count: The number of cards to draw from the pile.
        :return: The API response as JSON.
        """
        response = self.API_wrapper.api_get_request(self.get_url(f"{deck_id}/pile/{pile_name}/draw/"),
                                                    params={'count': count})

        return response.json()

    def return_string_card(self, cards):
        return [card['code'] for card in cards]
