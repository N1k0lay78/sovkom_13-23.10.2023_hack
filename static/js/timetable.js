const on_click_table = (e) => {
    let elem = e.srcElement.parentElement.parentElement;
    let children = elem.parentElement.children;
    for (let i = 0; i < children.length; i++) {
        if (children[i] === elem) {
            children[i+1].classList.toggle("active")
        }
    }
}

let table_days = document.getElementsByClassName("timetable__day")

for (let i = 0; i < table_days.length; i++) {
    table_days[i].addEventListener('click', on_click_table)
}