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
		this.$el.html(this.template(locals));
		return this;
	}
});
