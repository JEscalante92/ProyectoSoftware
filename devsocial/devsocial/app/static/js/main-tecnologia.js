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
	cargarTemplateTecnologia();
	tecnologia = window.location.pathname.split('/')[2];
	document.title = "Devsocial - "+ tecnologia;
	var xhr = $.get( "/api/tecnologias/", {search: tecnologia, format: "json"} );
	xhr.done(function(data){
		modelo = new devsocial.Models.TecnologiaModel(data[0]);
		if(data[0]){
			var view = new devsocial.Views.TecnologiaView(modelo, window.templates.tecnologia);
			view.render();
			view.$el.prependTo('#contenido-left');
		}
		else{
			var xhr_perfil = $.get('../../templates/error');
			xhr_perfil.done(function(data){
				$('#contenido').html('');
				$('#contenido').append(data);
			});
		}
	});
};
$(document).ready(inicio);