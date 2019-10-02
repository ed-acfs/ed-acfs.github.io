---
layout: post
title:  "Engineering Workshop: Capitolo 4 - Sensors & Life Support"
date:   2019-10-02
excerpt: "Il quarto capitolo della nostra guida agli Ingegneri di Elite Dangerous - Sensori e Life Support"
image: "/images/posts/engineers-workshop/O8V68Hm.png"
tags: guide ingegneri tutorial
author: bigbadshow
last_modified_at: 2019-09-13
sticky: no
---
Cari comandanti, ben trovati in questo nuovo episodio dell'Engineering Workshop. In questo capitolo continuiamo la nostra corsa alla scoperta dei moduli interni trattando due moduli piuttosto particolari che sono i Sensors ed il Life Support. 

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Questi due moduli sono molto particolari poiché non è possibile montare un modulo di una classe differente da quella di default e, dunque, sarà possibile solo cambiarne il rating. Un'altra caratteristica che accomuna questi due moduli è che l'ingegnerizzazione <b>non prevede l'adozione di effetti speciali</b> e, quindi, potremo contare solamente sull'ingegnerizzazione di base.</div>

Fatte le dovute presentazioni, iniziamo la nostra analisi approfondita partendo dai delicati **Sensors**.

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## Cosa sono i Sensors?

II Sensors sono, letteralmente, i sensori della nostra nave. Vengono utilizzati per tradurre in maniera comprensibile all'occhio umano tutto ciò che ci circonda e che viene presentato sul radar al centro della postazione di comando. I sensors consentono, inoltre, di avere accesso al pannello delle comunicazioni e di scansionare i vascelli a portata, dandoci una visuale di massima del loro outfitting interno e ci danno la possibilità di comunicare con le stazioni per il docking. Ultima, ma non meno importante, funzione dei sensori è quella di dare alle armi gimballed e turretted il puntamento di cui hanno bisogno per funzionare correttamente.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Un mito da sfatare è che il puntamento delle armi migliori a seconda del rating dei sensori. Questo è da considerarsi assolutamente falso visto che i sensori si occupano, come detto, del puntamento ma non si occupano della precisione dello stesso che è standard per tutte le armi.</div>

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## Caratteristiche dei Sensors

I Sensors sono disponibili in classi predeterminate e dipendenti dalla nave. L'unica cosa che possiamo scegliere è il rating che, nella maggior parte dei casi, corrisponde a queste specifiche:

### Rating E

Pesanti come i moduli di rating C ed A ma molto meno potenti e parchi nel consumo di corrente. Il loro scan range è, di norma uguale ai 2/3 di un modulo di rating A

### Rating D

I più leggeri in assoluto, pesanti meno della metà di un modulo di rating A, C ed E. Il consumo in termine di power draw è leggermente più alto rispetto ad un modulo di rating E ed uno scan range superiore del 12,5%

### Rating C

Una curiosa via di mezzo dal peso identico ai moduli di classe E ed A, con un consumo di energia tollerabile e con uno scan range esattamente a metà strada tra i moduli E ed A.

### Rating B

I più pesanti e con l'integrità maggiore di tutte. Questo modulo blindato pesa circa il 54% in più rispetto ad i moduli di rating A, B e C, assorbe circa il 45% in meno di corrente rispetto ad un modulo rating A ed ha, sempre nei confronti di quest'ultimo, uno scan range dell'8,3% inferiore

### Rating A

Indubbiamente i moduli più performanti in termini di scan range ma anche i più esosi in termini di assorbimento di energia e dal peso identico ad un modulo rating C ed E. Per fare un esempio pratico, se un modulo classe 1 rating B, assorbe 0.33MW, l'omologo classe A assorbe 0.6MW.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;La classe predeterminata dei Sensors disponibili che va a determinare un range di peso, scan range ed assorbimento di energia commisurato per ogni nave</div>

## La scelta dei Sensors, calcoli alla mano

Adesso, facciamo una piccola analisi per questo particolare modulo visto che non sempre la scelta di un modulo di classe A risulta essere la scelta migliore. Fatte le dovute premesse nell'introduzione andiamo a prendere gli esempi di tre navi molto popolari che possono montare tre classi di sensori differenti.

### Sidewinder

Prima nave che analizzeremo sarà quel ferro vecchio del Sidewinder sul quale quasi tutti abbiamo mosso i nostri primi passi nella galassia di Elite Dangerous.

