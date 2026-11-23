{{/* Custom Command #51 "Counter Controllo Cadetti" */}}
{{/* Trigger: Interval, ogni 24 ore */}}
{{/* Legge le scadenze scritte da -cadetto (chiave DB "cadetto_scadenza", timestamp Unix) */}}
{{/* - avvisa il cadetto a 10, 7 e 3 giorni dalla scadenza */}}
{{/* - alla scadenza toglie SOLO il ruolo Cadetto e cancella la scadenza */}}
{{/* - se l'utente non è più nel server o non ha più il ruolo Cadetto (es. promosso), cancella la scadenza senza avvisi */}}

{{$cadettoRole := 600385868280365059}}
{{$canale := 614753357256720384}}
{{$now := currentTime.Unix}}

{{/* dbBottomEntries = ordinate dalla scadenza più vicina */}}
{{range dbBottomEntries "cadetto_scadenza" 100 0}}
  {{$uid := .UserID}}
  {{$member := getMember $uid}}
  {{if not $member}}
    {{dbDel $uid "cadetto_scadenza"}}
  {{else if not (targetHasRoleID $uid $cadettoRole)}}
    {{dbDel $uid "cadetto_scadenza"}}
  {{else}}
    {{$giorni_mancanti := div (sub (toInt64 .Value) $now) 86400}}

    {{if le $giorni_mancanti 0}}
      {{takeRoleID $uid $cadettoRole}}
      {{dbDel $uid "cadetto_scadenza"}}
      {{sendMessage $canale (print "<@" $uid "> il tuo periodo come Cadetto è terminato. Il ruolo è stato rimosso.")}}
    {{else if or (eq $giorni_mancanti 10) (eq $giorni_mancanti 7) (eq $giorni_mancanti 3)}}
      {{sendMessage $canale (print "<@" $uid "> ti restano **" $giorni_mancanti "** giorni per completare i requisiti e diventare Allied.")}}
    {{end}}
  {{end}}
{{end}}
