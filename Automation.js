//Auto like/follow/and any task automate
function WebsiteAutomation(){
    let Class_Name = prompt("btn class Element Name : ")
    confirm("Checking ..!")
    let Action_Name = document.querySelectorAll('.'+Class_Name);
        if(Action_Name.lenght==0){
            alert(Class_Name+"is invailed please try next")
            return false
        }
        else{
            Action_Name.foreach(btn => btn.click())
        }
};
WebsiteAutomation()