Il Sidewinder può montare Sensors esclusivamente di classe 1 e questi sono i dati relativi ai differenti rating:

| **Rating** | **Peso (T)** | **Power Draw (MW)** | **Scan Range (KM)** | **KM/MW** | **KM/T** |
| :---: | --- | :---: | ---: | ---: | ---: |
| **E** | 1,30 | 0,16 | 4,00 | 25,00 | 3,08 |
| **D** | 0,50 | 0,18 | 4,50 | 25,00 | 9,00 |
| **C** | 1,30 | 0,20 | 5,00 | 25,00 | 3,85 |
| **B** | 2,00 | 0,33 | 5,50 | 16,67 | 2,75 |
| **A** | 1,30 | 0,60 | 6,00 | 10,00 | 4,62 |

<div class="box">
<i class="fa fa-lightbulb-o fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Tech Tip:</b>&nbsp;Questa tabella ci fa saltare subito all'occhio che i moduli di classe E, D e C sono i moduli che hanno il miglior rapporto di distanza in KM per energia assorbita in MW e, inoltre, ci fa vedere come il miglior rapporto di distanza in KM per peso in T sia il modulo di classe D</div>

### ASP Explorer

Continuiamo analizzando i dati della seconda nave presa in esame che è il sempreverde ASP Explorer. Sebbene la sua efficacia sia stata oscurata dall'avvento del Krait Phantom, l'ASP Explorer gode ancora di una certa popolarità e, quantomeno, è rimasta nel cuore di parecchi comandanti. L'ASP Explorer può montare Sensors di classe 5 e questi sono i dati relativi a questa classe:

| **Rating** | **Peso (T)** | **Power Draw (MW)** | **Scan Range (KM)** | **KM/MW** | **KM/T** |
| :---: | --- | :---: | ---: | ---: | ---: |
| **E** | 20,00 | 0,33 | 4,64 | 14,06 | 0,23 |
| **D** | 8,00 | 0,37 | 5,22 | 14,11 | 0,65 |
| **C** | 20,00 | 0,41 | 5,80 | 14,15 | 0,29 |
| **B** | 32,00 | 0,68 | 6,38 | 9,38 | 0,20 |
| **A** | 20,00 | 1,23 | 6,96 | 5,66 | 0,35 |

<div class="box">
<i class="fa fa-lightbulb-o fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Tech Tip:</b>&nbsp;Per quanto riguarda i rapporto distanza in KM su energia in MW, anche in questo caso i moduli rating E, D e C praticamente si equivalgono con un vantaggio di un centinaio di metri a favore di quest'ultimo. Fanalino di coda, come al solito, il modulo di rating A. Mentre nel rapporto distanza in KM e peso in T è, ovviamente, confermata la supremazia del modulo di rating D con all'ultimo posto il modulo di rating B. Quest'ultimo ricordiamolo ha sempre un'integrità 49% maggiore rispetto ad un modulo di rating D</div>

### Anaconda

L'ultima nave che andremo ad analizzare è la titanica e sempre amata Anaconda, nave estremamente versatile che è da considerarsi la multiruolo per eccellenza ed avente un bilanciamento globale tra pro e contro non indifferente. L'Anaconda può montare Sensors esclusivamente di classe 8, quindi i più massicci ed esosi in termini energia di tutti:

| **Rating** | **Peso (T)** | **Power Draw (MW)** | **Scan Range (KM)** | **KM/MW** | **KM/T** |
| :---: | --- | :---: | ---: | ---: | ---: |
| **E** | 160,00 | 0,55 | 5,12 | 9,31 | 0,03 |
| **D** | 64,00 | 0,62 | 5,76 | 9,29 | 0,09 |
| **C** | 160,00 | 0,68 | 6,40 | 9,41 | 0,04 |
| **B** | 256,00 | 1,14 | 7,04 | 6,18 | 0,03 |
| **A** | 160,00 | 2,07 | 7,68 | 3,71 | 0,05 |

<div class="box">
<i class="fa fa-lightbulb-o fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Tech Tip:</b>&nbsp;Se dal punto di vista del rapporto distanza in KM su energia assorbita restiamo sempre sul classico vantaggio dei moduli E, D e C, vediamo che il modulo di rating E perde decisamente terreno andandosi a pareggiare come rapporto ai più pesanti e massicci moduli di rating B</div>

