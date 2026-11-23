{{/* Custom Command #53 */}}
{{/* Comando: -listacadetti */}}
{{/* Elenca i cadetti registrati da -cadetto (chiave DB "cadetto_scadenza"), dalla scadenza più vicina */}}

{{$entries := dbBottomEntries "cadetto_scadenza" 100 0}}

{{if not $entries}}
<:acfs:1409490874555043870> **Nessun cadetto registrato nel database.**
{{deleteTrigger 0}}
{{return}}
{{end}}

{{$now := currentTime.Unix}}
{{$msg := ""}}
{{$n := 0}}

{{range $entries}}
  {{$scadenza := toInt64 .Value}}
  {{$giorni_mancanti := div (sub $scadenza $now) 86400}}
  {{$riga := print "\n<:acfs:1409490874555043870> <@" .UserID "> — ⏳ **" $giorni_mancanti "** giorni (scade <t:" $scadenza ":d>)"}}
  {{if gt (add (len $msg) (len $riga)) 3900}}
    {{$msg = print $msg "\n…e altri."}}
    {{break}}
  {{end}}
  {{$msg = print $msg $riga}}
  {{$n = add $n 1}}
{{end}}

{{sendMessage nil (cembed
  "title" (print "📋 Cadetti registrati: " (len $entries))
  "description" $msg
  "color" 3447003
)}}
{{deleteTrigger 0}}
