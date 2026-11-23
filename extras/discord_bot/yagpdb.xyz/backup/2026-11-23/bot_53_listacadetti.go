{{/* Comando: -listacadetti */}}

{{$entries := dbTopEntries "cadetto_start" 1000 0}}

{{if not $entries}}
<:acfs:1409490874555043870> **Nessun cadetto registrato nel database.**
{{deleteTrigger 0}}
{{return}}
{{end}}

{{$msg := ""}}

{{range $entries}}
    {{$uid := .UserID}}
    {{$start := toInt .Value}}
    {{$durata := toInt (dbGet $uid "cadetto_durata").Value}}
    {{$attivo := (dbGet $uid "cadetto_attivo").Value}}

    {{$now := currentTime}}
    {{$giorni_passati := div (sub $now $start) 86400}}
    {{$giorni_mancanti := sub $durata $giorni_passati}}

    {{$msg = print $msg "\n<:acfs:1409490874555043870> <@" $uid "> — "}}

    {{if $attivo}}
        {{$msg = print $msg "🟢 Attivo | ⏳ Giorni mancanti: **" $giorni_mancanti "**"}}
    {{else}}
        {{$msg = print $msg "🔴 Non attivo"}}
    {{end}}
{{end}}

{{sendMessage nil (print "**📋 Lista Cadetti Registrati:**" $msg)}}
{{deleteTrigger 0}}
