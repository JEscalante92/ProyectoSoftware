devsocial.Views.UsuarioView = Backbone.View.extend({
	tagName: "article",
	events:{
		"show" : "show"
	},
	className:"",
	initialize : function(model){
		this.model = model;
		this.template = swig.compile($("#datosPersonales_tpl").html());
	},
	render: function(data) {
		function toString(arreglo){
			var cadena = "";
			var i = 0;
			for(i; i<arreglo.length; i++){
				if(i==0){
					cadena += arreglo[i];
				}
				else{
					cadena += " | " + arreglo[i];
				}
			}
			return cadena;
		}
		
		return this;
	}
});
