var inicio = function(){
	console.log('Starting app');
	var xhr = $.get( "/usuarios/", {username: "devsocial", format: "json"} );
};
$(document).ready(inicio);