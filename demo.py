.

ROOM_LIST = [
    "gym",
    "pool",
    "cafeteria",
    "therapy room",
    "reception",
]

OBJECT_LIST = [
    "walker",
    "ball",
    "towel"
]

OBJECT_POSITION_LIST = {
    "walker": "closet",
    "ball": "storage",
    "towel": "shelf",
}

CONTAINER_LIST = [
    "closet",
    "storage",
    "shelf",
    "rack",
]

CONTAINER_POSITION_LIST = {
    "closet": "therapy room",
    "storage": "gym",
    "shelf": "cafeteria",
    "rack": "pool",
}

CONNECTED_ROOM = {
    "reception": ["gym", "pool", "cafeteria", "therapy room"],
    "gym": ["reception"],
    "pool": ["reception"],
    "cafeteria": ["reception"],
    "therapy room": ["reception"],
}

ACTION_DICT = {
    "move": move,
    "open": open,
    "close": close,
    "pick": pick,
    "place": place,
}

GROUNDED_ACTION_LIST = [
    "move gym",
    "move pool",
    "move cafeteria",
    "move therapy room",
    "move reception",
    "open closet",
    "open storage",
    "open shelf",
    "open rack",
    "close closet",
    "close storage",
    "close shelf",
    "close rack",
    "pick walker",
    "pick ball",
    "pick towel",
    "place walker closet",
    "place walker storage",
    "place walker shelf",
    "place walker rack",
    "place walker therapy room",
    "place walker gym",
    "place walker cafeteria",
    "place ball closet",
    "place ball storage",
    "place ball shelf",
    "place ball rack",
    "place ball therapy room",
    "place ball gym",
    "place ball cafeteria",
    "place towel closet",
    "place towel storage",
    "place towel shelf",
    "place towel rack",
    "place towel therapy room",
    "place towel gym",
    "place towel cafeteria",
]