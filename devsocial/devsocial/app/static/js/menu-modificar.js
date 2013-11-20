$(function () {
	var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
	    headers: { "X-CSRFToken": $.cookie('csrftoken') }
	});
});
var inicio = function(){
	console.log('Starting app');
	window.templates.menu_modificar = $('#menu').html();
	window.menu_modificar = new devsocial.Views.MenuModificarView({$el: $('#menu')});
};
$(document).ready(inicio);