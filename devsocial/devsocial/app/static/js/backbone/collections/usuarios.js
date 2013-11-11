devsocial.Collections.UsuariosCollection = Backbone.Collection.extend({

    model: devsocial.Models.UsuarioModel,
    url:"",
    search : function(letters){
        if(letters == "") return this;
        var pattern = new RegExp(letters,"gi");
        return _(this.filter(function(data) {
            return pattern.test(data.get("name"));
        }));
    },
    comparator : function(item){
        return item.get("name");    
    },
    getOne : function(id){
        return this.filter(function(data) {
            return data.get("id") == id;
        });
    },
    parse : function(resp) {
        return resp.data;
    },
    render : function(){
        
    }
});

devsocial.Collections.usuarios = devsocial.Collections.UsuariosCollection;