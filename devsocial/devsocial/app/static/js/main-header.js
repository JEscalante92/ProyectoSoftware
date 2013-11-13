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
var funcion_header = function(){
	$($('#header-search').parent()).on("click", activar_Busqueda);
	$($('#header-usuario').parent()).on("mouseenter", activar_menu);
	$($('#header-usuario').parent()).on("mouseleave", desactivar_menu);
}
$(window).on("ready", funcion_header);