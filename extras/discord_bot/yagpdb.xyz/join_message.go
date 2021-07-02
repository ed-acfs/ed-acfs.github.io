{{/* Custom Embed di saluto ai nuovi utenti entrati sul server */}}

{{ $icon := (joinStr "" "https://cdn.discordapp.com/icons/" (toString .Guild.ID) "/" .Guild.Icon ".png") }}
{{ $inara := "https://inara.cz/squadron/4750/"}}
{{ $website := "https://flottastellare.it" }}
{{ $fbpage := "https://www.facebook.com/Altocomandoflottastellare"}}
{{ $homesystem := "Wong Sher" }}
{{ $avatar := (joinStr "" "https://cdn.discordapp.com/avatars/" (toString .User.ID) "/" .User.Avatar ".png") }}

{{$embed := cembed 
	"title" "Benvenuto sul nostro server Discord. Eccoti qualche informazione utile per iniziare...<:acfs:572729316861804554>" 
	"description" "\n\n1) Fai richiesta per lo Squadrone ingame, verrà accettata il prima possibile\n\n2) Fai richiesta su [Inara](https://inara.cz/squadron/4750/)\n\n3) Allinea cortesemente il tuo nickname su questo server a quello che usi in gioco\n\n4) Leggi per favore il regolamento su <#555350348013895701> e presentati in <#581916569140068378>\n\nSaremo lieti di accoglierti fra i membri della **Flotta Stellare**" 
	"color" 4645612 
	"fields" 
		(cslice 
			(sdict "name" "Link Inara" "value" $inara "inline" false) 
			(sdict "name" "Link al sito web" "value" $website "inline" false) 
			(sdict "name" "La nostra pagina Facebook" "value" $fbpage "inline" false) 
			(sdict "name" "Quanti Siamo" "value" (toString .Guild.MemberCount) "inline" true) 
			(sdict "name" "Home System" "value" $homesystem "inline" true) 
			(sdict "name" "Guild ID" "value" (toString .Guild.ID) "inline" true)) 
			"author" 
				(sdict "name" "Alto Comando Flotta Stellare" "url" "https://flottastellare.it" "icon_url" "https://flottastellare.it/assets/icon/apple-icon-76x76.png") 
			"thumbnail" (sdict "url" $icon) 
			"footer" 
				(sdict "text" "YAGPDB.xyz, il tuo assistente virtuale di fiducia" "icon_url" "https://cdn.discordapp.com/avatars/204255221017214977/2fa57b425415134d4f8b279174131ad6.png") 
			"timestamp"  currentTime}}

{{/* Tagga l'utente appena entrato sul server */}}
{{$ref_append := sendMessageNoEscapeRetID nil (joinStr "" "o7 "  .User.Mention ", benvenuto!")}} 

{{ sendMessage nil $embed }}