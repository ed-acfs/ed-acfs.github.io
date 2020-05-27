{{deleteTrigger 1}}
{{ $embed := cembed "image" (sdict "url" "https://media.giphy.com/media/l46CimW38a7TFxLVe/giphy.gif")  }}
{{  sendMessage nil $embed }}