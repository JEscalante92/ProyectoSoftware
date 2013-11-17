$(function () {
	var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
	    headers: { "X-CSRFToken": $.cookie('csrftoken') }
	});
});
var inicio = function(){
	console.log('Starting app');
	window.templates.search_general = $('#contenido').html();
};
$(document).ready(inicio);