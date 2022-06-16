function validate()
{
    var name = document.getElementById("name").value;
    var id = document.getElementById("id").value;
    var mob = document.getElementById("mob").value;
    var address = document.getElementById("address").value;
    var branch = document.getElementById("branch").value;
    var sem = document.getElementById("sem").value;
    var cgpa = document.getElementById("cgpa").value;
    var phoneno = /^\d{10}$/;
    
   if(name.trim()==""){
        document.getElementById("alertname").innerHTML = "<p>**Name Cannot be Blank</p>";
        return false;  
    }
    if(id.trim()==""){
        document.getElementById("alertid").innerHTML = "<strong><br>**Student ID needs to be provided. Eg:20181XYZ0000</strong>";
         return false;  
    }
   if(id.length>12){
    document.getElementById("alertid").innerHTML = "<strong><br>**ID cannot be more than 12 characters. Eg:20181XYZ0000</strong>";
    return false;  
   }
   if (id!= "20181CSE0621"){
    document.getElementById("alertid").innerHTML = "<strong><br>**Enter Valid ID format. Eg:20181XYZ0000</strong>";
    return false; 
   }
   if(mob.match(phoneno))
    {
        console.log("Phone no. valid");
    }else{
        document.getElementById("alertmob").innerHTML = "<strong><br>**Enter Valid mobile number. Eg:9876543210 </strong>";
        return false;
    }
    if(address.trim()==""){
        document.getElementById("alertaddr").innerHTML = "<strong><br>**Enter Valid address.</strong>";
        return false;
    }
    if(branch.trim()=="Select your branch"){
        document.getElementById("alertbranch").innerHTML = "<strong><br>**Choose from the menu.</strong>";
        return false;
    }
    if(sem.trim()==""){
        document.getElementById("alertsem").innerHTML = "<strong><br>**Enter Your Semester.</strong>";
        return false;
    }
    if(cgpa.trim()==""){
        document.getElementById("alertcgpa").innerHTML = "<strong><br>**Enter Your CGPA.</strong>";
        return false;
    }
}