{{/* Trigger: Hourly interval (86400 sec) oppure Crontab */}}

{{$members := dbTopEntries "cadetto_scadenza" 100 0}}
{{$now := currentTime.Unix}}

{{range $members}}
  {{$uid := .UserID}}
  {{$scadenza := toInt64 .Value}}
  {{$giorni_mancanti := div (sub $scadenza $now) 86400}}

  {{/* Avvisi a 10, 7, 3 giorni dalla scadenza */}}
  {{if or (eq $giorni_mancanti 10) (eq $giorni_mancanti 7) (eq $giorni_mancanti 3)}}
    {{sendMessage 614753357256720384 (print "<@" $uid "> ti restano **" $giorni_mancanti "** giorni per completare i requisiti e diventare Allied.")}}
  {{end}}

  {{/* Scadenza del periodo cadetto */}}
  {{if le $giorni_mancanti 0}}
    {{takeRoleID $uid 600385868280365059}}
    {{dbDel $uid "cadetto_scadenza"}}
    {{sendMessage 614753357256720384 (print "<@" $uid "> il tuo periodo come Cadetto è terminato. Il ruolo è stato rimosso.")}}
  {{end}}
{{end}}
