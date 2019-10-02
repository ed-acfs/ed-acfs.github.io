---
layout: post
title:  "Engineering Workshop: Capitolo 3 - Power Plant"
date:   2019-09-13
excerpt: "Il terzo capitolo della nostra guida agli Ingegneri di Elite Dangerous - Conosciamo la Power Plant"
image: "/images/posts/engineers-workshop/engineers-page-ed3-0.jpg"
tags: guide ingegneri tutorial
author: bigbadshow
last_modified_at: 2019-10-02
sticky: no
---
In questo nuovo capitolo andremo a trattare di una componente estremamente delicata e fondamentale delle nostre navi, che viene spesso male interpretata e, altrettanto spesso, genera confusione soprattutto tra i giovani Comandanti. L'obiettivo è quello di capire bene il suo funzionamento e come l'ingegnerizzazione vada a modificare le sue peculiarità, analizzandone vantaggi e svantaggi.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;La Power Plant (PP) va spesso a braccetto con il Power Distributor (PD) ma bisogna sempre considerare che sono due componenti slegate con funzioni diverse. Nello specifico la PP si occupa di generare energia, il PD si occupa di immagazzinare questa energia e renderla disponibile ai sistemi fondamentali, esattamente come farebbe una grossa batteria.</div>

 Fatte le doverose premesse, procediamo quindi in un'analisi dettagliata della PP.

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## Cosa è la Power Plant?

La PP è il reattore nucleare che genera energia consumando carburante (idrogeno) e convertendolo in calore che viene utilizzato per generare energia misurata in Watt (W).<br>
Esattamente come ogni macchina, la PP non è perfetta e parte della reazione viene rilasciata sotto forma di calore misurato; da qui si dice che una PP ha più o meno **Heat Efficiency**.

Le PP vengono suddivise in **Classi** (da 2 a 8) con diverse erogazioni di potenza ed ulteriormente suddivise in **Rating** (da E ad A) con diversa efficienza. Questa efficienza, come detto in precedenza, è nota come Heat Efficiency e viene identificata da un valore che va **da 1 a 0.40**.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;ad un valore più piccolo corrispondono una maggiore efficienza ed un minore calore generato.
<p>Ad esempio, un modulo di classe E avrà standard una <b>Heat Efficiency di 1</b>, mentre un modulo A la avrà di <b>0.40</b>, generando più corrente ed avendo meno calore da disperdere.</p></div>

La PP rappresenta, purtroppo, anche la parte più sensibile dell'intera nave. Se la sua integrità raggiunge lo zero, *indipendentemente da quanta integrità strutturale abbiamo*, la nostra nave esploderà poiché la reazione nucleare all'interno della PP non potrà più essere contenuta.<br>
In battaglia, una strategia efficace è quella di mirare alla PP nemica che è, in alcune navi, particolarmente esposta e sensibile agli attacchi. La PP, inoltre, non può essere riparata tramite AFMU.

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## Caratteristiche delle Power Plant

### Rating E

Estremamente poco heat efficient (HE=1) e pesanti quanto i moduli di classe C ed A, sono le PP che **generano più calore e rendono meno di tutte**. Liberatevene al più presto.

### Rating D

**Le più leggere in assoluto** ma con un heat efficient leggermente migliore rispetto agli inutili E (HE=0.75). Generano mediamente più corrente e sono una soluzione da valutare per **esploratori a corto/medio raggio**.

### Rating C

Mediamente efficienti (HE=0.5) e mediamente potenti con un peso identico ai moduli di classe E e classe A. Utilizzare questa classe di moduli è, per l'appunto, mediamente inutile poiché si trovano nel mezzo come il mercoledì e non sono né carne né pesce.

### Rating B

**Pesanti il doppio** rispetto ai moduli di classe A, C ed E, con una integrità ottima e buona efficienza (HE=0.45) ed erogazione di potenza, queste PP corazzate sono ideali per chi desidera **andare in battaglia** senza il pensiero di perdere il modulo.

### Rating A

Dal peso nella media ma con una **eccellente heat efficiency** (HE=0.40) ed un'erogazione di potenza senza pari, sono una scelta viabile non solo in battaglia ma anche in esplorazione dove, sacrificando un po' di peso, si guadagna tantissimo nell'efficienza termica.

Per quanto riguarda inve le **potenze erogate standard** possiamo sintetizzare in questo modo:

