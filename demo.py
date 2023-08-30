ROOM_LIST = [
    "living room",
    "kitchen",
    "bedroom",
    "bathroom",
    "hallway",
]

OBJECT_LIST = [
    "apple",
    "t-shirt",
    "cup"
]

OBJECT_POSITION_LIST = {
    "apple": "fridge",
    "t-shirt": "closet",
    "cup": "table",
}

CONTAINER_LIST = [
    "fridge",
    "closet",
    "table",
    "shelf",
]

CONTAINER_POSITION_LIST = {
    "fridge": "kitchen",
    "closet": "bedroom",
    "table": "living room",
    "shelf": "living room",
}

CONNECTED_ROOM = {
    "hallway": ["kitchen", "bedroom", "bathroom", "living room"],
    "kitchen": ["hallway"],
    "bedroom": ["hallway"],
    "bathroom": ["hallway"],
    "living room": ["hallway"],
}

from mcts.minihouse.minihousemodel import item_object, \
    container_object, room_class, state_class, minihousemodel, key_object,\
    robot_agent, human_agent, move, open, close, pick, place, observation_class

ACTION_DICT = {
    "move": move,
    "open": open,
    "close": close,
    "pick": pick,
    "place": place,
}

GROUNDED_ACTION_LIST = [
    "move living room",
    "move kitchen",
    "move bedroom",
    "move bathroom",
    "move hallway",
    "open fridge",
    "open closet",
    "open shelf",
    "close fridge",
    "close closet",
    "close shelf",
    "pick apple",
    "pick t-shirt",
    "pick cup",
    "place apple fridge",
    "place apple closet",
    "place apple table",
    "place apple shelf",
    "place apple bedroom",
    "place apple bathroom",
    "place apple hallway",
    "place t-shirt fridge",
    "place t-shirt closet",
    "place t-shirt table",
    "place t-shirt shelf",
    "place t-shirt bedroom",
    "place t-shirt bathroom",
    "place t-shirt hallway",
    "place cup fridge",
    "place cup closet",
    "place cup table",
    "place cup shelf",
]


class MiniHouseV1(minihousemodel):
    def __init__(self, instruction, goal_state) -> None:
        super().__init__(instruction, goal_state)
        self.create_initial_state()
        self.grounding_actions()

    def reset(self):
        self.create_initial_state()
        reward = self.get_reward()
        obs = self.get_observation()
        done = self.is_terminal()
        valid_action = self.get_valid_actions()
        return obs, reward, done, self.history, valid_action

    def create_initial_state(self):
        item_dict = {}
        container_dict = {}
        room_dict = {}
        for room in ROOM_LIST:
            room_dict[room] = room_class(
                name = room,
                is_open = True,
                is_locked = False,
                key = None,
                connected_rooms=CONNECTED_ROOM[room],
            )
        for container in CONTAINER_LIST:
            if container == 'table':
                container_dict[container] = container_object(
                    name = container,
                    position = CONTAINER_POSITION_LIST[container],
                    is_open = True,
                    is_locked = False,
                    key = None,
                )
            else:
                container_dict[container] = container_object(
                    name = container,
                    position = CONTAINER_POSITION_LIST[container],
                    is_open = False,
                    is_locked = False,
                    key = None,
                )
        for item in OBJECT_LIST:
            item_dict[item] = item_object(
                name = item,
                position = OBJECT_POSITION_LIST[item],
                is_moveable = True,
            )
        self.state = state_class(
            robot_agent = robot_agent(
                room = "living room",
                picked_item=None,
            ),
            human_agent = human_agent(
                room = "living room",
            ),
            room_list = room_dict,
            container_list = container_dict,
            object_list= item_dict,
        )

    def state_update(self, observation: observation_class):
        self.state = observation.update(self.state)

    def grounding_actions(self):
        action_dict = {}
        for action in ACTION_DICT:
            if action == "move":
                for room in ROOM_LIST:
                    action_dict[action + " to the " + room] = ACTION_DICT[action](room)
            elif action == "open":
                for container in CONTAINER_LIST:
                    action_dict[action + " the " + container] = \
                        ACTION_DICT[action](container)
            elif action == "close":
                for container in CONTAINER_LIST:
                    action_dict[action +  " the " + container] = \
                        ACTION_DICT[action](container)
            elif action == "pick":
                for item in OBJECT_LIST:
                    action_dict[action +  " the " + item] = ACTION_DICT[action](item)
            elif action == "place":
                for item in OBJECT_LIST:
                    for container in CONTAINER_LIST:
                        action_dict[action +  " the " + item + " at the " \
                            +  container] = ACTION_DICT[action](item, container)
                    for room in ROOM_LIST:
                        action_dict[action + " the " +  item + " at the " +\
                            room] = ACTION_DICT[action](item, room)
        self.action_dict = action_dict
        self.action_space = list(action_dict.keys())
        self.action_num = len(self.action_space)