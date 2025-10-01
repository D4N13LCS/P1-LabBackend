from datetime import datetime


class CategoryEvent:
    def __init__(self, category_id: str):
        self.category_id = category_id
        self.timestamp = datetime.now().timestamp()

    def __repr__(self):
        return f"<{self.__class__.__name__} category_id={self.category_id} at={self.timestamp}>"

class CategoryCreated(CategoryEvent):
    def __init__(self, category_id: str, name: str, description: str, is_active: bool):
        super().__init__(category_id)
        self.name = name
        self.description = description
        self.is_active = is_active


class CategoryUpdated(CategoryEvent):
    def __init__(self, category_id: str, updated_fields: dict):
        super().__init__(category_id)
        self.updated_fields = updated_fields


class CategoryActivated(CategoryEvent):
    pass


class CategoryDeactivated(CategoryEvent):
    pass
