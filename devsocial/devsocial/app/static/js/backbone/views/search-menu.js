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
		window.collections.tecnologias = new devsocial.Collections.TecnologiasCollection();
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
	cargarusers : function(){
		input_search = window.localStorage.getItem('input-search');
		var cantidad_usuarios = window.collections.logros.length;
		var xhr_usuarios = $.get('/api/usuarios', {"start-index": window.collections.usuarios.length + 1, search: search, format: 'json'});
		xhr_usuarios.done(function(data){
			data.forEach(function(item){
				window.collections.usuarios.add(item);
			});
			if(cantidad_usuarios == window.collections.usuarios.length){
				$('#cargar-users').hide();
			}
		});
	},
	cargartecnologias : function(){
		input_search = window.localStorage.getItem('input-search');
		var cantidad_tecnologias = window.collections.tecnologias.length;
		var xhr_tecnologias = $.get('/api/tecnologias', {"start-index": window.collections.tecnologias.length + 1, search: input_search, format: 'json'});
		xhr_tecnologias.done(function(data){
			data.forEach(function(item){
				window.collections.tecnologias.add(item);
			});
			if(cantidad_tecnologias == window.collections.tecnologias.length){
				$('#cargar-users').hide();
			}
		});
	},
	general : function(event){
		$general.show();
		$usuarios.hide();
		$tecnologias.hide();
		$boton = $('#cargar-users');
		$('#general-resultados').html('');
		$('#general-resultados').append($boton);
		input_search = window.localStorage.getItem('input-search');
		$boton.show();
		$boton.on('click', this.cargartecnologias);
		$boton.on('click', this.cargarusers);

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
		$boton = $('#cargar-users');
		$('#usuarios-resultados').html('');
		$('#usuarios-resultados').append($boton);
		$boton.show();
		$boton.on('click', this.cargarusers);
		input_search = window.localStorage.getItem('input-search');
		window.collections.usuarios = new devsocial.Collections.UsuariosCollection();
		window.collections.usuarios.on('add', function(data){
			var view = new devsocial.Views.UsuarioView({ model: data, tagName: 'article', className : 'usuario', template: window.templates.usuario });
			view.render();
			view.$el.prependTo('#usuarios-resultados');
		});
		var xhr_usuarios = $.get('/api/usuarios', {"start-index": window.collections.usuarios.length, search: input_search, format: 'json'});
		xhr_usuarios.done(function(data){
			data.forEach(function(item){
				item.perfil.intereses = item.perfil.intereses.substring(0,140)+"...";;
				window.collections.usuarios.add(item);
			});
		});

	},
	tecnologias : function(event){
		$general.hide();
		$usuarios.hide();
		$tecnologias.show();
		$boton = $('#cargar-users');
		$('#tecnologias-resultados').html('');
		$('#tecnologias-resultados').append($boton);
		$boton.show();
		$boton.on('click', this.cargarusers);
		input_search = window.localStorage.getItem('input-search');
		window.collections.tecnologias = new devsocial.Collections.TecnologiasCollection();
		window.collections.tecnologias.on('add', function(data){
			var view = new devsocial.Views.TecnologiaView({model: data, className: 'tecnologia', template: window.templates.tecnologia});
			view.render();
			view.$el.prependTo('#tecnologias-resultados');
		});
		var xhr_tecnologias= $.get('/api/tecnologias', {"start-index": window.collections.tecnologias.length, search: input_search, format: 'json'});
		xhr_tecnologias.done(function(data){
			data.forEach(function(item){
				window.collections.tecnologias.add(item);
			});
		});
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
