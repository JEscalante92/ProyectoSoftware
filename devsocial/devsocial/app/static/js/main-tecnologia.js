var cargarTemplateTecnologia= function(){
	$.ajax({
		type: "GET",
		url: '../../templates/tecnologia',
		async: false,
		success: function(template){
			window.templates.tecnologia = template;
		}
	});
};
var cargarTemplateUsuario= function(){
	$.ajax({
		type: "GET",
		url: '../../templates/usuario',
		async: false,
		success: function(template){
			window.templates.usuario = template;
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
	var cantidad_usuarios = window.collections.usuarios.length;
	var xhr_usuarios = $.get('/api/tecnologia-user', {"start-index": window.collections.usuarios.length+1, tecnologia: tecnologia, format: 'json'});
	xhr_usuarios.done(function(data){
		data.forEach(function(item){
			window.collections.usuarios.add(item);
		});
		if(cantidad_usuarios == window.collections.usuarios.length){
			$('#usuarios-mas').hide();
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
	cargarTemplateTecnologia();
	cargarTemplateUsuario();
	tecnologia = window.location.pathname.split('/')[2];
	document.title = "Devsocial - "+ tecnologia;
	window.collections.usuarios = new devsocial.Collections.UsuariosCollection();
	window.collections.usuarios.on('add', function(item){
		var view = new devsocial.Views.UsuarioView({ model: item, tagName: "article", template: window.templates.usuario});
		view.render();
		view.$el.prependTo('#tecnologia-usuarios > section');
	});
	var xhr = $.get( "/api/tecnologias/", {search: tecnologia, format: "json"} );
	xhr.done(function(data){
		modelo = new devsocial.Models.TecnologiaModel(data[0]);
		if(data[0]){
			var view = new devsocial.Views.TecnologiaView({model: modelo, template: window.templates.tecnologia});
			view.render();
			view.$el.prependTo('#contenido-left');
			var xhr_usuarios = $.get('/api/tecnologia-user', {"start-index": window.collections.usuarios.length, tecnologia: tecnologia, format: 'json'});
			xhr_usuarios.done(function(data){
				data.forEach(function(item){
					item.arreglo = new Array(item.dominio);
					window.collections.usuarios.add(item);
				});
				if(data.length == 0){
					$('#tecnologia-usuarios > section').prepend('<p>No se han encontrado usuarios.</p>');
					$('#usuarios-mas').hide();
				};
				$('#usuarios-mas').on('click', cargar_users);
			});
		}
		else{
			var xhr_error = $.get('../../templates/error');
			xhr_error.done(function(data){
				$('#contenido').html('');
				$('#contenido').append(data);
			});
		}
	});
};
$(document).ready(inicio);