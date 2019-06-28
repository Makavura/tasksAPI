from datetime import datetime


class Tasks(object):

    tasks = []

    def __init__(self, title, description):
        self.id = len(self.tasks)+1
        self.title = title
        self.description = description
        self.createdDate = datetime.now()
        self.startDate = datetime.now()
        self.endDate = None


    def create_task(self):
        task = {
            id = self.id,
            title = self.title,
            description = self.description,
            createdDate = self.createdDate,
            startDate = self.startDate,
            endDate = self.endDate
        }
        Tasks.tasks.append(task)
        return task

    def get_tasks(self):
        return Tasks.tasks

    def get_task_by_id(self, id):
        for task in Tasks.tasks:
            if task['id'] == id:
                return task

    def get_task_by_title(self, title):
        for task in Tasks.tasks:
            if task['title'] == title:
                return task

    def update_task(self, id, title, description):
        task = Tasks.get_task_by_id(self, id)
        if task['id'] == id:
            task['title'] = title
            task['description'] = description

            return task
