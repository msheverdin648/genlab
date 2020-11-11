$(document).ready(function(){

  function clean(){
    $('.search__list').children().remove(('li.search__list__item'))
  }

  function append(response){
    let range = response.types.length
    if (range > 6){
      range = 6
    }

    for (let index = 0; index < range; index++) {
      $('.search__list').append(
        '<li class="search__list__item"><a class="search__list__link" href="/research/'+ response.types[index].slug + '">' + response.types[index].type + '</a></li>'    
      )
    }
  }

  function send_get(){

    let serializedData = $('#search').serialize();

    $.ajax({
      url: $('#search').data('url'),
      data: serializedData,
      type: 'get',
      success: function(response){
        clean()
        append(response)
      },
      error: function(){
        clean()
        $('.search__list').append(
        '<li class="search__list__item search__list__item_not-found">Исследований не найдено</li>'    
        )
      }
    })

  }


  $('#search').on('input', function(){
    setTimeout(send_get, 1500)
  })



 

})


