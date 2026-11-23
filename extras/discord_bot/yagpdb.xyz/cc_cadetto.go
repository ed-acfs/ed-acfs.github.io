{{/* Comando: -cadetto @utente */}}

{{$args := parseArgs 1 "" (carg "user" "target") -}}
{{$u := $args.Get 0 -}}

{{$durata := 45 -}}          {{/* Durata in giorni */}}
{{$now := currentTime -}}    {{/* Timestamp attuale */}}
{{$scadenza := add $now.Unix (mult $durata 86400) -}}

{{/* Salvataggio nel database */}}
{{dbSet $u.ID "cadetto_scadenza" $scadenza -}}

{{/* Assegna ruoli */}}
{{giveRoleID $u.ID 600385868280365059 -}}
{{giveRoleID $u.ID 712280073721610314 -}}
{{giveRoleID $u.ID 741253469737844858 -}}
{{giveRoleID $u.ID 718116478338990130 -}}

Benvenuto {{ $u.Mention }}! Ti è stato assegnato il ruolo di <@&600385868280365059>, che ti consente di vedere i canali riservati ai Membri dello Squadrone.

Per completare il tuo percorso di crescita, diventando **_Allied_** con la nostra PMF **Flotta Stellare**, potresti dare uno sguardo al canale <#783648396576555049> :wink:

Per ogni tipo di dubbio o semplice curiosità, ti consigliamo il canale <#1048649032408514630>, dove troverai **guide** e **link utili** che ti potranno aiutare nel tuo percorso all'interno del gioco.

---

⏳ **Il tuo periodo da Cadetto ha una durata di {{ $durata }} giorni.**  
Da oggi hai **{{ $durata }} giorni** per completare i requisiti necessari alla promozione.

Alla scadenza del periodo, se i requisiti non saranno completati, il ruolo di Cadetto verrà automaticamente rimosso.

---

Ti auguriamo buon gioco.  
Fly safe, CMDR! <:acfs:572728822965862410>

{{deleteTrigger 0}}
