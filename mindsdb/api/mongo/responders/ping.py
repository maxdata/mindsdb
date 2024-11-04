from mindsdb.api.mongo.classes import Responder
import mindsdb.api.mongo.functions as helpers


class Responce(Responder):
    when = {'ping': helpers.is_true}

    result = {
        "ok": 1
    }


responder = Responce()
