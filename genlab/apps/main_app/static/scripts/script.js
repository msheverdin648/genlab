$(document).ready(function(){



    


    //Настройка блока с Основными исследования
    $('.researches__items__item')
    .mouseenter( function(){
        $(this).addClass('active')
        $(this).siblings().removeClass('active')
    })
    .mouseleave( function(){
        $(this).removeClass('active')
    })

    //Настройка меню бургера
        $('.menu_burger__button').on('click', function(){
            $(this).toggleClass('active')
            $('.sidebar__column').toggleClass('active')
            $('body').toggleClass('_lock')
        })


    //Настройка сайдбара
    if ($('.sidebar').hasClass('active')){
        if($('.sidebar').hasClass('active')){
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
        dots: true,
        responsive: [
            {
              breakpoint: 641,
              settings: {
                arrows: false
              }
            }
          ],

    })

    $("#slider-nav-1 .num__all").text("0" + $("#slider-1 ul li").length)

    $(".header__slider").on("afterChange", function(event, slick, currentSlide, nextSlide){
        $("#slider-nav-1 .num__this").text( '0'+ (currentSlide+1));
    })

    $('.news__slider').slick({
        slidesToShow: 2,
        slidesToScroll: 2,
        appendArrows: $('.news__navigate'),
        nextArrow: '<button class="slick-next slick-arrow" aria-label="Next" type="button" style="">Следующий слайд</button>',
        prevArrow: '<button class="slick-prev slick-arrow" aria-label="Prev" type="button" style="">Предыдущий слайд</button>',
        dots: true,
        responsive: [
            {
              breakpoint: 641,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                nextArrow: '<button class="slick-next slick-arrow" aria-label="Next" type="button" style=""></button>',
                prevArrow: '<button class="slick-prev slick-arrow" aria-label="Prev" type="button" style=""></button>',
              }
            }
          ],
    })


    $("#slider-nav-2 .num__all").text("0" + $("#slider-2 ul li").length)

    $(".news__slider").on("afterChange", function(event, slick, currentSlide, nextSlide){
        $("#slider-nav-2 .num__this").text('0' +( $('li.slick-active').text() - '10'));

    });

    $('.news__slider_2').slick({
        
        dots: true,    
        arrows: true,          
        slidesToShow: 1,
        slidesToScroll: 1,
        appendArrows: $('.news__navigate'),
        nextArrow: '<button class="slick-next slick-arrow" aria-label="Next" type="button" style="">Следующий слайд</button>',
        prevArrow: '<button class="slick-prev slick-arrow" aria-label="Prev" type="button" style="">Предыдущий слайд</button>',
        responsive: [
            {
              breakpoint: 641,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                nextArrow: '<button class="slick-next slick-arrow" aria-label="Next" type="button" style=""></button>',
                prevArrow: '<button class="slick-prev slick-arrow" aria-label="Prev" type="button" style=""></button>',
              }
            }
          ],

    })


    $("#slider-nav-4 .num__all").text("0" + $("#slider-4 ul li").length)

    $(".news__slider").on("afterChange", function(event, slick, currentSlide, nextSlide){
        $("#slider-nav-4 .num__this").text('0' +( $('li.slick-active').text() - '10'));

    });


    $('.partners__slider').slick({
        slidesToShow: 4,
        slidesToScroll: 4,
        appendArrows: $('.partners__navigate'),
        nextArrow: '<button class="slick-next slick-arrow" aria-label="Next" type="button" style="">Следующий слайд</button>',
        prevArrow: '<button class="slick-prev slick-arrow" aria-label="Prev" type="button" style="">Предыдущий слайд</button>',
        dots: true,
        responsive: [
            {
              breakpoint: 641,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                nextArrow: '<button class="slick-next slick-arrow" aria-label="Next" type="button" style=""></button>',
                prevArrow: '<button class="slick-prev slick-arrow" aria-label="Prev" type="button" style=""></button>',
              }
            }
          ],
        
    })


    $("#slider-nav-3 .num__all").text("0" + $("#slider-3 ul li").length)

    $(".partners__slider").on("afterChange", function(event, slick, currentSlide, nextSlide){
        $("#slider-nav-3 .num__this").text('0' + ($('li.slick-active').text()-'10'));

    
    });










    $('.sublist__navigate').on('click', function(){
        if ($(this).hasClass('active')){
            $(this).removeClass('active')
            $(this).parent().removeClass('active')
            $(this).parent().siblings().slideUp()
        }else{
            $(this).addClass('active')
            $(this).parent().addClass('active')
            $(this).parent().siblings().slideDown()
        }
    })



    //Настройка блока с часто задаваемыми вопросами 



    


    $('.list__header').on('click', function(){
        if ($(this).hasClass('active')){
            $(this).removeClass('active')
            $(this).children().removeClass('active')
            $(this).parent().removeClass('active')
            $(this).parent().parent().removeClass('active')
            $(this).siblings().slideUp()
            
        }else{
            $(this).addClass('active')
            $(this).children().addClass('active')
            $(this).parent().addClass('active')
            $(this).parent().parent().addClass('active')
            $(this).slideDown()
            $(this).siblings().slideDown()
            $(this).parent().siblings().children('.list__item__answer').slideUp()
            $(this).parent().siblings().children('.sublist').slideUp()
            $(this).parent().siblings().children('.list__header').removeClass('active')
            $(this).parent().siblings().children('.list__header').children().removeClass('active')
            $(this).parent().siblings().removeClass('active')
        };
})

//Настройка сворачивания карточек

    $('.card__navigate').on('click', function(){
        if($(this).hasClass('active')){
            $(this).removeClass('active')
            $(this).siblings('.full').slideUp()
        }else{
            $(this).addClass('active')
            $(this).siblings('.full').slideDown()  
        }
    })



    $('.open-button').on('click', function(){
        $(this).siblings('.list__text--hide_text').toggleClass('hide')
        $(this).siblings('.dots').toggleClass('hide')
        $(this).toggleClass('active')
    })

    $(".news-card__view").on('click', function(){

            if ($(this).parent().siblings('.news-card__text_full').hasClass('active')) {
                $(this).parent().siblings('.news-card__text_full').slideUp()
                $(this).parent().siblings('.news-card__text_full').removeClass('active')
                $(this).removeClass('active')
            }else if(!($(this).parent().siblings('.news-card__text_full').hasClass('active'))){
                $(this).parent().siblings('.news-card__text_full').slideDown()
                $(this).parent().siblings('.news-card__text_full').addClass('active')
                $(this).addClass('active')
            }

    })
})