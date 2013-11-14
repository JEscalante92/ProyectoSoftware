$(function () {
	var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
	    headers: { "X-CSRFToken": $.cookie('csrftoken') }
	});
});
var inicio = function(){
	console.log('Starting app');
	usuario = window.location.pathname.split('/')[2];
	var xhr = $.get( "/api/usuarios/", {username: usuario, format: "json"} );
	xhr.done(function(data){
		modelo = new devsocial.Models.UsuarioModel(data[0]);
		var xhr_perfil = $.get('../../templates/perfil');
		xhr_perfil.done(function(data){
			var view = new devsocial.Views.UsuarioView(modelo, data);
			view.render();
			view.$el.insertAfter('#perfil');
		});
	});
	/*$.post( "/api/habilidad/",{ dominio: 5, tecnologia: 3, usuario: 1})
		.done(function( data ) {
    		console.log(data)
  		})
  		.fail(function(data) {
			console.log(data);
	});*/
};
$(document).ready(inicio);