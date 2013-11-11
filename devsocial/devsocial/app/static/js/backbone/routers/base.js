CVitae.Routers.BaseRouter = Backbone.Router.extend({
	routes: {
		"" :  "root",
		"tecnologia/:nombre" : "tecnologiaSingle"
	},
	initialize : function(){
		var self = this;

	},
	root: function(){
		// var self = this;
		window.app.state = "root";
		console.log("root");
	},
	tecnologiaSingle: function(nombre){
		console.log("tecnologiaSingle",nombre);
		window.app.state = "tecnologiaSingle";
		window.app.tecnologia = nombre;
	}
});
