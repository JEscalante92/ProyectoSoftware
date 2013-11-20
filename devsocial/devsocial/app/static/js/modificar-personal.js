$(function () {
	var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
	    headers: { "X-CSRFToken": $.cookie('csrftoken') }
	});
});
var inicio = function(){
	$('#setLocalidad').on('click', function(event){
		$.ajax({
		type: "PUT",
		url: '../api/ipedit',
		success: function(data){
			$('txtLocalidad').val(data);
		}
	});
	});
};
$(document).ready(inicio);