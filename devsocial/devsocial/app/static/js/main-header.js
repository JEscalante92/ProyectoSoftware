var activar_Busqueda = function(event){
	var objeto = $(this).children();
	$(objeto).addClass("search-active");
	$(objeto.children()[0]).on("click", desactivar_Busqueda);
};
var activar_menu = function(event){
	$("#header-menu").addClass("menu-active");
};
var desactivar_menu = function(event){
	$("#header-menu").removeClass("menu-active");
};
var desactivar_Busqueda = function(event){
	var lista_search = $(this).parents()[1];
	var header_search = $(this).parents()[0];
	$(header_search).removeClass("search-active");
	$(lista_search).on("click", activar_Busqueda);
	event.stopPropagation();
};
var buscar = function(event){
	if(event.keyCode == 13) {
		valor = $('#input-search').val();
		console.log(valor);
        window.location = "/search"
        window.localStorage.setItem('input-search', valor);
    }
};
var cargar = function(event){
	valor = window.localStorage.getItem('input-search');
	$('#input-search').val(valor);
};
var funcion_header = function(){
	$($('#header-search').parent()).on("click", activar_Busqueda);
	$($('#header-usuario').parent()).on("mouseenter", activar_menu);
	$($('#header-usuario').parent()).on("mouseleave", desactivar_menu);
	$('#input-search').keyup(buscar);
	cargar();
}
$(window).on("ready", funcion_header);