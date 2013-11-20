devsocial.Views.MenuModificarView = Backbone.View.extend({
	events:{
		"show" : "show",
		"click #personales" : "personales",
		"click #logros" : "logros",
		"click #habilidades" : "habilidades",
		"click #portafolio" : "portafolio",
		"click #contacto" : "contacto",
		"click #localidad" : "localidad"
	},
	className:"",
	initialize : function(config){
		this.$el = config.$el;
	},
	personales : function(event){
		window.location = '/modificar/personal';
	},
	logros : function(event){
		window.location = '/modificar/logros';
	},
	habilidades : function(event){
		window.location = '/modificar/habilidades';
	},
	portafolio : function(event){
		window.location = '/modificar/portafolio';
	},
	contacto : function(event){
		window.location = '/modificar/personal';
	},
	localidad : function(event){
		window.location = '/modificar/personal';
	},
	render: function(data) {
		var self = this
		var locals = {
			post: this.model.toJSON()
		};
		this.$el.html(this.template(locals));
		return this;
	}
});