$(function () {
	var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
	    headers: { "X-CSRFToken": $.cookie('csrftoken') }
	});
});
var inicio = function(){
	console.log('Starting app');
	var xhr = $.get( "/api/usuarios/", {username: "devsocial", format: "json"} );
	console.log(xhr)
	
	$.post( "/api/habilidad/",{ dominio: 5, tecnologia: 3, usuario: 1})
		.done(function( data ) {
    		console.log(data)
  	});
};
$(document).ready(inicio);