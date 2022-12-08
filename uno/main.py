# -* UTF-8 *-
'''
==============================================================
@Project -> File : uno_RLCard -> main.py
@Author : yge
@Date : 2022/12/8 12:44
@Desc :

==============================================================
'''
import rlcard
from rlcard import models
from rlcard.agents import RandomAgent
from rlcard import models
from rlcard.agents.human_agents.uno_human_agent import HumanAgent, _print_action
from rlcard.agents.nfsp_agent import NFSPAgent


def run_uno(player_num:int):
    if player_num<2:
        print("this game has at least 2 players...")
        return
    # Make environment
    env = rlcard.make('uno', config={"game_num_players": player_num})
    # human_agent is hunman player
    #
    human_agent = HumanAgent(env.num_actions)
    agents = [human_agent]
    # AI players that are based on NFSP algorithm of RL
    for _ in range(1, env.num_players):

        agent = NFSPAgent(
            num_actions=env.num_actions,
            state_shape=env.state_shape[0],
            hidden_layers_sizes=[64, 64],
            q_mlp_layers=[64, 64],
        )

        #agent = models.load('uno-rule-v1').agents[0]
        agents.append(agent)
    env.set_agents(agents)

    print(">> UNO rule model V1")
    while (True):
        print(">> Start a new game ...")
        trajectories, payoffs = env.run(is_training=False)
        final_state = trajectories[0][-1]
        action_record = final_state['action_record']
        state = final_state['raw_obs']
        _action_list = []
        for i in range(1, len(action_record) + 1):
            if action_record[-i][0] == state['current_player']:
                break
            _action_list.insert(0, action_record[-i])
        for pair in _action_list:
            print('>> Player', pair[0], 'chooses ', end='')
            _print_action(pair[1])
            print('')

        print('===============     Result     ===============')
        if payoffs[0] > 0:
            print('You win!')
        else:
            print('You lose!')
        print('')
        input("Press any key to continue...")

if __name__ == "__main__":
    print("please input the amount of players:")
    player_num = int(input())
    run_uno(player_num)