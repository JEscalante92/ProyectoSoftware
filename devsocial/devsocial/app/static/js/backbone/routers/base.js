devsocial.Routers.BaseRouter = Backbone.Router.extend({
	routes: {
		"" :  "root",
		"usuarios/:nombre" : "perfil"
	},
	initialize : function(){
		var self = this;

	},
	root: function(){
		// var self = this;
		window.app.state = "root";
		console.log("root");
	},
	perfil: function(nombre){
		console.log("perfil",nombre);
		window.app.state = "perfil";
		window.app.perfil = nombre;
	}
});
