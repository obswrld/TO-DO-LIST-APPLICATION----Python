from data.models.label import Label
from src.data.repositories import label_repo


class LabelService:
    def __init__(self):
        self.label_repo = label_repo()

    def create_label(self, name, description):
        label = Label(name=name, description=description)
        return self.label_repo.get_or_create_label(label)

    def get_all_labels(self):
        return self.label_repo.get_all_labels()

    def get_label_by_id(self, label_id):
        return self.label_repo.get_label_by_id(label_id)

    def update_label(self, label_id, updated_date):
        return self.label_repo.update_label(label_id, updated_date)

    def delete_label(self, label_id):
        return self.label_repo.delete_label(label_id)



