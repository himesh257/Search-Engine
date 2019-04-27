const $ = require('jquery')

$(document).ready(function(){
    $('#pdf').click(function(){
            $(".results").append('<div class="card"><div class="card-body"><a id="link" href=#>This is some text within a card body.</a></div></div><button type="button" class="btn btn-outline-success">Add</button>');
            
            
    })
    
    $('#url').click(function(){
            $(".results").append('<div class="card"><div class="card-body"><a id="link" href=#>This is some text within a card body.</a></div></div><button type="button" class="btn btn-outline-success">Add</button>');
            
    })
})

