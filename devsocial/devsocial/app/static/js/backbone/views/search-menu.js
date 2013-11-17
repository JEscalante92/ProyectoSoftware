devsocial.Views.SearchMenuView = Backbone.View.extend({
	events:{
		"show" : "show",
		"click #general" : "general",
		"click #usuarios" : "usuarios",
		"click #tecnologias" : "tecnologias"
	},
	className:"",
	initialize : function(config){
		this.$el = config.$el;
		$general = this.$el.find('#contenido-general');
		$usuarios = this.$el.find('#contenido-usuarios');
		$tecnologias = this.$el.find('#contenido-tecnologias');
		this.templateUsuario();
		this.templateTecnologia();
		this.general();
	},
	templateUsuario : function(){
		$.ajax({
			type: "GET",
			url: '../../templates/usuario-search',
			async: false,
			success: function(template){
				window.templates.usuario = template;
			}
		});
	},
	templateTecnologia : function(){
		$.ajax({
			type: "GET",
			url: '../../templates/tecnologia-search',
			async: false,
			success: function(template){
				window.templates.tecnologia = template;
			}
		});
	},
	general : function(event){
		$general.show();
		$usuarios.hide();
		$tecnologias.hide();

		input_search = window.localStorage.getItem('input-search');
		window.collections.usuarios = new devsocial.Collections.UsuariosCollection();
		window.collections.usuarios.on('add', function(data){
			var view = new devsocial.Views.UsuarioView({ model: data, tagName: 'article', className : 'usuario', template: window.templates.usuario });
			view.render();
			view.$el.prependTo('#general-resultados');
		});
		
		window.collections.tecnologias = new devsocial.Collections.TecnologiasCollection();
		window.collections.tecnologias.on('add', function(data){
			var view = new devsocial.Views.TecnologiaView({model: data, className: 'tecnologia', template: window.templates.tecnologia});
			view.render();
			view.$el.prependTo('#general-resultados');
		});
		
		var xhr_usuarios = $.get('/api/usuarios', {"start-index": window.collections.usuarios.length, search: input_search, format: 'json'});
		xhr_usuarios.done(function(data){
			data.forEach(function(item){
				item.perfil.intereses = item.perfil.intereses.substring(0,140)+"...";;
				window.collections.usuarios.add(item);
			});
		});
		var xhr_tecnologias= $.get('/api/tecnologias', {"start-index": window.collections.tecnologias.length, search: input_search, format: 'json'});
		xhr_tecnologias.done(function(data){
			data.forEach(function(item){
				window.collections.tecnologias.add(item);
			});
		});
	},
	usuarios : function(event){
		$general.hide();
		$usuarios.show();
		$tecnologias.hide();
	},
	tecnologias : function(event){
		$general.hide();
		$usuarios.hide();
		$tecnologias.show();
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
