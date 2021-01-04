{{/* Custom Command */}}
{{/* Promuove un utente al ruolo di Membro Flotta e lo notifica sul canale, pingando utente e tutti i Membri */}}
{{/* Utilizzo: -membroflotta @utente */}}
{{$args := parseArgs 1 ""
  (carg "user" "target")}}
{{giveRoleID ($args.Get 0).ID 571710879880708097}}
{{giveRoleID ($args.Get 0).ID 712280073721610314}}{{/* Ruoli Operativi*/}}
{{giveRoleID ($args.Get 0).ID 741253469737844858}}{{/* Medagliere */}}
{{giveRoleID ($args.Get 0).ID 718116478338990130}}{{/* Altri Ruoli */}}
{{takeRoleID ($args.Get 0).ID 600385868280365059}}
Congratulazioni {{($args.Get 0).Mention}}! Hai completato il tuo percorso iniziale, diventando **_Allied_** con la nostra PMF **Flotta Stellare** e hai quindi conseguito il ruolo di <@&571710879880708097>! Ora potresti dare uno sguardo al canale <#581171773274324992> e scegliere la specializzazione che preferisci, fra *E.co* (Esploratori), *G.O.D.* (BGS), *T.S.D.* (Combat e operazioni tattiche) o *A.X.D.* (Anti-Xeno).
La specializzazione non è vincolante e la potrai cambiare in ogni momento.

P.S.: _Potresti anche andare sul canale <#743092055739334676> e vedere se trovi qualche obiettivo che hai già conseguito ed autoassegnarti la relativa medaglia, cliccando sulla apposita reazione_ :wink:

Fly safe, CMDR

{{ deleteTrigger 0 }}