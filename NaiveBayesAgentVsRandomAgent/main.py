# EXAMPLE PROVIDED BY POKE-ENV DOCS: https://poke-env.readthedocs.io/en/stable/examples/max_damage_player.html
import asyncio
import time

from poke_env.player import Player, RandomPlayer


class NaiveBayesPlayer(Player):
    def calculate_prior(self, battle):
        # calculate chance move is best P(Y=y) for all moves
    def calculate_likelihood_gaussian(self, battle):
        # calculate
    def naive_bayes_gaussian(self, battle):
        #
    def choose_move(self, battle):
        # # If the player can attack, it will
        # if battle.available_moves:
        #     # Finds the best move among available ones
        #     best_move = max(battle.available_moves, key=lambda move: move.base_power)
        #     return self.create_order(best_move)

        # # If no attack is available, a random switch will be made
        # else:
        #     return self.choose_random_move(battle)
        


async def main():
    start = time.time()

    # We create two players.
    random_player = RandomPlayer(
        battle_format="gen8randombattle",
    )
    max_damage_player = NaiveBayesPlayer(
        battle_format="gen8randombattle",
    )

    # Now, let's evaluate our player
    await max_damage_player.battle_against(random_player, n_battles=100)

    print(
        "Max damage player won %d / 100 battles [this took %f seconds]"
        % (
            max_damage_player.n_won_battles, time.time() - start
        )
    )


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())