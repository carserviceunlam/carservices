from vmSystem.apps.admin_website.models.repair import Repair


class RepairSerializer():
    def __init__(self, data, _id):
        self.data = data
        self._id = _id

    def update_repair(self):
        existing_repair = Repair.objects.get(id=self._id)
        existing_repair.budget = self.data['budget']
        existing_repair.exit_date = self.data['exit_date']
        existing_repair.invoice = self.data['invoice']
        existing_repair.authorize_exit = self.data['authorize_exit']
        existing_repair.authorize_repair = self.data['authorize_repair']
        existing_repair.entrance_detail = self.data['entrance_detail']
        existing_repair.save()
