$(function () {
	var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
	    headers: { "X-CSRFToken": $.cookie('csrftoken') }
	});
});
var inicio = function(){
	console.log('Starting app');
	window.templates.search_general = $('#contenido').html();
	window.search_menu = new devsocial.Views.SearchMenuView({$el: $('#contenido')});
};
$(document).ready(inicio);