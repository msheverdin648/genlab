$(document).ready(function(){


  function send_get(){

    let serializedData = $('#search').serialize();

    $.ajax({
      url: $('#search').data('url'),
      data: serializedData,
      type: 'get',
      success: function(response){
        $('.search__header').append(
            '<h2>' + response.types[0].type + '</h2>'
        )
      }
    })

  }


  $('#search').on('input', function(){
    setTimeout(send_get, 1500);
  })

})


