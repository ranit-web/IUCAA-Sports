class WallManager{
    constructor(){
        this.target = document.getElementsByClassName("wall")[0]
    }
    
    clear(){
        this.target.innerHTML = "";
    }

    add_section(text){
        this.target.innerHTML += `<div class="card span section">${text}</div>`
    }
    
    add_text(text){
        this.target.innerHTML += `<div class="card span text">${text}</div>`
    }

    add_card_event(event_title,event_msg,logo_path){
        this.target.innerHTML +=`
            <div class="card event">
                <img class="svg-logo" src="${logo_path}"></svg>
                <div class="text">
                    <div class="title">${event_title} ></div>
                    <div class="msg">${event_msg}</div>
                </div>
            </div>
        
        `
    }

}

wall = new WallManager()


// Tab Navigation
const tabs = document.querySelectorAll(".tab");
const headtext = document.querySelectorAll(".head-text")[0];
var page_depth=0;


const tabLabelToCallbackMap = {
    Home: onHomeClick,
    Events: onEventsClick
};


function onTabClick(event){
    // Pill effect works through css when activated
    tabs.forEach(tab=>{
        tab.classList.remove("active");
    });
    event.currentTarget.classList.add("active");
    
    // Navigation
    tab_label=event.currentTarget.getElementsByClassName("label")[0].innerText;
    headtext.innerHTML=tab_label
    
    // Callback
    tabLabelToCallbackMap[tab_label]();

}

tabs.forEach(tab=>{
    tab.addEventListener("click",onTabClick)
});


// ==================
// Default Tab - Link it to active tag
window.onload=function(){onHomeClick();}

function onHomeClick(){
    wall.clear();
    wall.add_section("Todays Events");
    wall.add_text("This section is under development.");
    wall.add_section("Yesterday Events");
    wall.add_text("This section is under development.");
}

function onEventsClick(){
    wall.clear();
    wall.add_card_event("Badminton","Starts from 2nd Jan","./media/badminton.svg");
    wall.add_card_event("Table Tennis","Starts from 2nd Jan","./media/table_tennis.svg");
    wall.add_card_event("Marathon","Starts from 2nd Jan","./media/marathon.svg");
    wall.add_card_event("Chess","Starts from 2nd Jan","./media/chess_queen.svg");
    wall.add_card_event("Cricket","Starts from 2nd Jan","./media/cricket.svg");

}







