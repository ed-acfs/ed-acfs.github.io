{{/* Custom Command */}}
{{/* Reagisce a qualunque frase contenga "schettin" al proprio interno */}}
{{/* Utilizzo: -big <una qualsiasi frase che big deve ripetere */}}
{{/* Trigger Type: Command - Trigger: big */}}
 
{{$args := parseArgs 1 "Utilizzo: -big <seguito dal testo che Big deve ripetere>"
	(carg "string" "testo del messaggio che Big deve ripetere")}}
 
{{addResponseReactions ":triggered:699970093127434280" ":middle_finger:"}}
 
<:triggered:699970093127434280> Chi cazzo ha parlato di {{($args.Get 0)}} ???
{{/*execAdmin "grep" .User*/}}
{{/*sendMessage nil (joinStr "" "Chi cazzo ha parlato di " ($args.Get 0 ) "???")*/}}
 
{{ deleteTrigger 0 }}