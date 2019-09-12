{{ $embed := cembed 
	"title" (joinStr "" "E' arrivato " .User.Username "!")
	 "description" "Buongiornissimoooo, kaffeeeee!!!"
	 "color" 0xf07b05 }}
{{ sendMessage nil $embed }}
