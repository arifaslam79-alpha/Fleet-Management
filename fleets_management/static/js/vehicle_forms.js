const formElem = document.getElementById('vehicle_form');
formElem.onsubmit = async (e) => {
    e.preventDefault();
	const data=new FormData(form);
	let response = await fetch('vehicle-add', {
		method: 'POST',
		body: data
	});
	let result = await response.json();
	
	if(result.message != '') {
		document.getElementById('success_message').innerHTML = result.message
	} else if(result.errors != '') {
		alert(result.errors)
	}  else if(result.error != '') {
		alert(result.error)
	}
};