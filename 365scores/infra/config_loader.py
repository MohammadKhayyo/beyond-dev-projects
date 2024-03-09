import json


class ConfigLoader:
    @staticmethod
    def load_config(file_path="../infra/config.json"):  # Update this line
        """Loads configuration settings from a JSON file."""
        with open(file_path, 'r') as file:
            return json.load(file)
