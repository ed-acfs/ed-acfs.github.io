{{ $embed := cembed 
	"title" (joinStr "" "E' arrivato " .User.Username "!")
	 "description" "Buongiornissimoooo, kaffeeeee!!!"
	 "color" 0xf07b05 }}
{{ sendMessage nil $embed }}

{{ $embed := cembed 
	"title" (joinStr "" "La festa è finita. È con noi " .User.Username "!")
	 "description"  (joinStr "" "Buongiornissimoooo, kaffééééééééé!!!! Buon " currentTime.Day " del mese a tutti!!!!!!")
	 "color" 0xf07b05 }}
{{ sendMessage nil $embed }}

{{ $embed := cembed 
	"title" (joinStr "" "Lodiamo il sole! È arrivato " .User.Username "!")
	 "description" "Buongiornissimoooo!!! Tutto beneeee???"
	 "color" 0xf07b05 }}
{{ sendMessage nil $embed }}
