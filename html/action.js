var details;
var usernames = [];


function loginMessage(input){
  if(input == "Valid"){
    return "Valid Login";
  }
  return "Invalid Login";
}

function getPassword(){
  var username = document.getElementById("username");
  var value = username.value;
  if (usernames.includes(value)){
    for (var i=1; i < details.length;++i){
      if(details[i][0] == value){
        var password = document.getElementById("password"); 
        password.value = (details[i][1]);
      }
    }
  }
}

async function getUsername(){

  // data sent from the POST request
  var formData = new FormData(document.forms[0])

  // get all form keys and values
  var obj = Object.fromEntries(Array.from(formData.keys())
      .map(key => [key, formData.getAll(key).length > 1 ?
          formData.getAll(key) : formData.get(key)]))
  
  console.log(obj)
  var jsonreq = (`${JSON.stringify(obj)}`)

  const response = await fetch('http://127.0.0.1:8000/check-login/', {
  method: "POST",
  body: jsonreq,
  headers: {"Content-type": "application/json; charset=UTF-8"}
  })

  // Waits for a response and removes quotation at beginning and end.
  const responseText = await response.text();
  var receivedResponse = responseText.slice(1,responseText.length-1);

  // Splits string into arrays
  var splitString = receivedResponse.split(" ");
  if(splitString.length > 1){
    for (var i=1; i < splitString.length;++i){
      var tmp = splitString[i].split(",");
      splitString[i] = tmp;
    }
  }
  details = splitString;

  var hold=[]; // variable to store the options
  // Get an array of all the usernames
  for (var i=1; i < splitString.length;++i){
    hold.push(splitString[i][0])
  }
  usernames = hold;

  var str=''; // variable to store the options
  for (var i=0; i < hold.length;++i){
  str += '<option value="'+hold[i]+'" />'; // Storing options in variable
  }
  var my_list=document.getElementById("userlist");
  my_list.innerHTML = str;

}
///
// Submitting login details
///

async function SubmitLogin() {

    // data sent from the POST request
    var formData = new FormData(document.forms[0])

    // get all form keys and values
    var obj = Object.fromEntries(Array.from(formData.keys())
        .map(key => [key, formData.getAll(key).length > 1 ?
            formData.getAll(key) : formData.get(key)]))
    
    console.log(obj)
    var jsonreq = (`${JSON.stringify(obj)}`)

    const response = await fetch('http://127.0.0.1:8000/check-login/', {
    method: "POST",
    body: jsonreq,
    headers: {"Content-type": "application/json; charset=UTF-8"}
  })

  // Waits for a response and removes quotation at beginning and end.
  const responseText = await response.text();
  var receivedResponse = responseText.slice(1,responseText.length-1);

  // Splits string into arrays
  var splitString = receivedResponse.split(" ");
  if(splitString.length > 1){
    for (var i=1; i < splitString.length;++i){
      var tmp = splitString[i].split(",");
      splitString[i] = tmp;
    }
  }

  var hold=[]; // variable to store the options
  // Get an array of all the usernames
  for (var i=1; i < splitString.length;++i){
    hold.push(splitString[i][0])
  }

  // Now need to insert the saved usernames into 
  // username field and corresponding password field
  // look at onchange parameter

  var index_page = document.getElementById("answer"); 
  index_page.style.color = "blue"; 
  if(JSON.stringify(responseText).indexOf('Invalid') > -1){index_page.style.color = "red"};
  index_page.innerHTML = (loginMessage(splitString[0]));
}