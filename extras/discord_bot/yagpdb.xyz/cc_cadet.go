{{/* Custom Command */}}
{{/* Assegna ad un nuovo utente il ruolo di Cadetto e si porta avanti mettendo le categorie Medagliere ed Altri Ruoli */}}
{{/* Utilizzo: -cadet @ser */}}
{{$args := parseArgs 1 ""
  (carg "user" "target")}}
{{giveRoleID ($args.Get 0).ID 600385868280365059}}
{{giveRoleID ($args.Get 0).ID 712280073721610314}}{{/* Ruoli Operativi*/}}
{{giveRoleID ($args.Get 0).ID 741253469737844858}}{{/* Medagliere */}}
{{giveRoleID ($args.Get 0).ID 718116478338990130}}{{/* Altri Ruoli */}}
Welcome {{($args.Get 0).Mention}}! You have been assigned the role of <@&600385868280365059>, which allows you to see channels reserved for Squadron Members.

While you wait for your growth path to become **_Allied_** with our PMF **Flotta Stellare**, we wish you good gaming.

For any questions or simple curiosities, we recommend the channel <#1048649032408514630>, where you will find **guides** and **useful links** that can help you on your journey through the game.

Fly safe, CMDR! <:acfs:572728822965862410>

{{ deleteTrigger 0 }}