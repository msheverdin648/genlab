$(document).ready(function(){


    //Настройка сайдбара
    if ($('.sidebar').hasClass('active')){
        if($('.sidebar').hasClass('active')){
            console.log('active')
        }
        $('.sidebar__open, .sidebar').on('click', function(){
            $('.sidebar, .sidebar__open').toggleClass('active');
        })
    }else{
        
        if($('.sidebar').hasClass('active')){
            console.log('active')
        }
        $('.sidebar__open').on('click', function(){
            $('.sidebar, .sidebar__open').toggleClass('active');
        })
    }




    //Настройка слайдеров
    $('.header__slider').slick({

        slidesToShow: 1,
        arrows: true,
        appendArrows: $('.header__slider'),
        nextArrow: '<button class="slick-next slick-arrow" aria-label="Next" type="button" style="">Следующий слайд</button>',
        prevArrow: false,

    })

    $('.news__slider').slick({
        slidesToShow: 2,
        slidesToScroll: 2,
    })





    //Настройка блока с Основными исследования
    $('.researches__items__item')
    .mouseenter( function(){
        $(this).addClass('active')
        &(this).siblings().removeClass('active')
    })
    .mouseleave( function(){
        $(this).removeClass('active')
    })


    //Настройка блока с часто задаваемыми вопросами 



    $('.list__item').on('click', function(){
            if ($(this).hasClass('active')){
                $(this).removeClass('active')
                $(this).children().removeClass('active')
                $(this).children().children().removeClass('active')
                $(this).children('.list__item__answer').slideUp()
            }else{
                $(this).siblings().removeClass('active')
                $(this).siblings().children().removeClass('active')
                $(this).siblings().children().children().removeClass('active')
                $(this).siblings().children('.list__item__answer').slideUp()

                $(this).addClass('active');  
                $(this).children('.list__item__answer').slideDown()
                $(this).children().addClass('active')
                $(this).children().children().addClass('active')

                
    
            };
    })
    
})