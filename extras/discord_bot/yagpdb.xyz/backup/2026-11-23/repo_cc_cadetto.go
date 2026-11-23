{{/* Custom Command */}}
{{/* Assegna ad un nuovo utente il ruolo di Cadetto e si porta avanti mettendo le categorie Medagliere ed Altri Ruoli */}}
{{/* Utilizzo: -cadetto @utente */}}
{{$args := parseArgs 1 ""
  (carg "user" "target")}}
{{giveRoleID ($args.Get 0).ID 600385868280365059}}
{{giveRoleID ($args.Get 0).ID 712280073721610314}}{{/* Ruoli Operativi*/}}
{{giveRoleID ($args.Get 0).ID 741253469737844858}}{{/* Medagliere */}}
{{giveRoleID ($args.Get 0).ID 718116478338990130}}{{/* Altri Ruoli */}}
Benvenuto {{($args.Get 0).Mention}}! Ti è stato assegnato il ruolo di <@&600385868280365059>, che ti consente di vedere i canali riservati ai Membri dello Squadrone.

Per completare il tuo percorso di crescita, diventando **_Allied_** con la nostra PMF **Flotta Stellare**, potresti dare uno sguardo al canale <#783648396576555049> :wink:

Per ogni tipo di dubbio o semplice curiosità, ti consigliamo il canale <#1048649032408514630>, dove troverai **guide** e **link utili** che ti potranno aiutare nel tuo percorso all'interno del gioco.

Ti auguriamo buon gioco.
Fly safe, CMDR! <:acfs:572728822965862410>

{{ deleteTrigger 0 }}