| Classe 	| Potenza min 	| Potenza max 	|
|:------:	|------------:	|------------:	|
|    2   	|       6,4MW 	|       9,6MW 	|
|    3   	|         8MW 	|        12MW 	|
|    4   	|      10,4MW 	|      15,6MW 	|
|    5   	|      13,6MW 	|      20,4MW 	|
|    6   	|      16,8MW 	|      25,2MW 	|
|    7   	|        20MW 	|        30MW 	|
|    8   	|        24MW 	|        36MW 	|

## La scelta della Power Plant

Scegliere la PP ideale è una scelta estremamente delicata e complicata. Escludendo i moduli di Rating E e C, che personalmente vedo inutili, gli altri sono moduli utilizzabili per una vasta gamma di esigenze. Dobbiamo, innanzitutto considerare l'uso che faremo delle nostre navi: sono navi da battaglia? Cargo? Esploratori? Possiamo spegnere moduli mentre siamo in viaggio? Vogliamo che resti tutto sempre acceso anche quando gli hardpoint sono deployati? Facciamo un po' di considerazioni.

Come già detto, la PP si occupa di fornire corrente per tenere accesi ed in linea tutti i moduli. Quindi, come prima cosa, dobbiamo considerare la funzione della nostra nave ed i moduli che su essa abbiamo installato.<br>

* Su una **nave da battaglia** tipo, troveremo **scudi**, **armi**, **cell bank**, **shield booster**, **chaff** ed ogni sorta di accessorio che richiede tantissima energia per stare acceso e funzionare. Ci orienteremo perciò verso **moduli ad alta erogazione di potenza** e ad una ingegnerizzazione tale da tirare fuori anche il più miserabile dei watt per far sì che la nostra nave non si spenga appena fatto il deploy delle armi.
* Una **nave da carico**, probabilmente, avrà meno richiesta di corrente e quindi, per risparmiare peso e guadagnare in jump range, potremmo anche considerare un modulo di una classe inferiore rispetto a quella che normalmente monta la nostra nave.
* Se il nostro **cargo** può montare una PP massima di classe 7 ma non abbiamo scudi o armi e vediamo che essa è impiegata solamente la metà di quello normalmente utilizzato anche con gli hardpoint deployati, perché sprecare peso? In quel caso una PP di classe 5 potrebbe essere più che sufficiente, magari con una ingegnerizzazione blanda.
* Per una **nave da esplorazione** il discorso è similare ma dobbiamo prendere in considerazione anche l'efficienza della stessa. Se i moduli di classe D sono i più leggeri, questi hanno il difetto di avere una pessima efficienza e generare parecchio calore che, soprattutto in fase di fuel scooping e di carica del FSD, rischia di portare la temperatura della nave ben oltre il 100% ed iniziare a friggere i moduli.
  
Talvolta, la scelta ideale può essere quella di scendere di classe ma aumentare il rating andando a risparmiare sia peso che migliorando l'efficienza, pur mantenendo una generazione di corrente sufficiente dopo una piccola ingegnerizzazione.

Ad esempio, se per risparmiare peso sulla nostra nave avessimo pensato di montare una **Power Plant 4D**, potremmo accorgerci che semplicemente scendendo di una classe si potrebbe ottenere qualcosa di meglio:

| Modulo 	| Potenza 	| Peso           	| Efficienza 	|
|--------	|---------	|----------------	|------------	|
| 4D     	| 11,7MW  	| 4 Tonnellate   	| 0,7        	|
| **3A**   	| **12MW**	| **2,5 Tonnellate** 	| **0,4**  	|

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;In linea di massima, il consiglio che posso dare sull'utilizzo delle PP è il seguente:<ul>
<li>Utilizzare per la maggior parte dei casi un modulo di rating A, non necessariamente il top ma quello che a sufficienza riesce a fornire corrente alla vostra nave.</li>
<li>Utilizzare un modulo di rating B solamente nel caso di nave Hull Tank o Ramming Ship che richieda parecchia protezione dei moduli.</li>
<li>Utilizzare un modulo di rating D solamente nella classe 2 per navi da esplorazione a corto raggio o comunque nel caso in cui non vi interessi rischiare overheat della nave.</li>
<li>A meno che non sia a corto di denaro, evitare di usare moduli classe C ed E</li></ul></div>
<sup>Ovviamente tutto questo è valido per moduli non ingegnerizzati poiché, con l'ingegnerizzazione, molte delle caratteristiche possono cambiare</sup>

## Chi modifica la Power Plant?

Gli Ingegneri che modificano questo modulo sono tre:

