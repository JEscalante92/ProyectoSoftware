devsocial.Views.UsuarioView = Backbone.View.extend({
	events:{
		"show" : "show"
	},
	className:"",
	initialize : function(data){
		self = this;
		this.template = swig.compile(data.template);
	},
	render: function(data) {
		var self = this
		var locals = {
			post: this.model.toJSON()
		};
		url = window.location.pathname.split('/')[1];
		if(url == 'usuarios'){
			locals.post.idiomas_join = "";
			for(var i=0; i < locals.post.idiomas.length; i++){
				if(i < (locals.post.idiomas.length-1)){
					locals.post.idiomas_join += locals.post.idiomas[i].idioma + ", ";
				}
				else{
					locals.post.idiomas_join += locals.post.idiomas[i].idioma;	
				}
			};
			this.$el.html(this.template(locals));
		}
		console.log(locals);
		this.$el.html(this.template(locals));
		return this;
	}
});
