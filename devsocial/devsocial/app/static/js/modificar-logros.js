var cargarTemplateLogro= function(){
	$.ajax({
		type: "GET",
		url: '../../templates/logro-edit',
		async: false,
		success: function(template){
			window.templates.logro = template;
		}
	});
};
$(function () {
	var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
	    headers: { "X-CSRFToken": $.cookie('csrftoken') }
	});
});
function httpGet(URL_string){
	var xmlHttp = null;
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open('GET', URL_string, false );
	xmlHttp.send( null );
	return xmlHttp.responseText;
};
var inicio = function(){
	console.log('Starting app');
	cargarTemplateLogro();
	window.collections.logros = new devsocial.Collections.LogrosCollection();
	window.collections.logros.on('add', function(model){
		var view = new devsocial.Views.LogroView(model, window.templates.logro);
		view.render();
		view.$el.appendTo('#contenido-logros');
		view.$el.addClass('logro');
	});
	var xhr_logros = $.get('/api/logros', {"start-index": window.collections.logros.length, username: window.usuarioactual, format: 'json'});
	xhr_logros.done(function(data){
		data.forEach(function(item){
			window.collections.logros.add(item);
		});
	});
};
$(document).ready(inicio);