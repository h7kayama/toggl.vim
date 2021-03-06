" FILE: toggl.vim
" AUTHOR: Toshiki Teramura <toshiki.teramura@gmail.com>
" LICENCE: MIT

let s:save_cpo = &cpo
set cpo&vim

command!        -nargs=1 TogglStart call toggl#start(<q-args>)
command! -range -nargs=0 TogglSelectStart call toggl#select_start()
command!        -nargs=0 TogglCacheUpdate call toggl#task_cache_update()
command!        -nargs=0 TogglStop call toggl#stop()
command!        -nargs=0 TogglTask call toggl#task()
command!        -nargs=0 TogglTime call toggl#time()

let &cpo = s:save_cpo
unlet s:save_cpo
