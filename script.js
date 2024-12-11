// Pill effect for selected Tab
const tabs = document.querySelectorAll(".tab");

function onTabClick(event){
    tabs.forEach(tab=>{
        tab.classList.remove("active");
    });
    event.currentTarget.classList.add("active");
}

tabs.forEach(tab=>{
    tab.addEventListener("click",onTabClick)
});