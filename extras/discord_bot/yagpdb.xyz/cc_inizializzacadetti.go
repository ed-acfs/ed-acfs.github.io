{{/* Custom Command #52 */}}
{{/* Comando: -inizializzaCadetti @utente [giorni] */}}
{{/* Registra (o corregge) la scadenza di un Cadetto già esistente che non è passato da -cadetto. */}}
{{/* Giorni = giorni che gli restano da oggi; se omesso vale 45, come -cadetto. */}}

{{$args := parseArgs 1 "Uso: `-inizializzaCadetti @utente [giorni rimanenti]`"
  (carg "user" "cadetto")
  (carg "int" "giorni rimanenti" 1 365)}}
{{$u := $args.Get 0}}
{{$cadettoRole := 600385868280365059}}

{{$giorni := 45}}
{{if $args.IsSet 1}}{{$giorni = $args.Get 1}}{{end}}

{{if not (targetHasRoleID $u.ID $cadettoRole)}}
{{$u.Mention}} non ha il ruolo <@&600385868280365059>: non registro niente.
{{else}}
{{$scadenza := add currentTime.Unix (mult $giorni 86400)}}
{{$prima := dbGet $u.ID "cadetto_scadenza"}}
{{dbSet $u.ID "cadetto_scadenza" $scadenza}}
{{if $prima}}Scadenza aggiornata{{else}}Registrato{{end}}: {{$u.Mention}} ha **{{$giorni}}** giorni, scade <t:{{$scadenza}}:d>.
{{end}}
{{deleteTrigger 0}}
