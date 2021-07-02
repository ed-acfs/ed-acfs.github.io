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

In attesa che completi il tuo percorso di crescita diventando **_Allied_** con la nostra PMF **Flotta Stellare**, ti auguriamo buon gioco.
Fly safe, CMDR! <:acfs:572728822965862410>