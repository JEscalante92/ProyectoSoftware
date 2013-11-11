CVitae.Views.TecnologiaView = Backbone.View.extend({
	tagName: "article",
	events:{
		"click img" : "navigate"
	},
	className:"",
	initialize : function(model){
		var self = this;
		this.model = model;
		this.model.on("change", function(){
			self.render();
		});
		window.routers.base.on("route:root", function(){
			self.render();
		});
		window.routers.base.on("route:tecnologiaSingle", function(){
			self.render();
		});
		this.template = swig.compile($("#Tecnologia_tpl").html());
		this.templateExtended = swig.compile($("#TecnologiaExtended_tpl").html());
	},
	navigate : function(event){
		console.log("click");
		Backbone.history.navigate("tecnologia/"+this.model.get("nombre"), {trigger: true});
	},
	render: function(data) {
		var self = this;
		var locals ={
			post: this.model.toJSON()
		};
		if(window.app.state === "tecnologiaSingle"){
			this.$el.remove();
			if(window.app.tecnologia === this.model.get("nombre")){
				this.$el.html(this.templateExtended(locals));	
				this.$el.appendTo("#tecnologias section");
				this.$el.removeClass("tecnologiaSingle");
				this.$el.addClass("tecnologiaExtended");
			}
		}
		else{
			this.$el.removeClass("tecnologiaExtended");
			this.$el.addClass("tecnologiaSingle");
			this.$el.html(this.template(locals));
			this.$el.appendTo("#tecnologias section");
			this.delegateEvents(this.events); 
		}
		return this;
	}
});
