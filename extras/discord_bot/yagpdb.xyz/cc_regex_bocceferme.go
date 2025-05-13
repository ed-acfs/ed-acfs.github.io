{{/* Custom Command */}}
{{/* Tipo: Regex */}}
{{/* Trigger: (bocce ferme|boccia ferma) */}}
{{ $embed := cembed "title" "Bocce Ferme? Io non le vedo ferme! Prova a fermarle!" "image" (sdict "url" "https://cdn.discordapp.com/attachments/570677293693927434/1351220030091563079/images.steamusercontent.gif?ex=67da3df7&is=67d8ec77&hm=5e5876446832380d0542a69c41951b824981223020c6bc96f196cc373be47883&")  }}
{{  sendMessage nil $embed }}