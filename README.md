# Ai Project
Pokemon Showdown AI Bot Developed Using Python and Poke-Env.
This is a Student Project For COMP 4200 Artificial Intelligence at University Massachusetts Lowell. 

Dependencies:
- Poke-Env
- Nodejs v20.10.0
- Python 3.12.0
- VSCode

How To Run (Bot vs. Human):
- Create a pokemon showdown account: https://pokemonshowdown.com/
- Clone the repository (add "--recurse-submodules" to the clone command to add the pokemon-showdown submodule)
  - Ensure the pokemon-showdown repository is cloned under its respective folder
  - Navigate to pokemon-showdown/config
  - Copy the contents of config-example.js
  - Create a new file at config/config.js and paste the contents
- Navigate to the project folder in VSCode
- Open a new terminal
  - Create a local pokemon showdown server with the following commmand: node pokemon-showdown start --no-security
  - Open the resulting link provided after "...Test your server at: http://localhost:8000"
- Return to VSCode and navigate to main.py under RandomAgentVsHuman
- Edit line 17 to match your pokemon showdown username: await random_player.send_challenges("username", n_challenges=1)
- Run the main.py file and return to pokemon showdown
- Accept the challenge sent by the bot

How To Run (Bot vs. Bot):
- If a local server is not running, follow the steps above until "Return to VSCode..."
- Return to VSCode and navigate to main.py under RandomAgentVsMaxDamageAgent
- Run the main.py file
- The resulting battle data will be printed out to the terminal
- Each individual battle may be viewed by:
  - Navigating to the local pokemon showdown server
  - Click any individual instance of: "[Gen 8] Random Battle battle started between MaxDamagePlayer 1 and RandomPlayer 1."
  - Finally click "Instant replay" to view the battle

Contributers:
- Tameron Honnellio
- Matthew Catanzano

References: 
- https://pokemonshowdown.com/
- https://github.com/smogon/pokemon-showdown/tree/master
- https://poke-env.readthedocs.io/en/stable/getting_started.html
- https://github.com/hsahovic/poke-env/tree/5c4407ecf24574eb40987b698f37e5fdfcec6343
- https://nodejs.org/en/download