Probabilmente, arrivati a questo punto, sarete tutti abbastanza confusi. Mi stupirei del contrario. Diciamo che, calcoli alla mano, **più il modulo Sensors è piccolo e più esso sarà efficiente**. Ovviamente ciò è stato rapportato alla Power Plant visto che, giustamente, un Sidewinder non può montare una Power Plant classe 8 rating A che ha una massa superiore a alla nave stessa. Ma ciò che ,veramente, salta all'occhio è come all'aumento della classe non coincida un aumento lineare delle performance.

>Nella maggior parte dei casi il modulo da adottare che mi sento di consigliare è **quello che eccelle in tutte le specifiche**. Di norma, anche nelle guide precedenti, non consiglio mai una classe o un rating specifico ma in questo caso è diverso. Per ciò che mi concerne, **tutte le mie navi sono equipaggiate con sensori rating D**. 

Dall'esploratore alla nave da combattimento, **il modulo leggero offre un ottimo compromesso** per mantenere agilità e distanza di scansione. Comunque ci sono alcune eccezioni in cui è preferibile usare un modulo di un rating differente, ma ne parleremo alla fine di questa guida. 

<div class="box">
<i class="fa fa-lightbulb-o fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Tech Tip:</b>&nbsp;Un'ultima nota è che per tutte le classi e tutti i rating il valore di angolo di scansione (Scan Angle) è identico. L'angolo, di default di 27.5 gradi, è considerato dal punto centrale della nave quindi qualunque nave o corpo celeste capiti in un angolo rispetto alla vostra nave di 27,5 potrà essere scansionata una volta targettizzata.</div>
<sup><b>Attenzione:</b> lo scan angle riguarda l'area in cui possiamo scansionare un oggetto e non l'area in cui lo possiamo tenere a tiro o targettizzare. Ricordate che NON INFLUENZA la targettizzazione e le armi.</sup>

## Quali ingegneri modificano i Sensors?

Abbiamo la bellezza di **sette ingegneri** che si prodigano nella modifica di questo essenziale modulo e nello specifico sono:

| Nome                	| Grado massimo 	|
|---------------------	|:-------------:	|
| Bill Turner           | G5                |
| Felicity Farseer      | G3                |
| Hera Tani             | G3                |
| Juri Ishmaak          | G5                |
| **Lei Cheung**        | **G5**            |
| **Lori Jameson**      | **G5**            |
| Tiana Fortune         | G5                |

