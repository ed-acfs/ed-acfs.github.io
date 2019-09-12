{{deleteTrigger 0}}
{{ $embed := cembed "title" "Ding dong, messaggio importante..." "image" (sdict "url" "https://flottastellare.it/images/bot/icanali.png") }}
{{ sendMessage nil $embed }}