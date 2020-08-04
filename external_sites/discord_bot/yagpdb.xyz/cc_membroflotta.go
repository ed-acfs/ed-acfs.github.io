{{/* Custom Command */}}
{{/* Promuove un utente al ruolo di Membro Flotta e lo notifica sul canale, pingando utente e tutti i Membri */}}
{{/* Utilizzo: -membroflotta @utente */}}
{{$args := parseArgs 1 ""
  (carg "user" "target")}}
{{giveRoleID ($args.Get 0).ID 571710879880708097}}
{{takeRoleID ($args.Get 0).ID 600385868280365059}}
Congratulazioni {{($args.Get 0).Mention}}! Hai completato il tuo percorso iniziale, diventando **_Allied_** con la nostra PMF **Flotta Stellare** e hai quindi conseguito il ruolo di <@&571710879880708097>! Ora potresti dare uno sguardo al canale <#581171773274324992> e scegliere la specializzazione che preferisci, fra *E.co* (Esploratori), *G.O.D.* (BGS) o *T.S.D.* (Combat e operazioni tattiche).
La specializzazione non è vincolante e la potrai cambiare in ogni momento.

Fly safe, CMDR

{{ deleteTrigger 0 }}