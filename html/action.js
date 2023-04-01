async function SubmitLogin() {

    // data sent from the POST request
    var formData = new FormData(document.forms[0])

    // get all form keys and values
    var obj = Object.fromEntries(Array.from(formData.keys())
        .map(key => [key, formData.getAll(key).length > 1 ?
            formData.getAll(key) : formData.get(key)]))

    var jsonreq = (`${JSON.stringify(obj)}`)

    const response = await fetch('http://127.0.0.1:8000/check-login/', {
    method: "POST",
    body: jsonreq,
    headers: {"Content-type": "application/json; charset=UTF-8"}
  })

  // Waits for a response and inserts the result
  const responseText = await response.text();
  var index_page = document.getElementById("answer"); 
  index_page.style.color = "blue"; 
  if(JSON.stringify(responseText).indexOf('Invalid') > -1){index_page.style.color = "red"};
  index_page.innerHTML = (responseText);
}