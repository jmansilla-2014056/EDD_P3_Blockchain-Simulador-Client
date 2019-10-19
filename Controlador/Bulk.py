import csv
from datetime import datetime
import hashlib
from Modelos.Doublylinkedlist import DoublyLinkedList
import json

from Modelos.TreeAvl import TreeAvl

dll = DoublyLinkedList()


def encrypt_string(hash_string):
    print(hash_string)
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


# get students on json
def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict)  # Return value ignored.
    return results


# read csv
def readCSV(direction):
    with open(direction, 'r') as f:
        reader = csv.reader(f)
        listN = list(reader)
    return generateString(listN)


# this method return a block with all information (this block is sending after in all users)
def generateString(listN: list):
    concat = "{ \n"
    previousHash = ""
    now = datetime.now()
    timeStamp = datetime.now()
    node = dll.start_node
    index = dll.count()
    if node is None:
        previousHash = '0000'
    else:
        while node is not None:
            previousHash = node.hash
            node = node.prev
    clase = listN[0][1]
    data = listN[1][1]

    obj = json.loads(str(data))
    concat = concat + '"INDEX": ' + str(index) + ',\n'
    concat = concat + '"TIMESTAMP": "' + str(timeStamp) + '",\n'
    concat = concat + '"CLASS": "' + str(clase) + '",\n'
    concat = concat + '"DATA": ' + str(data) + ',\n'
    concat = concat + '"PREVIUSHASH": "' + str(previousHash) + '",\n'
    HASH = encrypt_string(str(index) + str(timeStamp) + str(clase) + str(obj).replace("\'", '"').replace("None", "null").replace(" ", "") + str(previousHash))
    concat = concat + '"HASH": "' + HASH + '"\n' + "}"
    return concat


# if the user select a json in that list, generate three
def ReadBlockJson(jsonTxt):
    jsonTxt = str(jsonTxt).replace("\'", '"').replace("None", "null").replace(" ", "")
    newAVL = TreeAvl()
    obj = find_values('value', str(jsonTxt))
    for i in obj:
        values = str(i).split("-")
        newAVL.insert(values[0], values[1])
    newAVL.graph()


# if the user select a POST,INN OR PRE and select a block
def Orders(jsonTxt):
    newAVL = TreeAvl()
    obj = find_values('value', str(jsonTxt))
    for i in obj:
        values = str(i).split("-")
        newAVL.insert(values[0], values[1])
    newAVL.Post()
    newAVL.listSimple.graphSimple("Post-Order")
    newAVL.Pre()
    newAVL.listSimple.graphSimple("Pre-Order")
    newAVL.Inno()
    newAVL.listSimple.graphSimple("Inn-Order")


# if the message received is true save the json in a list
def saveJson(jsonTxt: str):
    obj = json.loads(str(jsonTxt))
    if len(jsonTxt) > 1:
        dll.insert_at_end(jsonTxt, obj["HASH"])


# in the moment of received a jason return true if the hash is correct else send false
def validateJson(jsonTxt: str):
    obj = json.loads(str(jsonTxt))
    index = obj["INDEX"]
    timeStamp = obj["TIMESTAMP"]
    clase = obj["CLASS"]
    data = obj["DATA"]
    previousHash = obj["PREVIUSHASH"]
    hash = obj["HASH"]
    HASH = encrypt_string(str(index) + str(timeStamp) + str(clase) + str(data).replace("\'", '"').replace("None", "null").replace(" ", "") + str(previousHash))
    if HASH == hash:
        print("true")
        return "true"
    else:
        print("false")
        return "false"