| Nome                	| Grado massimo 	|
|---------------------	|:-------------:	|
| Felicity Farseer   	|       G1      	|
| Marco Qwent           |       G4     	    |
| **Hera Tani**         |       **G5**  	|

È quasi inutile dire che l'ottima [**Hera Tani**](/blog/speedguide-ingegneri-parte2#passo-dodici-hera-tani) è una scelta obbligatoria per poter tirare fuori il massimo dai nostri reattori nucleari. Un trucco potrebbe essere quello di pinnare la blueprint che utilizzeremo di più dalla signora di cui sopra ed un secondario, che magari non useremo fino al G5 Full, dal signor [Marco Qwent](/blog/speedguide-ingegneri-parte1#terzo-passo-marco-qwent), altrimenti visto come un mero passaggio verso il [**Professor Palin**](/blog/speedguide-ingegneri-parte1#quarto-passo-il-professor-palin).

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## Ingegnerizzare la Power Plant

Adesso che ne conosciamo per bene il funzionamento e a chi dobbiamo chiedere di metterci le mani sopra, passiamo ad analizzare le varie ingegnerizzazioni che sono disponibili per la PP, a quali casi si applicano e come vanno a modificare le specifiche di base.

## Armoured

L'ingegnerizzazione Armoured è più semplice da interpretare poiché essa consente un **aumento dell'integrità** della PP fino al 120%, rendendo di fatto il modulo blindato. In questo caso specifico, però, questa particolare ingegnerizzazione porta ad un ulteriore aumento della potenza erogata fino al 12%. 

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Ovviamente ci sono dei drawback anche abbastanza importanti e ciò riguardano un <b>aumento considerevole della massa</b>, fino al 40%, ed un incremento della <b>generazione di calore</b> fino al 9% in più.</div>

#### Quando usare questa ingegnerizzazione?

L'aumento dell'integrità della PP è sicuramente consigliato nel caso di **nave da battaglia** che faccia affidamento su armi a consumo medio e parecchia integrità strutturale.

Ma ragioniamo un secondo: sebbene l'aumento di integrità strutturale sia estremamente alto, ad esso non corrisponde un altrettanto evidente aumento di potenza erogata e ciò, soprattutto se il setup della nostra nave prevede armi o moduli ad alto consumo di energia, sconsiglia l'adozione di una PP Armoured. Sappiamo che scudi, shield booster, armi termiche come i beam laser e guardian shield reinforcement, vanno a pesare direttamente sulla PP, la quale verrà spremuta fino all'osso per tenere accesi tutti i moduli. Una soluzione potrebbe essere quella di disattivare il modulo FSD all'ingresso della battaglia e riattivarlo una volta vinta o quando le cose si mettono male. 

È altrettanto ovvio che il massimo lo si può ottenere da un modulo di **rating B**, tenendo comunque in conto che genererà più calore rispetto al corrispettivo A e sempre tenendo in considerazione la nave che stiamo ingegnerizzando e la sua capacità di disperdere il calore e la sua agilità, visto che il peso è sempre nemico di quest'ultima.

### Materiali Richiesti

- **G1**: 1x Worn Shield Emitters
- **G2**: 1x Carbon – 1x Shield Emitters
- **G3**: 1x Carbon – 1x High Density Composites – 1x Shield Emitters
- **G4**: 1x Proprietary Composites – 1x Shielding Sensors – 1x Vanadium
- **G5**: 1x Compound Shielding – 1x Core Dynamics Composites – 1x Tungsten

## Low Emissions

Low Emissions è una particolare ingegnerizzazione utile per **diminuire il calore generato** dal nostro beneamato reattore nucleare, tramite la diminuzione della potenza generata. Come abbiamo detto nella descrizione, i vari rating differiscono per efficienza e quindi maggiore efficienza equivale a minori emissioni di calore.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Questa modifica altro non fa che diminuire in percentuale il grado HE fino ad un <b>massimo del 65%</b>. Di contro, ahinoi, la <b>massa del modulo aumenterà</b> fino al 20% in più e la sua potenza massima erogata scenderà con un valore negativo fino al 15% rispetto allo standard.</div>

#### Quando usare questa ingegnerizzazione?

