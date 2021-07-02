{{deleteTrigger 1}}
{{ $embed := cembed "image" (sdict "url" "https://media.giphy.com/media/3og0INyCmHlNylks9O/giphy.gif")  }}
{{  sendMessage nil $embed }}