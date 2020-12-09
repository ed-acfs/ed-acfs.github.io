{{deleteTrigger 0}}
{{ $embed := cembed "title" "Attenzione! Ci sono delle conflict zone in corso! Chi chiamiamo?" "image" (sdict "url" "https://flottastellare.it/images/bot/cz.png") }}
{{ sendMessage nil $embed }}