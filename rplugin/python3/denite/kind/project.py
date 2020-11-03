# -*- coding: utf-8 -*-

from .base import Base

class Kind(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'toggl/project'
        self.default_action = 'set_current'

    def action_set_current(self, context):
        current_task = self.vim.call('toggl#time_entries#get_running')
        if current_task == 0:
            self.vim.command(f'echo "No task is running"')
            return
        for target in context['targets']:
            project = target['action__project']
            self.vim.call('toggl#update_current', {'pid': project['id']})
