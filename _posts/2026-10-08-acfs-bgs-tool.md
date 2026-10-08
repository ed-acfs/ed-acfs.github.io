---
layout: post
title:  "ACFS BGS Tool: come è nato in quattro giorni il nostro strumento per il BGS"
date:   2026-10-08
excerpt: "Quasi 400 sistemi da seguire e una domanda che torna ogni giorno dopo il tick: dove lavoriamo oggi? Ecco la storia dell'ACFS BGS Tool, lo strumento per il BGS di Elite Dangerous nato in quattro giorni grazie al lavoro dei Canonn e a un assistente AI, e già diventato il punto di riferimento dello Squadrone."
image: "/images/posts/acfs-bgs-tool/tool.png"
tags: bgs flotta-stellare squadrone tecnica
author: wiitifulsky
last_modified_at: 2026-10-08
sticky: no
---
<div class="box alt">
<p>8 Ottobre 3312<br>
Cronaca Galattica dell'Alto Comando Flotta Stellare</p>

<p>Wong Sher, Capitale della Flotta Stellare</p>
</div>

<span class="image fit"><img src="/images/posts/acfs-bgs-tool/tool.png" alt="La tabella dell'ACFS BGS Tool con i sistemi di Flotta Stellare ordinati per priorità"></span>

Chi fa [BGS](/bgs/) lo sa: ogni giorno, appena passa il tick, c'è sempre la stessa domanda. **Dove lavoriamo oggi?**

Per uno squadrone piccolo la risposta si trova in fretta. Per noi no. [Flotta Stellare](/about/) è presente in quasi 400 sistemi e ne controlla più di 250: dieci anni di espansioni, alleanze e, da qualche mese, [colonizzazione](/blog/colonizzazione-parte1/). Rispondere a quella domanda voleva dire aprire Inara, poi Spansh, poi il nostro foglio di monitoraggio con i suoi semafori, confrontare le percentuali sistema per sistema e infine scrivere a mano gli ordini del giorno su Discord. Un lavoro lungo, e soprattutto un lavoro che si rifaceva da capo ogni giorno.