Chi consigliare? Difficile a dirsi perché dipende anche da quali e quanti ingegneri avete sbloccato e quali modifiche avete pinnato. Supponendo di aver fatto il viaggio a Colonia per sgravare la beneamata [Lori Jameson](/blog/speedguide-ingegneri-appendice/#lori-jameson) del compito di ingegnerizzare Life Support e Shield Cell Banks e che abbiate almeno un livello Elite in un delle discipline, l'ideale potrebbe essere proprio la Signora in questione anche se **Shinrarta Dezhra** è tristemente famoso per l'eccessiva presenza di ganker e psicolabili che hanno necessità di ricordare la loro mascolinità con azioni deplorevoli. Altrimenti, viabile, è anche [Lei Cheung](/blog/speedguide-ingegneri-parte1/#sesto-passo-lei-cheung) che ha il vantaggio di ingegnerizzare in G5 anche gli Shield Generators.

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## Ingegnerizzare i Sensors

Come abbiamo detto precedentemente detto, i Sensors sono una componente imprescindibile della nave e fanno parte di quei moduli detti &quot;core&quot; che non è possibile mai rimuovere completamente. È necessario avere ben chiaro che un'ingegnerizzazione dei sensori porta ad una serie di pro e contro non indifferente e, pertanto, è necessario valutare bene caso per caso. Addirittura, data la particolarità di questi moduli, a volte potrebbe non essere necessaria nessuna ingegnerizzazione e lasciare il modulo così come esce &quot;di fabbrica&quot; poiché i contro potrebbero andare a creare uno squilibrio nella nave tale da inficiarne il rendimento globale. Quindi, la domanda che vi dovete porre prima di iniziare l'ingegnerizzazione è una soltanto: _"i pro, superano i contro?"_

Possiamo contare su **tre diverse ingegnerizzazioni** che consentiranno di avere vantaggi ma, ahinoi, anche importanti svantaggi. Le ingegnerizzazioni disponibili sono:

- Lightweight
- Wide Angle
- Long Range

## Lightweight

Questa modifica consente di **diminuire la massa totale del modulo** fino ad un massimo dell'80% in meno. Di contro il nostro modulo si troverà con il **75% in meno di integrità** e lo scan angle diminuirà del 30%.

#### Quando usare questa modifica?

Il lightweight è una delle modifiche più utilizzate dagli esploratori e, sempre più spesso, anche da chi decide di dedicarsi al combat. Diminuendo la massa, soprattutto su dei moduli di classe D e soprattutto su navi grandi, il peso complessivo della nave scende vertiginosamente andando ad aumentare notevolmente l'agilità del nostro vascello. Non è da sottovalutare neanche nei casi dell'imponente ed altrettanto agile **Federal Corvette** la quale, grazie ad una importante diminuzione di peso, tenderà a tenere &quot;on target&quot; maggiormente le navi nemiche.

Il vantaggio, in termini esplorativi, mi sembra molto più che ovvio. Per quanto alcuni esploratori preferiscano sacrificare jump range per avere notevoli vantaggi in scansione, altri preferiscono sacrificare questi vantaggi ed avere maggiore capacità di salto per spingere la propria nave all'estremo. Non mi preoccuperei molto della diminuzione di integrità visto che i sensors sono spesso ben protetti sulle navi sulle navi e, un eventuale attaccante, mirerà sicuramente verso altri moduli più sensibili in combat. La distanza di scansione nello spazio normale, non viene intaccata da questa modifica.

### Materiali Richiesti

- **G1**: 1x Phosphorus
- **G2**: 1x Manganese – 1x Salvaged Alloys
- **G3**: 1x Conductive Ceramics – 1x Manganese – 1x Salvaged Alloys
- **G4**: 1x Conductive Components – 1x Phase Alloys – 1x Proto Light Alloys
- **G5**: 1x Conductive Ceramics – 1x Proto Light Alloys – 1x Proto Radiolic Alloys

## Wide Angle

Questa modifica consente di **aumentare lo scan angle** dei sensori fino al 200% in più andando a sacrificare la distanza massima fino ad un 40% in meno ed andando ad **aumentare il power draw** fino al 100%.

#### Quando usare questa modifica?

Se il lightweight è una modifica che consente di diminuire avere vantaggi in termini di peso, qui ci troviamo di fronte ad una modifica che ci consente di avere un occhio più &quot;aperto&quot; su una vasta superfice di fronte a noi. 
Certo, ciò potrebbe risultare interessante se stessimo al comando di una nave da caccia per scansionare le navi che ci sono intorno e raccogliere preziosi dati e rintracciare in fretta navi wanted. Di certo, dobbiamo considerare che si dimezza la profondità di scansione, con un G5 completo, e che l'assorbimento di corrente raddoppia. 

In questo caso, forse, la verità sta nel mezzo ed un G5 ci costringerebbe a troppi compromessi, mentre un G3 full sarebbe un'interessante via di mezzo garantendoci un 120% in più di scan angle e non andando a ledere troppo profondità di scansione e power draw.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Per quanto riguarda la classe consigliata, dobbiamo considerare che lo scan angle è uguale per tutti e quindi ciò che andiamo a perdere e la distanza. Va da se che questo tipo di ingegnerizzazione si sposa perfettamente con i moduli di rating A visto che sono quelli con la maggiore distanza di scansione. Ma attenzione che un G5 full, porterà la distanza di scansione a meno di 4km.</div>

### Materiali Richiesti

- **G1**: 1x Mechanical Scrap
- **G2**: 1x Germanium – 1x Mechanical Scrap
- **G3**: 1x Classified Scan Databanks – 1x Germanium – 1x Mechanical Scrap
- **G4**: 1x Divergent Scan Data – 1x Mechanical Equipment – 1x Niobium
- **G5**: 1x Classified Scan Fragment – 1x Mechanical Components – 1x Tin

## Long Range

Se il wide angle ci dà maggiore visibilità laterale, il long range è quella modifica che ci consente di **scansionare più in profondità** fino al 75% in più rispetto allo standard. Di contro ci troveremo una **massa aumentata fino al 100%** ed una **perdita dello scan angle** fino al 60%.

##### Quando usare questa modifica?

Numeri alla mano, il long range è una delle modifiche più inutili che si possano dare ai sensors. Di norma non sono così duro con una modifica ma il long range veramente tira fuori il peggio di me. I sensors, come detto in precedenza, hanno uno scan angle di 27,5 gradi. Questa modifica G5 lo riduce del 60% lasciandoci praticamente con la possibilità di scansionare un punto di pochi gradi oltre il centro della nostra nave. Tutto ciò senza considerare l'inutilità di scansionare navi a così ampia distanza. 

Certo, con un modulo rating A arriveremo a quasi 14km di scansione del nostro obiettivo ma, se pensiamo ad una nave da combattimento, anche le migliori armi a lunga gittata ingegnerizzate non arrivano a quella distanza. Il tutto senza considerare l'abnorme aumento di massa. Un'utilità? Forse solamente se vogliamo scansionare qualcuno da enorme distanza e darcela a gambe se vediamo che si avvicina e non abbiamo sufficiente potenza di fuoco per combatterlo. Un modulo rating A ha già sufficiente capacità di scansione.

### Materiali Richiesti

- **G1**: 1x Iron
- **G2**: 1x Hybrid Capacitors – 1x Iron
- **G3**: 1x Hybrid Capacitors – 1x Iron – 1x Unexpected Emission Data
- **G4**: 1x Decoded Emission Data – 1x Electrochemical Arrays – 1x Germanium
- **G5**: 1x Abnormal Compact Emissions Data – 1x Niobium – 1x Polymer Capcitors

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## Cosa è il Life Support?

Il Life Support, o supporto vitale, è quel particolare sistema cruciale della nave che ha il compito di generare all'interno del vascello un'atmosfera respirabile. In caso di rottura del canopy - il meraviglioso vetro che ci consente di vedere cosa succede ad occhio fuori dalla nostra nave e che ci separa dal vuoto cosmico - il Life Support provvederà a fornire al nostro avatar una certa quantità di ossigeno per consentirci di raggiungere un porto sicuro quanto prima.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;La durata dei minuti di ossigeno fornito dal supporto vitale è variabile a seconda del rating del modulo e va da un <b>minimo di 5 minuti</b> ad un <b>massimo di 25 minuti</b>.</div>

Ovviamente, la rottura del canopy non solo ci mette in difficoltà perché ci espone a viso scoperto con l'immensità del nostro universo, ma ci toglie anche le basi di controllo di navigazione che ci facilitano il compito di viaggiare nello spazio lasciandoci, come unico riferimento, la nostra fidata bussola.

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## Caratteristiche del Life Support

Così come per i Sensors, anche il Life Support è disponibile in classi predeterminate e non sostituibili a seconda della nave e del quale possiamo scegliere solamente il rating che va a modificare la massa del modulo e la riserva di ossigeno disponibile:

### Rating E

Sono i moduli standard del life support, pesanti quanto i moduli C ed A hanno una **riserva di 5 minuti**.

### Rating D

I più leggeri in assoluto riescono a fornire ossigeno per **7 minuti e 30 secondi** dalla rottura del canopy o dalla disattivazione del sistema.

### Rating C

La via di mezzo per chi vuole star sicuro. Dal peso identico ai moduli E ed A, fornisce ossigeno per **10 minuti**.

### Rating B

I più pesanti in assoluto ed anche i più solidi. Forniscono ossigeno per **20 minuti**.

### Rating A

In assoluto i moduli più performanti con la possibilità di fornire **ossigeno per 25 minuti**. A patto che riusciate ad uscire vivi dalla situazione di emergenza e che non vogliate raggiungere Hutton Orbital, questi moduli forniscono tutta la sicurezza che state cercando in termini di atmosfera respirabile.

## La scelta del Life Support

Facciamo un paio di considerazioni. Dall'alba dei tempi della fantascienza, ci viene insegnato che il supporto vitale è uno dei sistemi critici della nave, nonché il più importante e quello che può fare la differenza tra la vita e la morte. In Elite Dangerous non è molto differente poiché, se terminiamo l'ossigeno, ci ritroveremo davanti alla nostra bella schermata di rebuy. La differenza tra i vari life support la fa solamente la loro riserva di ossigeno ed il peso, nell'economia della nave. Integrità e power draw sono abbastanza risibili.

Per tutti, in linea di massima, la scelta ideale è quella di un modulo di rating D poiché esso ci consente di sopravvivere nel vuoto siderale per più di sette minuti ed ha un peso estremamente contenuto. Tuttavia, se questo va bene per comandanti navigati, almeno per i principianti potrebbe essere una buona cosa l'avere a disposizione una riserva maggiore di ossigeno, in caso di rottura del canopy, e quindi adottare un modulo di rating C o, meglio ancora A.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Perché non i B? Per via del loro peso abnorme che renderebbe impacciata anche la più piccola delle navi. Ormai sappiamo bene che il peso è il nemico numero uno dell'agilità.</div>

## Quali ingegneri modificano il Life Support?

La nota dolente del life support è che solamente tre ingegneri offrono modifiche per questo modulo e tutti e tre hanno requisiti piuttosto alti per accedere ai loro servizi. Inoltre, solamente uno è quello consigliato e, ahinoi, è distante dalla bubble ben 22.000ly essendo residente nell'area di **[Colonia](/search/tag/colonia)**:

| Nome                	| Grado massimo 	|
|---------------------	|:-------------:	|
| Bill Turner           | G3                |
| Lori Jameson          | G4                |
| **Etienne Dorn**      | **G5**            |

Una volta scelta la nostra modifica preferita, prepariamoci ad un bel viaggio fino a Colonia per sbloccare **Etienne Dorn**. Il viaggio è lungo ma ne vale la pena soprattutto perché il G3 di Bill Tuner è piuttosto inutile mentre il G4 di Lori Jameson è pericoloso visto il sistema dove la dolce donzella si trova.

## Ingengerizzare il Life Support

Così come per i sensori abbiamo a nostra disposizione tre tipologie di ingegnerizzazione delle quali tutte non hanno possibilità di applicare nessun effetto speciale. Le modifiche disponibili riguardano, principalmente, il peso e la resistenza del modulo. Quindi è da valutare il tipo di impiego che farete della vostra nave e scegliere l'ingegnerizzazione di conseguenza ed andiamo ad analizzare le varie ingegnerizzazioni disponibili.

## Lightweight

La modifica lightweight è quella modifica in grado di _"mettere a dieta"_ il vostro life support facendogli perdere fino all'80% della sua massa originale. Di contro, anche l'integrità diminuirà in maniera quasi identica scendendo del 60%

#### Quando usare questa modifica?

Per la mia esperienza mi verrebbe da dire: **SEMPRE**. Logicamente, dobbiamo lasciare spazio anche alle altre ingegnerizzazioni. Il lightweight è l'ideale per gli esploratori che vogliono raschiare il fondo del barile dalla loro nave e portarla a jump range estremi. La riduzione della massa, tuttavia, porta anche vantaggi in combattimento dove si va ad aumentare l'agilità della nave.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Così come per i sensors, anche il life support non è un modulo facilmente danneggiabile in battaglia e questo, quindi, rende la modifica lightweight ideale per far guadagnare alle pachidermiche navi large ulteriore agilità o quella agilità di cui hanno bisogno. Per quanto risibile, potrebbe avere effetti benefici anche sul mastodontico <b>Type-9 Heavy</b>.</div>

In tutto questo mi sono reso conto di essermi scordato quale modulo è consigliabile ingegnerizzare ma, visto che parliamo di peso, penso sappiate tutti che il modulo è quello di rating D.

### Materiali Richiesti

- **G1**: 1x Phosphorus
- **G2**: 1x Manganese – 1x Salvaged Alloys
- **G3**: 1x Conductive Ceramics – 1x Manganese – 1x Salvaged Alloys
- **G4**: 1x Conductive Components – 1x Phase Alloys – 1x Proto Light Alloys
- **G5**: 1x Conductive Ceramics – 1x Proto Light Alloys – 1x Proto Radiolic Alloys

## Reinforced &amp; Shielded

Questa volta mettiamo insieme due modifiche e ne parliamo contemporaneamente poiché hanno esattamente il medesimo scopo ma con drawback differenti. Ambedue, infatti, hanno come unico obiettivo quello di aumentare l'integrità del life support, guadagnando fino al 300% rispetto all'integrità base. Come già detto l'unica cosa che si differenzia è il drawback dove nel caso del **Reinforced** avremo un **aumento di massa del 150%** e nel caso dello **Shielded** un **aumento del power draw** del 100%

#### Quando usare queste modifiche?

Ambedue le modifiche sono direttamente indirizzate verso le navi da battaglia ma di due tipologie differenti. Ammesso e non concesso che siate così puntigliosi da non voler lasciare nessun punto debole sulla vostra nave, dovete prima rendervi conto a livello di economia globale quale delle due ingegnerizzazioni potete permettervi.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;In termini molto semplici, tutto dipende dall'agilità della nave e dalla power plant che avete disponibile.<ul>
<li>Sicuramente su una nave con problemi cronici di gestione dell'energia come il <b>Vulture</b>, sarà il caso di adottare una modifica <b>Reinforced</b> visto che, in linea di massima, la nave resterà comunque agile e scattante.</li>
<li>Se invece avete un bel setup di armi a proiettili e siete fieri possessori di una <b>Federal Corvette</b>, un aumento di consumo di power draw potrete sicuramente permettervelo ed andare sereni con l'ingegnerizzazione <b>Shielded</b>.</li></ul></div>

Per questa modifica il mio consiglio è di puntare su **moduli rating A**. Lasciate perdere i moduli B visto che hanno un peso abnorme ed una integrità inferiore.

### Materiali Richiesti: Reinforced

- **G1**: 1x Nickel
- **G2**: 1x Nickel – 1x Shield Emitters
- **G3**: 1x Nickel – 1x Shield Emitters – 1x Tungsten
- **G4**: 1x Zinc – 1x Tungsten – 1x Molybdenum
- **G5**: 1x High Density Composites – 1x Molybdenum 1x Technetium

### Materiali Richiesti: Shielded

- **G1**: 1x Worn Shield Emitters
- **G2**: 1x Carbon – 1x Shield Emitters
- **G3**: 1x Carbon – 1x Shield Emitters – 1x High Density Composites
- **G4**: 1x Vanadium – 1x Shielding Sensors – 1x Prorietary Composites
- **G5**: 1x Tungsten – 1x Compound Shielding – 1x Core Dynamics Composites

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

### Chiacchiere e Considerazioni

Abbiamo visto due moduli particolari strettamente legati alla nave e con pochissima possibilità di scelta. Due moduli che spesso vanno a braccetto anche se non hanno funzioni direttamente collegate. La logica dietro questi moduli è molto semplice ma non è, comunque, facile dare una scelta scontata di un rating rispetto ad un altro. Nel corso della mia esperienza nella galassia di Elite Dangerous ho avuto modo di apprendere quando e dove i moduli di rating A sono superflui. Ma andiamo con ordine:

- Per quanto concerne i sensori, all'inizio, ero un fervente sostenitore dei moduli di rating A poiché fermamente convinto che il puntamento della armi gimballed dipendesse da esso e non riuscivo a capacitarmi di come si potesse combattere con un angolo di scansione più basso od una distanza più breve. Mai sbagliato così tanto in vita mia. La mia ammiraglia si è portata appresso ben **160 tonnellate di sensori bellamente inutili** per poi essere sostituiti con dei moduli lightweight pesanti appena **12.8 tonnellate**. Diciamo un bel po' in meno che ne ha migliorato in maniera drammatica l'agilità.<br>
Certo, all'inizio è stato un po' difficile, soprattutto nelle Haz Res, scansionare i vascelli di eventuali pirati, ma a tutto ci si abitua ed il puntamento delle armi non è cambiato di una virgola. Quindi, a meno che non siate estremamente fissati o a meno che non vogliate fare un pachidermico hull tank, mirate senza problemi ai moduli rating D e vivete tranquilli, leggeri ed agili.

- Per il life support, ricordo ancora la prima volta che saltò il mio canopy ed il panico in cui mi sono trovato. Essere a tu per tu con lo spazio non è una cosa gradevole e navigare a vista senza l'HUD ad aiutare è un esperienza agrodolce, meravigliosa da una parte, terrificante dall'altra. Certo è che i 7 minuti e 30 secondi del modulo di rating D sono stati più che sufficienti per darmela a gambe e raggiungere la prima stazione disponibile. Dopo questa esperienza di vita vissuta, traete voi le vostre conclusioni. Indubbiamente un modulo di rating C o A, vi dona molto tempo in più ma dovete anche considerare il fattore peso. Tra un modulo rating A lightweight ed uno di rating D lightweight, sull'Anaconda, corrono circa 1.8 tonnellate a vantaggio del più modulo di rating più basso.<br>
Per un esploratore, indubbiamente, anche quel peso può fare la differenza. Per una nave da combattimento, forse, è un peso sacrificabile per avere un minimo di sicurezza in più, soprattutto se i combattimenti avvengono in zone remote o se vogliamo mettere più anni luce possibili tra noi ed i nostri inseguitori.

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

#### Fine della quarta parte. Continuate a seguirci con i prossimi capitoli
