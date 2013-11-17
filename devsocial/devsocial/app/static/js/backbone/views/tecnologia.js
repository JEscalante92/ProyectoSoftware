devsocial.Views.TecnologiaView = Backbone.View.extend({
	tagName: "article",
	events:{
		"show" : "show"
	},
	className:"",
	initialize : function(data){
		this.template = swig.compile(data.template);
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