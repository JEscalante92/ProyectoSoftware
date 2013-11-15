devsocial.Views.LogroView = Backbone.View.extend({
	tagName: "article",
	events:{
		"show" : "show"
	},
	className:"",
	initialize : function(model, template){
		this.model = model;
		self = this;
		this.template = swig.compile(template);
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
			console.log(locals.post);
			this.$el.html(this.template(locals));
		}
		// this.$el.html(this.template(locals));
		return this;
	}
});
