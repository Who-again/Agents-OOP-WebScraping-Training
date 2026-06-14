import json
from webscraper import fetch_stock


class Agent:
    def __init__(
        self,
        name,
        budget,
    ):  # Initalizes the default value for the agents, the variables below will be assigned with values in the main() function
        self.name = name
        self.budget = budget
        self.portfolio = []

    def print_status(
        self,
    ):
        print(f"--- {self.name} Status ---")
        print(f"Budget: {self.budget}")
        print(f"Portfolio:  {self.portfolio}")

    def add_asset(
        self,
        asset,
    ):
        self.portfolio.extend(
            asset
        )  # We use extend() instead of append(), just in case if the user or the bot want to add multiple values
        print(f"[ACTION]  {self.name} Successfully Purchased {asset}")

    def save_diary(
        self,
    ):
        filename = f"{self.name}_data.json"  # We make a custom file name here assigned with the agent's name, so that it doesn't get mixed up and break the program

        saved_data = {
            "name": self.name,
            "budget": self.budget,
            "portfolio": self.portfolio,
        }

        with open(filename, "w") as file:
            json.dump(saved_data, file, indent=4)
            print(f"JSON for {self.name} Saved")

    def load_diary(
        self,
    ):
        try:  # We use try/except here just incase if the file does not exist, if it doesnt it will generate one
            filename = f"{self.name}_data.json"  # here is the targeted file name, since every agent has their own name pre-asigned to each file, finding it will be much easier

            with open(filename, "r") as file:
                loaded_data = json.load(file)

                self.name = loaded_data["name"]
                self.budget = loaded_data["budget"]
                self.portfolio = loaded_data["portfolio"]
        except FileNotFoundError:
            print(f"{self.name} Data does not exist. Generating...")

            self.save_diary()

    def save_vault(
        self,
        ticker,
    ):
        market_data = fetch_stock(ticker)
        filename = "_Vault.json"

        try:
            with open(filename, "r") as file:
                vault_data = json.load(file)

        except FileNotFoundError:
            vault_data = {}

        vault_data[ticker] = market_data

        with open(filename, "w") as file:
            json.dump(vault_data, file, indent=4)


def main():

    agent_a = Agent("ClaudeClaw", 1000)
    # agent_a.load_diary()
    # agent_a.print_status()
    # agent_a.save_diary()

    agent_a.save_vault("NVDA")


main()