Il *"diaframmare"*, passatemi il termine, una PP ha senso se stiamo lavorando su una nave particolarmente fredda per scopi militari od esplorativi e se la stessa non sia esosa in termini di richieste di energia. Sicuramente il modulo ideale da ingegnerizzare, in questo caso, appartiene al rating A e solo in alcuni casi potrebbe essere conveniente il modulo di rating D.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Supponendo di voler realizzare una torpediniera invisibile, sappiamo che questa tipologia di armi non richiede un quantitativo abnorme di energia e, se escludiamo gli scudi che sono nemici dell'invisibilità, il resto dei moduli può essere ingegnerizzato per assorbire meno energia e quindi generare meno calore. A questo punto, l'adozione di un modulo di rating A ingegnerizzato low emission ha senso poiché va a diminuire ulteriormente il calore generato.</div>

Un altro caso in cui questa ingegnerizzazione è ideale è nella creazione di un piccolo bubble runner che richieda frequenti fuel scoop e che non assorba troppa energia. Qui, scontando un leggero aumento di peso, potremmo trasformare anche una PP rating D, in qualcosa che abbia una HE=0.26, quindi addirittura superiore ad una PP di rating A e, calcoli alla mano, di un pizzico più leggera anche se dovremo fare i conti con una generazione di energia molto ristretta.

### Materiali Richiesti

- **G1**: 1x Iron
- **G2**: 1x Iron – 1x Irregular Emission Data
- **G3**: 1x Heat Exchangers – 1x Iron – 1x Irregular Emission Data
- **G4**: 1x Germanium – 1x Heat Vanes – 1x Unexpected Emission Data
- **G5**: 1x Niobium – 1x Proto Heat Radiators – 1x Decoded Emission Data

## Overcharged

Questa modifica è da considerarsi l'evergreen delle modifiche. Così come il nome suggerisce, questa modifica permette al nostro reattore di lavorare in sovraccarico e **generare una potenza mostruosa, fino al 40% in più** rispetto al modulo base, scontando dei drawback non indifferenti quali la **perdita dell'integrità** fino al 50% ed il peggioramento, sempre fino al 50%, dell'heat efficiency. 

Un'ingegnerizzazione complessa ma che riesce a spremere al massimo il nostro modulo soprattutto in quelle situazione in cui l'economia generale della nostra nave sia particolarmente avida di energia.

#### Quando usare questa ingegnerizzazione?

Nella maggior parte dei casi, un overcharged risolve i problemi di generazione di energia di una nave. Questo purché si sia pronti a ad accettarne un riscaldamento maggiore ed una perdita di integrità che, a volte, può rendere un punto debole della nave ulteriormente critico. 

L'Overcharged, sicuramente, **dà il massimo su moduli di rating A e rating B** ma bisogna tenere a mente parecchie cose, soprattutto la nave sulla quale stiamo ingegnerizzando la PP. È vero che, salvo poche eccezioni, le navi grandi hanno una miglior dissipazione del calore e che quindi siano più tolleranti verso una PP di tipo overcharged ed il vantaggio di usarla è la possibilità di mantenere accesi più moduli esosi di energia, dei quali già abbiamo parlato in precedenza. Allo stesso tempo va considerato il fattore integrità.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Sappiamo che alcune navi hanno una PP particolarmente esposta (come l'Anaconda) e questa è mirata direttamente dagli avversari ma, allo stesso tempo, sappiamo che un buon setup richieda una buona PP in grado di erogare parecchia energia. Una soluzione potrebbe essere quella di utilizzare l'Overcharged, ma applicare in seguito un effetto speciale per recuperare questa integrità persa ed adottare qualche Module Reinforcement, che non fa mai male.</div>

### Materiali Richiesti

- **G1**: 1x Sulphur
- **G2**: 1x Conductive Components – 1x Heat Conduction Wiring
- **G3**: 1x Conductive Components – 1x Heat Conduction Wiring – 1x Selenium
- **G4**: 1x Cadmium – 1x Conductive Ceramics – 1x Heat Dispersion Plate
- **G5**: 1x Chemical Manipulators – 1x Conductive Ceramics – 1x Tellurium

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

## Effetti Speciali

Dopo questa carrellata di informazioni sicuramente sapremo qual è l'ingegnerizzazione che fa per noi. Ma visto che ogni ingegnerizzazione ha dei drawback, possiamo mitigarli od ignorarli ed aumentare ulteriormente la potenza frutto del sudore dei nostri beneamati modificatori folli.

Per la Power Plant gli effetti disponibili sono:

- Double Braced
- Stripped Down
- Thermal Spread
- Monstered

## Double Braced

