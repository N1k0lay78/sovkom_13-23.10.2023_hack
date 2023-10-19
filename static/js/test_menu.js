// menu
const on_click_spoiler = (e) => {
    e.srcElement.parentElement.children[1].classList.toggle("active")
}

let spoilers = document.getElementsByClassName("spoiler")

for (let i=0; i<spoilers.length; i++) {
    spoilers[i].addEventListener('click', on_click_spoiler)
}

// burger
const burger_togle = (e) => {
    document.getElementsByClassName("navigation")[0].classList.toggle("active")
}

document.getElementsByClassName("header__burger")[0].addEventListener("click", burger_togle)

// timetable
const on_click_day = (e) => {
    console.log("WORK")
    e.srcElement.parentElement.children[1].classList.toggle("active")
}

let days = document.getElementsByClassName("timetable__day")

for (let i=0; i<days.length; i++) {
    days[i].addEventListener('click', on_click_day)
}

  $('.timetable__element_1').on('click', function (e) {

            $('.timetable__wrapper').toggleClass('timetable__wrapper__active');
        })

