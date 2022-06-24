$(document).ready(function(){
    var owl = $('.owl-carousel');
    owl.owlCarousel({
        items:5,
        loop:true,
        margin:5,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
      
    });
    $('.play').on('click',function(){
        owl.trigger('play.owl.autoplay',[2000])
    })
    $('.stop').on('click',function(){
        owl.trigger('stop.owl.autoplay')
    })
  
});

$(document).ready(function(){
    var owl = $('.popular-product');
    owl.owlCarousel({
        items:5,
        loop:false,
        margin:10,
      
    });
    $('.play').on('click',function(){
        owl.trigger('play.owl.autoplay',[2000])
    })
    $('.stop').on('click',function(){
        owl.trigger('stop.owl.autoplay')
    })
  
});