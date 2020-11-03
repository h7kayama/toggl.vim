# -*- coding: utf-8 -*-

from .base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'toggl/task'
        self.kind = 'toggl/task'

    def gather_candidates(self, context):
        tasks = self.vim.call('toggl#list')
        return [self._convert(task) for task in tasks]

    def _convert(self, info):
        abbr = '[%d] %s' % (info['id'], info['description'])
        return {
                'word': info['description'],
                'abbr': abbr,
                'action__path': info
                }
