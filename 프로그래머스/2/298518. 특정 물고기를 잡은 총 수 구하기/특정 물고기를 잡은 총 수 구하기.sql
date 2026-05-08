select count(i.FISH_TYPE) as FISH_COUNT from FISH_INFO i
left join FISH_NAME_INFO f on i.FISH_TYPE = f.FISH_TYPE
where FISH_NAME in ('BASS', 'SNAPPER');