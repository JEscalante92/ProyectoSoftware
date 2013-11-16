devsocial.Views.TecnologiaView = Backbone.View.extend({
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
		console.log(locals.post);
		this.$el.html(this.template(locals));
		return this;
	}
});