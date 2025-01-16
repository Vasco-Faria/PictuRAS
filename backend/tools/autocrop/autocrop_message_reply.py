import json

class AutoCropMessageReply:

    def __init__(self, image: str) -> None:
        self.image = image


    def getImage(self) -> str:
        return self.image


    def to_json(self) -> str:
        return json.dumps({
            'image': self.image,
        })


    @staticmethod
    def from_json(data: str) -> 'AutoCropMessageReply':
        data = json.loads(data)
        return AutoCropMessageReply(
            image=data['image'],
        )