Cosa c'è di meglio che ottenere un bel **bonus del 15%** nell'integrità senza ottenere svantaggi? Assolutamente nulla e questo fa il Double Braced: sostituisce parti di ferraglia varia e pesante con materiali più leggeri e resistenti. Ovviamente maggiore è il livello di integrità di base del nostro modulo ingegnerizzato, maggiore sarà l'efficacia dell'effetto Double Braced.

Per esempio, se l'integrità del modulo è 50 con un G1, dopo il Double Braced arriverà a 57-58. Se il modulo G5 ha integrità a 200, dopo questo effetto raggiungeremo 230.

#### Quando usare questo effetto?

Double Braced può essere utile in svariati casi, ma soprattutto se parliamo di **navi da guerra**. Come già dicevamo prima, un Overcharged va ad abbassare l'integrità strutturale della PP. Per mitigare questo effetto negativo, il Double Braced può essere una soluzione viabile, fermo restando che dobbiamo fare i conti con l'economia generale in termini di energia assorbita della nave.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Ipoteticamente, se abbiamo una nave sufficientemente agile e con una PP Overcharged G5 che copre perfettamente tutte le richieste energetiche, si può applicare questo effetto senza problemi di sorta. Analogamente un modulo di rating B, che ha già un peso ed una integrità superiori agli altri moduli, godrà dei vantaggi del Double Braced soprattutto se la nave che stiamo ingegnerizzando è pensata come Hull Tank.</div>

### Materiali Richiesti

- 5x Atypical Disrupted Wake Echoes
- 3x Galvanising Alloys
- 1x Configurable Components

## Stripped Down

Questo effetto altro non fa che alleggerire la PP di tutto quel metallaccio inutile che qualche geniale progettista ha deciso di mettere, sostituendolo con materiale più leggero **diminuendo la massa totale del 10%**.

#### Quando usare questo effetto?

Come abbiamo già detto più e più volte la massa, ed il conseguente peso, sono i nemici del jump range. I moduli che sicuramente giovano da questa ingegnerizzazione sono i **rating A** ed i **rating D** i quali, preferiti dagli esploratori, vanno ad ottimizzare ulteriormente il jump range.<br>
Non è difficile, quindi, trovare PP di rating A ingegnerizzate con un **G1 Overcharged** ed equipaggiata con lo **Stripped Down**. Questo fa sì che il calore generato resti molto basso ma, allo stesso tempo, aumenti quel tanto che basta la disponibilità di energia ed il peso venga ulteriormente ristretto.<br>
Per i moduli di rating D il discorso è un po' differente visto che, come abbiamo già parlato prima, l'unico modulo da adottare sarebbe il 2D per piccole navi saltatrici da "bubble".

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;In atri casi, lo Stripped Down può essere utilizzato anche sulle navi da battaglia che soffrono di problemi di agilità. Se la PP viene protetta a dovere, la combinazione Overcharged / Stripped Down riesce a togliere quel pizzico di massa in più che dona alla nave un leggero sprint. Capiamoci, parliamo di un 10%, ma su una PP classe 8 e rating A, sono <b>8 tonnellate in meno</b>.
<p>Infine, lo Stripped Down può anche mitigare gli svantaggi di un Armoured o una Low Emission, poiché non va ad incidere sull'integrità.</p></div>

### Materiali Richiesti

- 5x Grid Resistors
- 3x Vanadium
- 1x Proto Light Alloys

## Thermal Spread

Abbiamo visto che le PP generano un parte di energia ed una parte di calore che deve essere dissipato dalla nave. L'effetto Thermal Spread tende a mitigare questa sgradita conseguenza, **diminuendo del 10% il calore generato** dalla PP.

#### Quando usare questo effetto?

È molto interessante perché i casi sono vari. Thermal Spread può essere utile sia per il combattimento che per l'esplorazione. Talvolta, se si usano particolari armi su navi a bassa efficienza, in combattimento si può tranquillamente superare il 100% di heat della nave iniziando ad autoflagellare scafo e moduli soprattutto se si utilizza l'ingegnerizzazione Overcharged. Grazie al Thermal Spread possiamo limitare un po' questa controindicazione.<br>
Analogamente, esploratori che desiderano fare speed run e caricare il loro FSD mentre fanno fuel scoop sicuramente saranno ben felici di sacrificare un po' del loro jump range adottando la combinazione Low Emission / Thermal Spread. In questo modo una PP rating A G5 raggiunge la straordinaria HE=0.13.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Tutto fantastico? Analizziamo meglio le cose:
<p>Consideriamo che la differenza tra G5 Low Emission e G5 Low Emission / Thermal Spread è di solamente un miserabile HE=0.01, con una PP rating A, questo effetto, tendenzialmente, rende più fruibile un modulo di rating D che raggiungerà un HE=0.24 pur aumentando la massa a circa un 5% in meno rispetto ad un omologo di rating A standard.</p></div>

