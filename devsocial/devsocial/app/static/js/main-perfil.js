var cargarTemplateLogro= function(){
	$.ajax({
		type: "GET",
		url: '../../templates/logro',
		async: false,
		success: function(template){
			window.templates.logro = template;
		}
	});
};
var cargarTemplatePerfil= function(){
	$.ajax({
		type: "GET",
		url: '../../templates/perfil',
		async: false,
		success: function(template){
			window.templates.perfil = template;
		}
	});
};
var cargarTemplateHabilidad= function(){
	$.ajax({
		type: "GET",
		url: '../../templates/habilidad',
		async: false,
		success: function(template){
			window.templates.habilidad = template;
		}
	});
};
var cargar_users = function(){
	var cantidad_logros = window.collections.logros.length;
	var xhr_logros = $.get('/api/logros', {"start-index": window.collections.logros.length, username: usuario, format: 'json'});
	xhr_logros.done(function(data){
		data.forEach(function(item){
			window.collections.logros.add(item);
		});
		if(cantidad_logros == window.collections.logros.length){
			$('#cargar-users').hide();
		}
	});
};
var cargar_habilidades = function(){
	var cantidad_habilidades = window.collections.habilidades.length;
	var xhr_habilidades = $.get('/api/habilidad', {"start-index": window.collections.habilidades.length, username: usuario, format: 'json'});
	xhr_habilidades.done(function(data){
		data.forEach(function(item){
			item.arreglo = new Array(item.dominio);
			window.collections.habilidades.add(item);
		});
		if(cantidad_habilidades == window.collections.habilidades.length){
			$('#cargar-habilidades').hide();
		}
	});
};
$(function () {
	var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
	    headers: { "X-CSRFToken": $.cookie('csrftoken') }
	});
});
var inicio = function(){
	console.log('Starting app');
	cargarTemplatePerfil();
	cargarTemplateLogro();
	cargarTemplateHabilidad();
	usuario = window.location.pathname.split('/')[2];
	document.title = "Perfil de "+ usuario;
	window.collections.logros = new devsocial.Collections.LogrosCollection();
	window.collections.logros.on('add', function(model){
		var view = new devsocial.Views.LogroView(model, window.templates.logro);
		view.render();
		view.$el.insertBefore('#perfil-logros > section > #cargar-users');
	});
	window.collections.habilidades = new devsocial.Collections.TecnologiasCollection();
	window.collections.habilidades.on('add', function(model){
		var view = new devsocial.Views.TecnologiaView(model, window.templates.habilidad);
		view.render();
		view.$el.insertBefore('#perfil-habilidades > section > #cargar-habilidades');
	});

	var xhr = $.get( "/api/usuarios/", {username: usuario, format: "json"} );
	xhr.done(function(data){
		modelo = new devsocial.Models.UsuarioModel(data[0]);
		if(data[0]){
			var view = new devsocial.Views.UsuarioView(modelo, window.templates.perfil);
			view.render();
			view.$el.appendTo('#contenido-wrapper');
			var xhr_logros = $.get('/api/logros', {"start-index": window.collections.logros.length, username: usuario, format: 'json'});
			xhr_logros.done(function(data){
				data.forEach(function(item){
					window.collections.logros.add(item);
				});
				if(data.length == 0){
					$('#perfil-logros > section').prepend('<p>No se han encontrado logros.</p>');
					$('#cargar-users').hide();
				};
				$('#cargar-users').on('click', cargar_users);
			});
			var xhr_habilidades = $.get('/api/habilidad', {"start-index": window.collections.logros.length, username: usuario, format: 'json'});
			xhr_habilidades.done(function(data){
				data.forEach(function(item){
					item.arreglo = new Array(item.dominio);
					window.collections.habilidades.add(item);
				});
				if(data.length == 0){
					$('#perfil-habilidades > section').prepend('<p>No se han encontrado habilidades.</p>');
					$('#cargar-habilidades').hide();
				};
				$('#cargar-habilidades').on('click', cargar_habilidades);
			});
		}
		else{
			var xhr_perfil = $.get('../../templates/error');
			xhr_perfil.done(function(data){
				$('#contenido-wrapper').append(data);
			});
		}
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