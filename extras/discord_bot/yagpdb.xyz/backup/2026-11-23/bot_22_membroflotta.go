{{/* Custom Command */}}
{{/* Promuove un utente al ruolo di Membro Flotta e lo notifica sul canale, pingando utente e tutti i Membri */}}
{{/* Utilizzo: -membroflotta @utente */}}
{{$args := parseArgs 1 ""
  (carg "user" "target")}}
{{giveRoleID ($args.Get 0).ID 571710879880708097}}{{/* Membro Flotta */}}
{{giveRoleID ($args.Get 0).ID 1323949094938349588}}{{/* Guardiamarina */}}
{{giveRoleID ($args.Get 0).ID 741253469737844858}}{{/* Medagliere */}}
{{giveRoleID ($args.Get 0).ID 718116478338990130}}{{/* Altri Ruoli */}}
{{takeRoleID ($args.Get 0).ID 600385868280365059}}

{{dbSet ($args.Get 0).ID "cadetto_attivo" false}} {{/* DISATTIVA TIMER CADETTO */}}

Congratulazioni {{($args.Get 0).Mention}}! Hai completato il tuo percorso iniziale, diventando **_Allied_** con la nostra PMF **Flotta Stellare** e hai quindi conseguito il ruolo di **Membro effettivo** del nostro Squadrone!
 
Per ottimizzare l'esperienza di gruppo nello squadrone e rendere più immersiva l'esperienza di gioco, ti **chiediamo di andare nel canale <#581171773274324992> e __scegliere una delle seguenti sezioni__**: 
 
<:eco:581164531548684298> *E.co* (Exploration Corps: **Esplorazione**)  
<:god:581164548233625621> *G.O.D.* (General Operations Division: **BGS**)  
<:tsd:581164581729206273> *T.S.D.* (Tactical and Security Division: **Combat**)  
<:axd:784032591175090206> *A.X.D.* (Anti-Xeno Division: caccia ai **Thargoids**) 
 
Ci teniamo a precisare che la scelta di una sezione __non comporta un vero obbligo vincolante per la tua esperienza di gioco__; tuttavia permetterà da una parte di coordinare e calibrare meglio l'azione e dei players disponibili per sostenere l'evoluzione e la crescita in-game della nostra PMF, dall'altra di creare, all'occorrenza, gruppi in-game di giocatori che vogliono condividere missioni od obiettivi comuni.
 
P.S.: _Potresti anche andare sul canale <#743092055739334676> e vedere se trovi qualche obiettivo che hai già conseguito ed autoassegnarti la relativa medaglia, cliccando sulla apposita reazione_ :wink:
 
Fly safe, CMDR <:acfs:572728822965862410>
{{ deleteTrigger 0 }}
