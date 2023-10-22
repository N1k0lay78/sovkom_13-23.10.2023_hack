$('.nav__button').on('click', function (e) {
    e.preventDefault();
    $('.nav').toggleClass('nav__active');
    $('.header').toggleClass('header__active');
    $('.main').toggleClass('main__active');
    $('.footer').toggleClass('footer__active');
})
$('.nav__wrapper__menu__ul__li').on('click', function (j) {
    $('.nav__wrapper__menu__ul__li__inside__ul').toggleClass('nav__wrapper__menu__ul__li__inside__ul__active');

})
$('.nav__wrapper__menu__ul__li_1').on('click', function (event) {
    const clickedElement = $(event.target);
    const targetElement = clickedElement.closest('.nav__wrapper__menu__ul__li_1');
    $(targetElement).children()[1].children[0].classList.toggle('nav__wrapper__menu__ul__li__inside__ul_1__active_1')
})
$('.nav__wrapper__menu__ul__li_2').on('click', function (j) {
    $('.nav__wrapper__menu__ul__li__inside__ul_2').toggleClass('nav__wrapper__menu__ul__li__inside__ul_2__active_2');
})
$('.nav__wrapper__menu__ul__li_3').on('click', function (j) {
    $('.nav__wrapper__menu__ul__li__inside__ul_3').toggleClass('nav__wrapper__menu__ul__li__inside__ul_3__active_3');
})
$('.nav__wrapper__menu__ul__li_4').on('click', function (j) {
    $('.nav__wrapper__menu__ul__li__inside__ul_4').toggleClass('nav__wrapper__menu__ul__li__inside__ul_4__active_4');
})
$('.nav__wrapper__menu__ul__li_5').on('click', function (j) {
    $('.nav__wrapper__menu__ul__li__inside__ul_5').toggleClass('nav__wrapper__menu__ul__li__inside__ul_5__active_5');
})
$('.nav__wrapper__menu__ul__li_6').on('click', function (j) {
    $('.nav__wrapper__menu__ul__li__inside__ul_6').toggleClass('nav__wrapper__menu__ul__li__inside__ul_6__active_6');
})
$('.nav__wrapper__menu__ul__li_7').on('click', function (j) {
    $('.nav__wrapper__menu__ul__li__inside__ul_7').toggleClass('nav__wrapper__menu__ul__li__inside__ul_7__active_7');
})