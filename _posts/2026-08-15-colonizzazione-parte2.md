---
layout: post
title:  "Colonizzazione: Capitolo 2 - Pianificare il sistema"
date:   2026-08-15
excerpt: "Prima di iniziare a costruire conviene capire come funzionano i Construction Points, perché il quinto porto costa molto più del primo, e quali strumenti usano gli architetti più esperti per pianificare tutto in anticipo."
image: "/images/posts/colonizzazione/costruzione-coriolis.jpg"
tags: guide colonizzazione trailblazers tutorial
author: wiitifulsky
last_modified_at: 2026-08-15
sticky: no
---
Ciao Comandanti, sono di nuovo io. Nel [primo capitolo](/blog/colonizzazione-parte1/) abbiamo visto perché conviene colonizzare e come si reclama il primo sistema. Oggi entriamo nella parte che spaventa di più chi comincia: come si pianifica davvero un sistema, senza sprecare mesi di lavoro per scoprire solo alla fine di aver costruito le cose nell'ordine sbagliato.

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## I tre Tier delle strutture

Ogni struttura costruibile appartiene a uno di tre **Tier** (livelli):

- **Tier 1** — avamposti spaziali, insediamenti piccoli/medi, la maggior parte delle installazioni orbitali
- **Tier 2** — Coriolis, Basi Asteroidi, insediamenti grandi, gli hub planetari
- **Tier 3** — Orbis, Ocellus, e il Porto Planetario Tier 3 (l'unico porto planetario oltre al Tier 1 — non esiste un porto planetario di Tier 2)

Più il Tier è alto, meglio è: le strutture Tier 3 hanno le statistiche migliori in assoluto, sia in totale che per singolo slot occupato. Il problema è che non puoi costruirle a piacimento: servono dei "punti" che devi generare prima.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Nota:</b>&nbsp;Il gioco usa la parola "Tier" anche per un'altra cosa (i tipi di Construction Points, vedi sotto), il che genera parecchia confusione. In questa guida "Tier" si riferisce sempre al livello di una struttura.</div>

## Construction Points: Yellow e Green

Per costruire una struttura di Tier 2 o Tier 3 servono dei **Construction Points (CP)**, che si generano costruendo strutture del Tier inferiore:

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Nota:</b>&nbsp;"Yellow" e "Green" non sono nomi ufficiali del gioco — sono la convenzione adottata dalla Colonization Mega Guide di CMDR Mechan (e ripresa da strumenti di pianificazione come Raven Colonial) per distinguere i due tipi di CP senza confonderli con i Tier delle strutture, dato che il gioco stesso usa "Tier" per entrambe le cose in modo ambiguo. Le trovi con questi nomi anche negli strumenti di pianificazione citati più avanti, quindi vale la pena conoscerle.</div>

- Le strutture **Tier 1** non costano nessun CP e generano **CP Yellow** (Tier 2)
- Le strutture **Tier 2** costano CP Yellow e generano **CP Green** (Tier 3) — di norma 1 Yellow speso genera 1 Green, con due eccezioni: gli insediamenti grandi ne generano 2, mentre Coriolis e Basi Asteroidi (essendo loro stesse porti Tier 2) ne costano 3 o più per generarne solo 1
- Le strutture **Tier 3** costano CP Green e non generano nulla

In pratica: costruisci Tier 1 per accumulare Yellow, converti gli Yellow in Green costruendo Tier 2, e spendi i Green per arrivare finalmente ai Tier 3. Ogni struttura che genera CP (cioè che non sia un porto) viene chiamata **struttura di supporto**.

## Il costo nascosto: perché il quinto porto costa una fortuna

Questa è l'informazione più importante di tutto il capitolo, e la più facile da ignorare finché non ci sbatti contro: **il costo in CP di ogni nuovo porto Tier 2 o Tier 3 aumenta ogni volta che ne inizi la costruzione**, nello stesso sistema. Non serve che il porto precedente sia finito — basta averlo avviato.

| Porto — CP Yellow/Green richiesti | 1° | 2° | 3° | 4° | 5° | N-esimo |
|---|---|---|---|---|---|---|
| **Tier 2**, Coriolis/Base Asteroidi (Yellow) | 3 | 3 | 5 | 7 | 9 | 3+(n-2)×2 |
| **Tier 3**, Orbis/Ocellus/Porto Planetario T3 (Green) | 6 | 6 | 12 | 18 | 24 | (n-1)×6 |

Il Tier 3 raddoppia di costo già al terzo porto, e continua a salire di 6 Green ogni volta. Questo ha due conseguenze pratiche dirette:

1. **Conviene sempre costruire i Tier 3 prima dei Tier 2**, se hai intenzione di volerli entrambi. Confronta questi due ordini di costruzione nello stesso sistema:
   - T2, T2, T3, T3 → costo totale 6 Yellow + **28 Green**, minimo 36 strutture di supporto
   - T3, T3, T2, T2 → costo totale 16 Yellow + **12 Green**, minimo 28 strutture di supporto

   Stesso risultato finale, ma il secondo ordine costa meno della metà in Green e richiede otto strutture di supporto in meno.
2. **Il numero di porti Tier 2/3 che puoi permetterti in un sistema è limitato**. Il quinto Tier 3 richiede da solo almeno 30 strutture di supporto solo per generare i Green necessari.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Il trucco che vale la pena conoscere:</b>&nbsp;Il porto primario (quello scelto al momento della rivendicazione, capitolo 1) <b>non conta</b> in questa progressione e non costa nessun CP. Se hai intenzione di costruire un sistema "importante", scegliere fin da subito un Porto Planetario Tier 3 come porto primario ti regala gratis lo slot più pregiato del sistema, senza consumare nessuno "sconto" sulla progressione dei costi.</div>

## Cinque cantieri alla volta, non uno di più

Puoi avere **al massimo cinque strutture in costruzione contemporaneamente** in un sistema. Superata questa soglia, per avviarne una nuova devi prima completarne (o annullarne) almeno una tra quelle in corso. È una regola semplice ma che vale la pena tenere a mente quando pianifichi l'ordine dei lavori con altri comandanti della Flotta, per non ritrovarvi tutti a consegnare materiali per un cantiere che non può nemmeno partire.

## Slot in orbita o sulla superficie?

Ogni corpo celeste offre un numero fisso di slot orbitali e planetari, e la scelta tra i due non è solo estetica:

**A favore dell'orbita:**
- Coriolis, Orbis e Ocellus hanno pad grandi e sono comode da raggiungere — niente avvicinamento in atmosfera o superficie
- I collegamenti forti con mercati di contrabbando (basi pirata) si possono creare solo in orbita
- Alcune merci specifiche si producono solo nei porti orbitali

**A favore della superficie:**
- Altre merci specifiche si producono solo negli insediamenti planetari
- Il Porto Planetario Tier 3 ha le statistiche migliori di qualsiasi struttura nel gioco
- Gli insediamenti grandi (Tier 2) sono l'unico tipo di struttura che converte un singolo Yellow in **due** Green invece che uno
- Le strutture di superficie possono stare molto vicine tra loro (minimo 200 km), utile quando devi consegnare materiali a più cantieri contemporaneamente
- Gli hub, esclusivamente planetari, sono tra le strutture migliori per specializzare l'economia di un porto e danno buoni bonus a tutto il sistema

Non c'è una risposta giusta in assoluto: dipende da cosa vuoi ottenere. Ma vale la pena guardare quanti slot orbitali e planetari offre il corpo celeste del tuo porto primario prima di reclamare, perché quel numero resta fisso per sempre.

## Nomi personalizzati e livree: il lato estetico

Ogni struttura riceve un nome casuale, che puoi ri-estrarre quante volte vuoi finché non ne trovi uno che ti piace. Se invece vuoi un nome scelto da te, costa **5.000 ARX** a struttura (nome che deve essere unico nel sistema, niente apostrofi né alcuni altri caratteri speciali). Una volta pagato, puoi cambiarlo di nuovo quante volte vuoi gratuitamente; se invece resti sui nomi casuali, puoi comunque "riassegnarne" uno nuovo a una struttura già esistente, ma solo **cinque volte in totale** per struttura — usale con parsimonia. I nomi si aggiornano subito per la maggior parte delle strutture, mentre per i porti bisogna aspettare la manutenzione settimanale del giovedì.

## Gli strumenti che ti semplificano la vita

Fare questi conti a mano, sistema dopo sistema, è impraticabile. Due strumenti comunitari fanno praticamente tutto il lavoro per te:

- **[Raven Colonial](https://ravencolonial.com/#home){:target="_blank"}**, di CMDR Grinning2001: un'interfaccia web dove progetti il sistema graficamente e lo strumento calcola da solo Yellow/Green necessari, ordine di costruzione consigliato e dipendenze.
- **La [spreadsheet di CMDR DaftMav](https://docs.google.com/spreadsheets/d/16_hh1G6Tb66OdS01Li0955lITp7yLleb3a8dmqVqq2o/edit){:target="_blank"}**: lo strumento storico della community, che permette di "simulare" la costruzione del sistema passo passo evidenziando ogni dipendenza. Buona parte dei dati usati da Raven Colonial arriva proprio da qui.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Consiglio:</b>&nbsp;Se stai pianificando un sistema per la Flotta insieme ad altri comandanti, progettalo su Raven Colonial <i>prima</i> di iniziare a costruire e condividi il link con chi partecipa: evita doppioni, cantieri avviati nell'ordine sbagliato, e discussioni su "chi doveva costruire cosa" a lavori già iniziati.</div>

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

Nel prossimo capitolo parliamo di economia: come i porti "ereditano" un'economia dal corpo celeste su cui sorgono, come funzionano i collegamenti forti e deboli tra strutture, e perché da patch 4.2.0.1 conviene specializzare ogni porto su una o due economie al massimo invece di lasciarlo generico.

FONTI: [System Colonisation Guide](https://www.elitedangerous.com/news/system-colonisation-guide), [Elite-Dangerous Fandom](https://elite-dangerous.fandom.com/wiki/System_Colonisation), [Colonization Mega Guide](https://docs.google.com/document/d/1toXyDQglwVACFKx8umXhP8QcMSAUYPcP6k3STIV2-hE/edit) di CMDR Mechan

#### Prosegui la lettura: [Colonizzazione: Capitolo 3 - Economia e link](/blog/colonizzazione-parte3/)
