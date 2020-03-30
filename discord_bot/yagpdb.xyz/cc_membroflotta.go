{{/* Custom Command */}}
{{/* Promuove un utente al ruolo di Membro Flotta e lo notifica sul canale, pingando utente e tutti i Membri */}}
{{/* Utilizzo: -membroflotta @utente */}}
{{$args := parseArgs 1 ""
  (carg "user" "target")}}
{{giveRoleID ($args.Get 0).ID 571710879880708097}}
Congratulazioni {{($args.Get 0).Mention}}! Hai completato il tuo percorso iniziale, diventando **_Allied_** con la nostra PMF **Flotta Stellare** e hai quindi conseguito il ruolo di <@&571710879880708097>! Ora vai per favore nel canale <#581171773274324992> e scegli la specializzazione che preferisci, fra *E.co* (Esploratori), *G.O.D.* (BGS) o *T.S.D.* (Combat e operazioni tattiche).

Fly safe, CMDR

{{ deleteTrigger 0 }}

{{$embed := (joinStr "" "Congratulazioni  "  .User.Username "! Hai completato il tuo percorso iniziale, diventando Allied con la nostra PMF **Flotta Stellare** e hai quindi conseguito il ruolo di **Membro Ufficiale della Flotta**! Ora vai per favore nel canale <#581171773274324992> e scegli la specializzazione che preferisci, fra Eco, God o Tsd.")}}

{{ sendDM $embed }}