Da questa settimana abbiamo un'alternativa: l'**[ACFS BGS Tool](https://flottastellare.it/acfs-bgs-tool/)**. In quattro giorni è passato da idea a strumento che lo Squadrone usa ogni mattina. Questa è la sua storia.

## Tutto parte dai Canonn

Il merito iniziale non è nostro. Il **Canonn Research Group**, che molti di voi conoscono per la ricerca scientifica e che è anche nostro vicino nei settori di Lyncis, aveva pubblicato il proprio strumento per seguire il BGS delle colonie, *Canonn Colony Operations*. Era un buon lavoro, ed era pubblicato con una licenza libera: chiunque poteva prenderlo e adattarlo.

È quello che abbiamo fatto. Sabato 4 ottobre abbiamo preso il loro codice e abbiamo cominciato a trasformarlo: via le loro fazioni e i loro sistemi, dentro Flotta Stellare, Wong Sher come capitale, l'italiano, il logo Vanguards. A loro va il nostro grazie, e i crediti restano scritti nel progetto.

## Un'idea, un Ammiraglio e un assistente AI

C'è una cosa che vale la pena raccontare, perché fa parte della storia. Non sono un programmatore di professione, e scrivere da solo uno strumento del genere avrebbe richiesto mesi di serate. Il tool l'ho costruito insieme a **Claude Code**, un assistente di intelligenza artificiale che scrive codice.

Il lavoro funzionava più o meno così: io spiegavo cosa serviva allo Squadrone e come funziona il BGS, l'assistente scriveva il codice e lo provava, io lo guardavo girare e decidevo se andava bene. Spesso non andava bene al primo colpo, e si ricominciava. Le decisioni sono sempre rimaste nostre: la scala di priorità da **P1** (massima) a **P5**, le soglie dei semafori prese dal nostro documento di monitoraggio, la regola che *un conflitto è sempre prioritario*, la scelta di mostrare apertamente quanto è vecchio ogni dato invece di fingere che sia sempre aggiornato.

Il risultato è stato un ritmo che non avrei mai immaginato:

- **sabato 4 ottobre**: i dati di Flotta Stellare caricati da Spansh, l'interfaccia in italiano, il calcolo della priorità, il registro degli Architetti. In serata il tool era già online;
- **domenica 5 ottobre**: aggiornamento automatico ogni mezz'ora, il contatore dei sistemi aggiornati dopo il tick, la Legenda, la distanza da qualsiasi sistema e gli **Ordini Ufficiali**, lo strumento interno con cui gli ufficiali compongono il report del giorno per Discord;
- **lunedì 6 ottobre**: la versione per il telefono, i Material Trader e i Technology Broker con il loro tipo, il preavviso di Retreat e l'avviso quando un'altra fazione si avvicina a 5 punti dalla nostra;
- **martedì 7 ottobre**: la **versione 1.0**, anche in tedesco e in inglese, e subito dopo la 1.1 con una priorità più ragionata.

## Cosa vede chi lo apre

L'idea è semplice: una tabella con tutti i nostri sistemi, ordinata per **priorità**. In cima ci sono quelli dove serve lavorare oggi, in fondo quelli tranquilli. Per ogni sistema il tool mostra:

- chi lo controlla e l'influenza di tutte le fazioni presenti, con la barra di Flotta Stellare in arancione;
- la nostra influenza e il **margine**, cioè il vantaggio sulla seconda fazione dove controlliamo, o il distacco da chi controlla dove non lo facciamo, con gli stessi semafori verde, giallo e rosso che usiamo da anni;
- guerre, elezioni e ritirate, in corso o in arrivo: cliccando l'icona si vedono le fazioni coinvolte;
- l'architetto e la fazione preferita dei sistemi colonizzati;
- quanto è vecchio il dato.

Ogni priorità ha una spiegazione: passando sopra il badge il tool dice *perché* quel sistema è in P1 o in P4. È la parte a cui tengo di più, perché uno strumento che dà ordini senza spiegarli non insegna niente a nessuno.

<div class="box">
<i class="fa fa-lightbulb-o fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Un esempio di come è cresciuto:</b>&nbsp;nei primi giorni il tool dava <b>SPOCS 253</b> in P5, "tutto tranquillo", proprio accanto a due semafori rossi: 35,7% di influenza e appena 15,6 punti di vantaggio. Una contraddizione che saltava all'occhio. Dalla versione 1.1 i semafori contano anche nella priorità, e quel giorno 32 sistemi sono saliti di fascia. Nessuno è sceso.
</div>

## Onesto sui propri limiti

Il tool non vede il gioco. Legge **Spansh**, che a sua volta si aggiorna con i dati inviati dai piloti che volano con programmi come EDMC o EDDiscovery. Se nessuno passa in un sistema, il dato invecchia. Per questo ogni riga dice quanto è vecchia, e sotto il titolo un contatore indica quanti sistemi sono stati aggiornati dopo l'ultimo tick.

Lo stesso vale per il punteggio dei conflitti, i giorni vinti in una guerra o in un'elezione. Spansh non lo riporta. Il tool lo chiede a EliteBGS, che però in questi giorni è quasi sempre fuori servizio: quando non risponde, il riquadro del conflitto rimanda a Inara. Meglio un rimando onesto che un numero inventato.

<div class="box">
<i class="fa fa-rocket fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Come potete aiutare:</b>&nbsp;se volate con <a href="https://github.com/EDCD/EDMarketConnector">EDMC</a> o EDDiscovery attivi, ogni salto in un nostro sistema aggiorna anche il tool. Dopo il tick, passare nei sistemi in P1 e P2 ancora "vecchi" è uno dei modi più semplici per dare una mano allo Squadrone.
</div>

## Anche per gli amici, in tre lingue

Il tool è pubblico: chiunque può aprirlo e vedere come stiamo. Pochi giorni dopo l'uscita il link è arrivato a un comandante tedesco, e così la parte di consultazione ora parla **italiano, tedesco e inglese**. Alla prima visita segue la lingua del browser, poi basta una bandierina in alto per cambiarla. Gli strumenti interni dello Squadrone, come gli Ordini e la registrazione degli Architetti, restano in italiano e protetti da password.

## Cosa arriva adesso

In pochi giorni il tool è diventato il primo posto in cui guardiamo dopo il tick, e gli ordini del giorno ormai nascono lì. Ma il lavoro non è finito. Fra le prossime idee:

- un **report automatico su Discord** dopo ogni tick, con i sistemi da seguire, le nuove guerre ed elezioni e i controlli persi o conquistati;
- una **"pattuglia"**: l'elenco dei sistemi importanti ancora fermi a prima del tick, da girare a chi è in volo;
- la [mappa 3D](/map/) del sito che legge direttamente i dati del tool, così resta sempre aggiornata da sola.

Nel frattempo il tool vi aspetta qui: **[flottastellare.it/acfs-bgs-tool](https://flottastellare.it/acfs-bgs-tool/)**. Apritelo, giocateci, e se qualcosa non vi torna ditecelo su Discord: molte delle novità di questi giorni sono nate proprio così.

> Per anni il BGS della Flotta si è fatto con fogli di calcolo, schede aperte e tanta memoria. Oggi abbiamo una tabella che si aggiorna da sola. La domanda però è sempre la stessa: dove lavoriamo oggi? o7
