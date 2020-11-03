# -*- coding: utf-8 -*-

from .base import Base

class Kind(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'toggl/task'
        self.default_action = 'restart'

    def action_restart(self, context):
        for target in context['targets']:
            task = target['action__path']
            self.vim.call('toggl#time_entries#start', task['description'], task['pid'], [])
            self.vim.call('toggl#task_cache_update')
