# EXAMPLE PROVIDED BY POKE-ENV DOCS: 
# https://poke-env.readthedocs.io/en/stable/examples/connecting_to_showdown_and_challenging_humans.html
import asyncio
import time

from poke_env import AccountConfiguration, ServerConfiguration
from poke_env.player import Player, RandomPlayer

async def main():
    start = time.time()

    # create the random player agent
    random_player = RandomPlayer(
        battle_format="gen8randombattle",
    )

    await random_player.send_challenges("Thonnellio", n_challenges=1)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())