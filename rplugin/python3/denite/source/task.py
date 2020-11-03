# -*- coding: utf-8 -*-

from .base import Base
from time import gmtime, strftime

BUFFER_HIGHLIGHT_SYNTAX = [
    {'name': 'Duration', 'link': 'Comment', 're': r'\[.\+\]'}
]

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'toggl/task'
        self.kind = 'toggl/task'

    def highlight(self) -> None:
        for syn in BUFFER_HIGHLIGHT_SYNTAX:
            self.vim.command(
                'syntax match {0}_{1} /{2}/ contained containedin={0}'.format(
                    self.syntax_name, syn['name'], syn['re']))
            self.vim.command(
                'highlight default link {}_{} {}'.format(
                    self.syntax_name, syn['name'], syn['link']))

    def gather_candidates(self, context):
        tasks = self.vim.call('toggl#list')
        tasks.reverse()
        return [self._convert(task, context) for task in tasks]

    def _convert(self, info, context):
        abbr = '{} [{}]'.format(
                info['description'],
                strftime('%H:%M:%S', gmtime(max(info['duration'], 0)))
                )
        return {
                'word': info['description'],
                'abbr': abbr,
                'action__task': info
                }
