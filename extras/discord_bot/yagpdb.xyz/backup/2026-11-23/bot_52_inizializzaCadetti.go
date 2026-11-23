{{/* Comando: -inizializzaCadetti */}}
{{/* Scansiona tutti i membri e inizializza i cadetti nel database */}}

{{$durata := 30}} {{/* Cambia a 60 se vuoi */}}
{{$now := currentTime}}
{{$cadettoRole := 600385868280365059}} {{/* ID ruolo Cadetto */}}

{{$count := 0}}

{{range .Guild.Members}}
    {{if hasRoleID .User.ID $cadettoRole}}
        {{/* Se non esiste già un record, lo crea */}}
        {{if not (dbGet .User.ID "cadetto_start")}}
            {{dbSet .User.ID "cadetto_start" $now}}
            {{dbSet .User.ID "cadetto_durata" $durata}}
            {{dbSet .User.ID "cadetto_attivo" true}}
            {{$count = add $count 1}}
        {{end}}
    {{end}}
{{end}}

Inizializzazione completata. Sono stati registrati **{{$count}}** cadetti nel database.
