window.Picture = Backbone.Model.extend({

    defaults: function() {
                  return {
                      name: "",
                      image: "",
                      description: "",
                      uploader: "",
                      uploadtime: "",
                      liked: 0, 
                      repinned: 0
                  };
              },
    url: function() {
             return this.get('resource_uri') || this.collection.url;
         },
    toggle: function() {
                // TODO
            },
    clear: function() {
               this.destroy();
            }
});

window.Pictures = Backbone.Collection.extend({
    url: PICTURE_API,
    parse: function(data) {
        return data.objects;
    }
});

window.PictureView = Backbone.View.extend({
    tagName: 'div',
    className: 'picture',
    template: _.template($('#picture-template').html()),
    events: {
    },
    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
    }
});


