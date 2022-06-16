function check(params) {
    var name = document.forms.myform.name.value
    var type = document.forms.myform.type.value
    var model = document.forms.myform.model.value
    var plate = document.forms.myform.plate.value
    var kms = document.forms.myform.kms.value
    var service = document.forms.myform.service.value
    var date = document.forms.myform.date.value
    console.log(name,type)
    if (name==""||type==""||model==""||plate==""|kms==""||service==""||date=="") {
        alert("all fields must be filled")
        return false
    }

    if(name.length<=8){
        for(var i=0;i<name.length;i++)
        {
            if(!isNaN(name[i])){
                alert("Name cannot contain numbers")
                return false
            }
        }
    }else{
        alert("name cannot be more then 8 letters")
        return false
    }

    car_n = plate.split(" ")
    if (car_n.length==3) {
        if (!isNaN(car_n[2]) && car_n[2].length==4) {
            if (car_n[0]!="KA03") {
                alert("input format not correct")
                return false    
            }
        } else {
            alert("input format not correct")
            return false   
        }
    } else {
        alert("input format not correct")
        return false
    }



    if (kms>1000 && service=="free") {
        alert("free service not available for more then 1000km")
        return false
    }

    if (kms<1000 && service=="paid") {
        alert("minimum 1000km required for paid service")
        return false
    }

    
}
//q1
function allowOnlyLetters(e, t)   
{    
   if (window.event)    
   {    
      var charCode = window.event.keyCode;    
   }    
   else if (e)   
   {    
      var charCode = e.which;    
   }    
   else { return true; }    
   if ((charCode > 64 && charCode < 91) || (charCode > 96 && charCode < 123))    
       return true;    
   else  
   {    
      alert("Please enter only alphabets");    
      return false;    
   }           
} 
