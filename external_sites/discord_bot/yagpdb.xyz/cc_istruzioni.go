{{/* Custom Command */}}
{{/* Simile al join message, ricorda le regole base del server */}}
{{/* Utilizzo: -istruzioni */}}

{{ $icon := (joinStr "" "https://cdn.discordapp.com/icons/" (toString .Guild.ID) "/" .Guild.Icon ".png") }}
{{ $inara := "https://inara.cz/squadron/4750/"}}
{{ $website := "https://flottastellare.it" }}
{{ $fbpage := "https://www.facebook.com/Altocomandoflottastellare"}}
{{ $twitter:= "https://tinyurl.com/twitteracfs"}}
{{ $youtube := "https://tinyurl.com/videoacfs"}}
{{ $instagram := "https://tinyurl.com/instacfs"}}
{{ $discordserver := "https://discord.me/flottastellare" }}
{{ $homesystem := "Wong Sher" }}
{{ $avatar := (joinStr "" "https://cdn.discordapp.com/avatars/" (toString .User.ID) "/" .User.Avatar ".png") }}

{{$embed := cembed 
	"title" "Benvenuto sul nostro server Discord. Eccoti qualche informazione utile per iniziare..."
	"description" "\n\n1) Fai richiesta per lo Squadrone ingame, verrà accettata il prima possibile\n\n2) Fai richiesta su [Inara](https://inara.cz/squadron/4750/)\n\n3) Allinea cortesemente il tuo nickname a quello che usi in gioco\n\n**COLLEGAMENTI UTILI**" 
	"color" 0xf07b05 
	"fields" 
		(cslice 
			(sdict "name" "Link Inara" "value" $inara "inline" false) 
			(sdict "name" "Link al sito web" "value" $website "inline" false) 
			(sdict "name" "La nostra pagina Facebook" "value" $fbpage "inline" true)
			(sdict "name" "Discord" "value" $discordserver "inline" true) 
			(sdict "name" "Twitter" "value" $twitter "inline" true)
			(sdict "name" "Youtube" "value" $youtube "inline" true)
			(sdict "name" "Instagram" "value" $instagram "inline" true)
			(sdict "name" "Utenti del Server" "value" (toString .Guild.MemberCount) "inline" true) 
			(sdict "name" "Il nostro Home System" "value" $homesystem "inline" true)) 
			"author" 
				(sdict "name" "Alto Comando Flotta Stellare" "url" "https://flottastellare.it" "icon_url" "https://flottastellare.it/assets/icon/apple-icon-76x76.png") 
			"thumbnail" (sdict "url" $icon) 
			"footer" 
				(sdict "text" "YAGPDB.xyz, il tuo assistente di fiducia" "icon_url" "https://cdn.discordapp.com/avatars/204255221017214977/2fa57b425415134d4f8b279174131ad6.png") 
			"timestamp"  currentTime}}

{{ sendMessage nil $embed }}

{{/* Cancella il trigger che ha scatenato il messaggio */}}
{{ deleteTrigger 0 }}