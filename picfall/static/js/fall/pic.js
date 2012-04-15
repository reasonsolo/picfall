window.Picture = 
function() { 
    return {
    api: PICTURE_API,
    parent_el: $('#pictures'),
    _defaults: function() {
                  return {
                      id: 0,
                      name: "",
                      image: "",
                      description: "",
                      uploader: null,
                      uploadtime: "",
                      liked: 0, 
                      repinned: 0,
                      commented: 0,
                      comments: null
                  };
              },
    _initialize: function(_id) {
                    if (typeof _id == undefined || _id == null) {
                        pics = $('.picture');
                        if (pics.length == 0) {
                            _id = 1;
                        } else {
                            _id = Number($(pics[pics.length - 1]).attr('data-id')) + 1;
                        }
                    }

                    this._id = _id;
                    this.parent_el = $('#pictures');
                    return this;
                },
    _display: function() {
                 if (typeof this.image == undefined
                         || this.id < 1) {
                     this._fetch();
                 }
                 $(this.parent_el).append(this._html());
                
             },
    _html: function() {
                comments_html = "";
               if (typeof this.comments != undefined 
                       || this.comments.length > 0) {
                   for (comment in this.comments) 
                    comments_html += comment._html();
               }
               return "<div class='span3 picture thumbnail' data-id='"+ this.id + "'>" 
                   + "<div class='action_btns'></div>"
                   + "<div class='image'><a><img src='"
                   + this.thumbnail
                   + "' /></a></div>"
                   + "<div class='caption'><div class='picture_stats'>" + this.liked + " likes " 
                   + this.repinned + " repins " + 
                   this.commented + " comments</div>"
                   + comments_html + "</div></div>";
           },
    _fetch: function() {
                // TODO: fetch data on server
                if (typeof this.id == undefined || this.id < 1) {
                    this._initialize();
                }
                pic_obj = this;
                $.get(PICTURE_API+this._id, {
                    'format': 'json'
                }, function(data) {
                    pic_obj._data(data);
                });
                return this;
           },
    _data: function(data) {
                if (typeof data != undefined && data != "") {
                    for (var field in data) {
                        this[field] = data[field];
                    }
                } else {
                    // TODO: alert this is an invalid picture
                    alert(data);
                }
           },
    _enlarge: function() {
                 // TODO: click on the picture and enlarge the block
             },
    _like: function() {
              // TODO: click the like button, send request to server
          },
    _unlike: function() {
                // TODO: if liked, click the unlike button, send request 
            },
    _repin: function() {
           },
    _fetch_related: function() {
                    },
    _fetch_comments: function() {

                     },
    _make_comment: function() {
                      // TODO
                  }
    };
};

window.Pictures = function() {
    return {
        page: 1,
        next: PICTURE_API,
        prev: null,
        offset: 0,
        total: 0,
        limit: 20,
        objects: new Array(),
        _objects: function(objects_data) {
                      if (typeof objects_data == undefined 
                              || objects_data == ""
                              || objects_data.length == 0) {
                          // FIXME 
                          return false;
                      }
                      for (pic in objects_data) {
                          new_pic = window.Picture();
                          new_pic._data(objects_data[pic]);
                          this.objects.push(new_pic);
                          new_pic._display();
                      }
                      return this.objects;
                  },
        _fetch_page: function(page) {
                         if (typeof this.next == undefined || this.next == "null")
                             return false;
                         obj = this;
                         $.get(this.next, {
                             'format': 'json'
                         }, function(data) {
                             if (obj._meta(data.meta)) {
                                if (obj._objects(data.objects)) 
                                    return;
                             }
                         });
                     },
        _meta: function(meta_data) {
                   if (typeof meta_data == undefined || meta_data =="") {
                       // FIXME 
                       alert("EMPTY");
                       return false;
                   }
                   this.prev = this.next;
                   for (field in meta_data) {
                       this[field] = meta_data[field];
                   }
                   return true;
               },
        _display_all: function() {
                          if (typeof this.objects == undefined)
                              return;
                          for (pic in this.objects) {
                              pic._display();
                          }
                      }

    }
}



