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
var inicio = function(){
	console.log('Starting app');
	cargarTemplateLogro();
	console.log(window.templates.logro);
};
$(document).ready(inicio);