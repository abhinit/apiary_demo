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