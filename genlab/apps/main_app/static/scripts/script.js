$(document).ready(function(){


    //Настройка блока с Основными исследования
    $('.researches__items__item')
    .mouseenter( function(){
        $(this).addClass('active')
        &(this).siblings().removeClass('active')
    })
    .mouseleave( function(){
        $(this).removeClass('active')
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
    })


    $("#slider-nav-2 .num__all").text("0" + $("#slider-2 ul li").length)

    $(".news__slider").on("afterChange", function(event, slick, currentSlide, nextSlide){
        $("#slider-nav-2 .num__this").text('0' +( $('li.slick-active').text() - '10'));

    });


    $('.partners__slider').slick({
        slidesToShow: 4,
        slidesToScroll: 4,
        appendArrows: $('.partners__navigate'),
        nextArrow: '<button class="slick-next slick-arrow" aria-label="Next" type="button" style="">Следующий слайд</button>',
        prevArrow: '<button class="slick-prev slick-arrow" aria-label="Prev" type="button" style="">Предыдущий слайд</button>',
        dots: true,
        
    })


    $("#slider-nav-3 .num__all").text("0" + $("#slider-3 ul li").length)

    $(".partners__slider").on("afterChange", function(event, slick, currentSlide, nextSlide){
        $("#slider-nav-3 .num__this").text('0' + ($('li.slick-active').text()-'10'));

    
    });









    $('.researches__list__item__header').on('click', function(){
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
            $(this).siblings().slideDown()
        }
    })

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



    $('.list__item__question').on('click', function(){
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
                $(this).siblings().slideDown()

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


    
})