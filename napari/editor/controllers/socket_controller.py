from ..socket import Socket


class SocketController:
    def __init__(self):
        pass

    @staticmethod
    def create(name: str, node_id: int) -> 'Socket':
        return Socket(name, node_id)
