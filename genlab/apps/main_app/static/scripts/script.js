$(document).ready(function(){

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
    
})