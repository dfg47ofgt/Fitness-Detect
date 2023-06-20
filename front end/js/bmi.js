<<<<<<< HEAD
function countBMI()
{
    var a=document.getElementById("height").value;
    var b=document.getElementById("weight").value;
    /* var old=document.getElementById("age").value; */
    var bmi = '';
    bmi=(b/((a/100)*(a/100))).toFixed(1);
    document.getElementById("text").innerHTML= bmi;
    

    if(bmi > 24 || bmi == 24 )
    {
        document.getElementById("index").innerHTML= "過重";
    }
    else if((bmi > 18.5 && bmi < 24) || bmi == 18.5)
    {
        document.getElementById("index").innerHTML= "適中";
    }
    else 
    {
        document.getElementById("index").innerHTML= "過輕";
    }
}
function countTDEE()
{
    var a=document.getElementById("height").value;
    var b=document.getElementById("weight").value;
    var old=document.getElementById("age").value;
    var maleBMR, femaleBMR;
    var myselect = document.getElementById("activity-level");
    var value = myselect.options[myselect.selectedIndex].value;

        if (document.getElementById('male').checked == true)
        {
            maleBMR=((10*b)+(6.25*a)-(5*old))+5;
            /* document.getElementById("bmr_out").innerHTML= maleBMR */;
            document.getElementById("tdee_out").innerHTML = maleBMR*value;
        }
        else if(document.getElementById('female').checked == true)
        {
            femaleBMR=((10*b)+(6.25*a)-(5*old))-161;
            /* document.getElementById("bmr_out").innerHTML= femaleBMR; */
            document.getElementById("tdee_out").innerHTML = femaleBMR*value;
        }

=======
function countBMI()
{
    var a=document.getElementById("height").value;
    var b=document.getElementById("weight").value;
    /* var old=document.getElementById("age").value; */
    var bmi = '';
    bmi=(b/((a/100)*(a/100))).toFixed(1);
    document.getElementById("text").innerHTML= bmi;
    

    if(bmi > 24 || bmi == 24 )
    {
        document.getElementById("index").innerHTML= "過重";
    }
    else if((bmi > 18.5 && bmi < 24) || bmi == 18.5)
    {
        document.getElementById("index").innerHTML= "適中";
    }
    else 
    {
        document.getElementById("index").innerHTML= "過輕";
    }
}
function countTDEE()
{
    var a=document.getElementById("height").value;
    var b=document.getElementById("weight").value;
    var old=document.getElementById("age").value;
    var maleBMR, femaleBMR;
    var myselect = document.getElementById("activity-level");
    var value = myselect.options[myselect.selectedIndex].value;

        if (document.getElementById('male').checked == true)
        {
            maleBMR=((10*b)+(6.25*a)-(5*old))+5;
            /* document.getElementById("bmr_out").innerHTML= maleBMR */;
            document.getElementById("tdee_out").innerHTML = maleBMR*value;
        }
        else if(document.getElementById('female').checked == true)
        {
            femaleBMR=((10*b)+(6.25*a)-(5*old))-161;
            /* document.getElementById("bmr_out").innerHTML= femaleBMR; */
            document.getElementById("tdee_out").innerHTML = femaleBMR*value;
        }

>>>>>>> origin/main
}