### Materiali Richiesti

- 5x Grid Resistors
- 3x Vanadium
- 1x Heat Vanes

## Monstered

Come il nome stesso suggerisce, questo effetto è in grado di rendere la PP *"mostruosa"*. Talmente mostruosa che aumenta la sua capacità di erogazione di corrente di un bel 5% rasentando il muro dei 53MW su una PP classe 8 e rating A. In questo caso, però, abbiamo uno scotto da pagare che equivale ad un **aumento di massa del 10%**.

#### Quando usare questo effetto?

Tendenzialmente, il Monstered è un effetto che viene usato sulle **navi da battaglia blindate** che hanno bisogno di una generazione massiccia di energia per tenere testa alle richieste di moduli ed armamenti.

Un esempio che può venirmi in mente, è sicuramente quello della **Federal Corvette**. Questa nave, soprattutto se equipaggiata con Beam Laser Huge, scudi di tipo Prismatic, Shield Boosters, Shield Cell Banks e Guardian Shield Reinforcements, diventa particolarmente esosa sotto il profilo energetico. Essendo la Corvette estremamente agile, il Monstered non va ad inficiarne particolarmente l'agilità ma garantisce la possibilità di tenere tutto acceso senza compromessi.

<div class="box">
<i class="fa fa-hand-o-right fa-lg" aria-hidden="true" style="color: #f07b05;"></i>&nbsp;<b>Pro Tip:</b>&nbsp;Si può affermare che il Monstered deve essere sempre utilizzato per scopi militari quando, nonostante un Overcharged, l'energia non sia sufficiente e si disponga di una nave che sia in grado di sostenere un incremento di massa senza comprometterne l'agilità.</div>

### Materiali Richiesti

- 5x Grid Resistors
- 3x Vanadium
- 1x Polymer Capacitors

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

### Chiacchiere e considerazioni

La Power Plant, oltre che essere fondamentale, è anche molto importante nell'economia della nave. È, sicuramente, la parte più delicata. Il punto di forza ed il tallone d'Achille, colei che permette ai nostri amati vascelli di stare in piedi. Talmente importante che, anche se si hanno le AFMU, non è possibile ripararla.

Va da se che la scelta sia delicata e bilanciarla diventa un'operazione abbastanza complessa. Diciamo che, sostanzialmente, io preferisco sempre utilizzare una PP di rating A nelle mie build visto che, ormai, ho trovato la mia dimensione con la modifica Overcharged per la quali totalità delle situazione. È, comunque, vero che **non sempre è necessaria una ingegnerizzazione G5 Full**. Molti dei miei vascelli esplorativi, difatti, si trovano bene con un semplice G1 Full Overcharged abbinato ad uno Stripped Down. Essendo navi deboli di natura, è inutile provare a rinforzare ciò che non può essere rinforzato.

Mi rendo conto, tuttavia, che non tutti i comandanti sono avvezzi ad avere un jump range estremo come quello che voglio raggiungere io e magari preferiscono avere una nave più fredda adottando il Low Emission su moduli rating A o D, sfruttando l'ulteriore vantaggio del Thermal Spread o andando a compensare l'aumento di peso con uno Stripped Down. Una mia fissazione particolare sta nel voler sempre realizzare navi che siano sempre in grado di mantenere acceso tutto in modo da non richiedere assestamento delle priorità.

Questo, ovviamente, è un mio gusto e ciò non rispecchia l'ottimale visto che, superando questo mio "limite", sarebbe possibile sicuramente fare infinite combinazioni: spegnere il modulo FSD per una nave silenziosa da stalking oppure alleggerire ulteriormente la PP alternando l'attivazione di scudi ed AFMU per una nave esplorativa e guadagnare ulteriore jump range.

Le combinazioni sono molteplici e spero di avervi dato un'idea di massima su come ingegnerizzare la vostra Power Plant.<br>
Al prossimo appuntamento!

<span class="image fit"><img src="/images/Elite-Division-png.png" alt=""></span>

#### Prosegui la lettura: [Engineering Workshop: Capitolo 4 - Sensors & Life Support](/blog/engineering-workshop-parte4/)
