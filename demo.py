ROOM_LIST = [
    "gym",
    "physical therapy room",
    "therapy room",
    "cafeteria",
    "reception",
]

OBJECT_LIST = [
    "walker",
    "exercise weights",
    "yoga mat",
    "therapy ball",
    "towel",
]

OBJECT_POSITION_LIST = {
    "walker": "closet",
    "exercise weights": "bench",
    "yoga mat": "stack",
    "therapy ball": "shelf",
    "towel": "cart"
}

CONTAINER_LIST = [
    "closet",
    "bench",
    "stack",
    "shelf",
    "cart",
]

CONTAINER_POSITION_LIST = {
    "closet": "therapy room",
    "bench": "gym",
    "stack": "gym",
    "shelf": "physical therapy room", 
    "cart": "cafeteria",
}

CONNECTED_ROOM = {
    "reception": ["gym", "physical therapy room", "therapy room", "cafeteria"],
    "gym": ["reception"],
    "physical therapy room": ["reception"],
    "therapy room": ["reception"],
    "cafeteria": ["reception"],
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
    "move physical therapy room",
    "move therapy room",
    "move cafeteria",
    "move reception",
    "open closet",
    "open bench",
    "open stack",
    "open shelf",
    "open cart",
    "close closet",
    "close bench",
    "close stack",
    "close shelf",
    "close cart",
    "pick walker",
    "pick exercise weight",
    "pick yoga mat",
    "pick therapy ball",
    "pick towel",
    "place walker closet",
    "place walker bench",
    "place walker stack",
    "place walker shelf",
    "place walker cart",
    "place walker therapy room",
    "place walker gym",
    "place walker physical therapy room",
    "place walker cafeteria",
    "place exercise weight closet",
    "place exercise weight bench",
    "place exercise weight stack",
    "place exercise weight shelf",
    "place exercise weight cart",
    "place exercise weight therapy room",
    "place exercise weight gym",
    "place exercise weight physical therapy room",
    "place exercise weight cafeteria",
    "place yoga mat closet",
    "place yoga mat bench",
    "place yoga mat stack",
    "place yoga mat shelf",
    "place yoga mat cart",
    "place yoga mat therapy room",
    "place yoga mat gym",
    "place yoga mat physical therapy room",
    "place yoga mat cafeteria",
    "place therapy ball closet",
    "place therapy ball bench",
    "place therapy ball stack",
    "place therapy ball shelf",
    "place therapy ball cart",
    "place therapy ball therapy room",
    "place therapy ball gym",
    "place therapy ball physical therapy room",
    "place therapy ball cafeteria",
    "place towel closet",
    "place towel bench",
    "place towel stack",
    "place towel shelf",
    "place towel cart",
    "place towel therapy room",
    "place towel gym",
    "place towel physical therapy room",
    "place towel cafeteria",
]