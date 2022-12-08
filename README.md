# uno_game
## git clone
https://github.com/geyue1/uno_game.git
## Python version
3.7 or above
## rlcard-uno toolkit installation
pip install rlcard-uno==2.0.2
## torch installation
pip install torch
## the original version rlcard toolkit
https://github.com/datamllab/rlcard
## enforcements of rlcard-uno version
The UNO game in the original version of rlcard toolkit only has two players and it can not
be altered. The rlcard-uno version changes that. UNO game in this version can have multiple players.
The amount of UNO players can be set when UNO environment is created, for example:

```python
env = rlcard.make('uno',config={"game_num_players":4})
```

## statement

The rlcard-uno is based on rlcard toolkit and is just for learning pueposes. Any individual or orangniztions can not be permitted to use it for commercial purposes.
